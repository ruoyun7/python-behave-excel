import requests
from http.cookies import SimpleCookie

params = {"parentId": 361544148074496, "code": "123123", "name": "123123", "enterpriseId": 336362349821952,
          "isLeaf": True}

url = "https://colla.zhonglr.com/collaboration/backend/invoiceGoodsType/create.json"
Referer = "https://colla.zhonglr.com/collaboration-business/index.html"
headers = {"Referer": Referer}
cookies = SimpleCookie(
    "_9755xjdesxxd_=32; zds-session=30885f19-3874-4e71-b68b-07d5c1c0ede1; gdxidpyhxdE=fUoqfCL3i%5CAHIYEapnWUl0BQU%5CKiWR6lLD600IobLpjpZAr%2F5Vwp4%2FPpHI%5ChXAE%2FeQHUVGCjSdhrOOYpL5yqEKACwfgTzSgv4mpcnV27r0oL%2BC0gvwZmbJg71ufOyXVgM%5C%2BzerYJTSK1k6r85GqoVQRtp0gc%2Ft7Iud%2FJ13TcRhQe36jV%3A1565665716330")
cookies = {v.key: v.value for k, v in cookies.items()}
resp = requests.post(url, json=params, cookies=cookies, headers=headers)
print(resp.content.decode())
