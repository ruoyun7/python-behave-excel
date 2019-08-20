import pandas as pd
import os
import requests
import json
import numpy as np


class ExcelRequester(object):
    def __init__(self, excel_path):
        self.excel_path = excel_path

    def register_request_callback(self, callback):
        self.callback = callback

    def read_excel_row(self):
        df = pd.read_excel(self.excel_path)
        # print(df.head())
        test_data = []
        for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
            # 根据i来获取每一行指定的数据 并利用to_dict转成字典
            row_data = df.loc[i, ['No', 'URL', 'Method', 'Headers', 'Cookies', 'Params', 'Expect', 'Status']].to_dict()
            test_data.append(row_data)
        print("最终获取到的数据是：{0}".format(test_data))
        return test_data

    def run(self):
        test_datas = self.read_excel_row()
        results = []
        df_no = []
        df_url = []
        df_method = []
        df_params = []
        df_headers = []
        df_cookies = []
        df_expect = []
        df_status = []
        df_result = []
        for item in test_datas:
            no = item["No"]
            url = item["URL"]
            method = item["Method"].upper()
            params = json.loads(item["Params"]) if not pd.isna(item["Params"]) else {}
            try:
                headers = json.loads(item["Headers"]) if not pd.isna(item["Headers"]) else {}
            except:
                from lib.parseutils import parse_headers
                headers = parse_headers(item["Headers"])
            try:
                cookies = json.loads(item["Cookies"]) if not pd.isna(item["Cookies"]) else {}
            except:
                from lib.parseutils import parse_cookies
                cookies = parse_cookies(item["Cookies"])
            expect = json.loads(item["Expect"]) if not pd.isna(item["Expect"]) else {}
            status = item["Status"]
            resp = None
            if method == "GET":
                resp = requests.get(url, data=params, headers=headers, cookies=cookies)
            if method == "POST":
                resp = requests.post(url, json=params, headers=headers, cookies=cookies)
            if self.callback is not None:
                ret = self.callback(item, resp)
                results.append(ret)
                if ret["success"] is not None and ret["success"] is False:
                    # 错误
                    df_no.append(no)
                    df_url.append(url)
                    df_method.append(method)
                    df_params.append(params)
                    df_headers.append(headers)
                    df_cookies.append(cookies)
                    df_expect.append(expect)
                    df_status.append(status)
                    df_result.append(json.dumps(ret, ensure_ascii=False))
                else:
                    pass
        df = pd.DataFrame.from_dict({"No": df_no,
                                     "URL": df_url,
                                     "Method": df_method,
                                     "Params": df_params,
                                     "Headers": df_headers,
                                     "Cookies": df_cookies,
                                     "Expect": df_expect,
                                     "Status": df_status,
                                     "Result": df_result})
        df.to_excel("error.xlsx", index=None)
        return results


def request_callback(item, resp):
    print(item["URL"])
    print(resp.status_code)
    return dict(success=False, msg="呵呵呵")


def invoke_excel_requests(excel_path, callback):
    excel_requester = ExcelRequester(excel_path)
    if callback is not None:
        excel_requester.register_request_callback(callback)
    excel_requester.run()


if __name__ == '__main__':
    # excel_path = os.path.join(os.path.dirname(__file__), "test.xlsx")
    excel_path = "E:\\test\\test_xietong\data\\test1.xlsx"
    excel_requester = ExcelRequester(excel_path)
    excel_requester.register_request_callback(request_callback)
    excel_requester.run()
