from behave import *
from lib.excelRequester import invoke_excel_requests
from lib.dbutils import invoke_sql
import os
import requests
import json
from lib.generalMethod import get_excle

@Then("拆分成功测试用例 {testId} and {noticeId} and {invoiceType} and {noticeOpenToken} and {count}")
def step_impl(context,testId,noticeId,invoiceType,noticeOpenToken,count):
    print("执行到第",context.testId)
    filename = "E:\\test\\test_xietong\data\\test2.xlsx"
    #获取开票token
    urlT="https://colla.zhonglr.com/collaboration/backend/outputNotice/openToken.json"
    cookieBef="_9755xjdesxxd_=32;zds-session=812629e6-fdc4-407b-8d20-3d9b9bcde7c9;ARToken.NoticeOpenToken="
    noticeOpenToken=context.noticeOpenToken
    cookieAft=";gdxidpyhxdE=%2B54MTcQ4eienOI61ZNrODCtazxCoQZHS7r5IQ%2FuWb5nbSZfK4%2BURLkzxR1E0M1G5yAUpsjh7Oi19zdvBBOni7fCVybQn9C0n%2Bua9xT6WO6%5CqaWqIM8z74Q95hXsvnWe1Cko%5CC%2FeBXbKOcTzj7G7PusvoKxkZz%5C%2F3xrvWoH1YS%2B2EKhhi%3A1566177766628"
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
    noticeId=context.noticeId
    invoiceType=get_excle(0,"invoiceType",filename)
    params={"noticeId":noticeId,"invoiceType":invoiceType}
    if respT.json()["success"]==True:
        #调用开票接口
        print("执行到调用开票接口了。。。")
        resp = requests.post(url, json=params, headers=headers)
        print("调用开票接口响应结果",resp.json())
        #校验响应结果和数据库结果
        data=resp.json()["data"]
        count=get_excle(0,"count",filename)
        assert data == count
        if resp.json()["success"]==True:
            sql = "SELECT * FROM select invoice_notice_status from op_notice  where id= %s" %noticeId
            results = invoke_sql(sql)
    else:
        return dict(success=False, msg="请求开票token失败！")


