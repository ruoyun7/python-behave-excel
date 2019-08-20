s = """
Host: colla.zhonglr.com
Connection: keep-alive
Content-Length: 52
Accept: application/json, text/plain, */*
Origin: https://colla.zhonglr.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Content-Type: application/json; charset=UTF-8
Referer: https://colla.zhonglr.com/collaboration-business/index.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _9755xjdesxxd_=32; zds-session=45ee998f-a3b1-4888-a0dc-21f77b30e5cc; gdxidpyhxdE=tgoyJlsC4Te5TiPBzOuq%5CAhDtjK%5C1G0n58ZWWzs%2BT1eLI8aTwfWNWmse0pWcn2x6qIKzht6OUb8XToJftNI3rYHgal8fv8lBVRQtjTCo3dW0%2Bv0wsCmrKACl%2FmvyJ43ozjbxvcoEYHQEETARlAlkITkGvylsGcCjcbQ8rhHbN15BHuLr%3A1565857675753; ARToken.NoticeOpenToken=bc8d64b9-162b-41cd-adb1-39515d907b16"""



s = s.strip().split('\n')
s = {x.split(':')[0].strip() : x.split(':')[1].strip() for x in s}
print(type(s))
print(s)