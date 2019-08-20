from behave import *
from lib.excelRequester import invoke_excel_requests
from lib.dbutils import *
import os
import requests
import json
from lib.generalMethod import *

@When("初始化数据")
def step_imp(context):
    print("开始执行初始化sql")
    invoke_sql_file(["E:\\test\\test_xietong\data\sql.txt"])
    print("执行初始化sql结束！")

@Then("第{no}行用例")
def step_impl(context,no):
    context.no=no
    num=int(context.no)
    filename="E:\\test\\test_xietong\data\\test2.xlsx"
    print("\n执行到第",get_excle(num,"testId",filename),"条用例")
    #获取开票token
    urlT="https://colla.zhonglr.com/collaboration/backend/outputNotice/openToken.json"
    cookieBef=get_excle(num,"cookieBef",filename)
    noticeOpenToken=get_excle(num,"noticeOpenToken",filename)
    cookieAft=get_excle(num,"cookieAft",filename)
    cookieT=cookieBef+noticeOpenToken+cookieAft
    headersT={"Host": "colla.zhonglr.com","Referer": "https://colla.zhonglr.com/collaboration-business/index.html","Cookie":cookieT}
    #调用获取开票token接口
    respT = requests.get(urlT, data={}, headers=headersT)
    print("\n获取开票token响应结果",respT.json())
    noticeOpenTokenR=respT.cookies['ARToken.NoticeOpenToken']
    #开票接口-------
    cookie=cookieBef+noticeOpenTokenR+cookieAft
    headers={"Host": "colla.zhonglr.com","Referer": "https://colla.zhonglr.com/collaboration-business/index.html","Cookie":cookie}
    url="https://colla.zhonglr.com/collaboration/backend/outputNotice/open.json"
    noticeId=get_excle(num,"noticeId",filename)
    invoiceType=get_excle(num,"invoice_type",filename)
    params={"noticeId":noticeId,"invoiceType":invoiceType}
    if respT.json()["success"]==True:
        #调用开票接口
        print("执行到调用开票接口了。。。")
        resp = requests.post(url, json=params, headers=headers)
        print("调用开票接口响应结果",resp.json())
        #校验响应结果和数据库结果
        data=resp.json()["data"]
        count=get_excle(num,"count",filename)
        assert data == count
        if resp.json()["success"]==True:
            sql = "SELECT * FROM  op_notice  where id= '%s'" %noticeId
            results = invoke_sql(sql)
            for result in results:
                assert result['open_person_id'] == get_excle(num,"open_person_id",filename)
                assert result['open_person_name'] == get_excle(num,"open_person_name",filename)
                assert result['invoice_end'] is  None
                assert result['invoice_notice_status'] == get_excle(num,"invoice_notice_status",filename)
                assert result['invoice_start'] is  None
                assert result['open_person_date'] is not None
                assert result['invoice_type'] == get_excle(num,"invoice_type",filename)
                # assert result['payee'] == get_excle(num,"payee",filename)
                # assert result['remark'] == get_excle(num,"remark",filename)
                # assert result['review_person'] == get_excle(num,"review_person",filename)

    else:
        return dict(success=False, msg="请求开票token失败！")




