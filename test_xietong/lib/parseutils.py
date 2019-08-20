import json


def parse_headers(headers):
    """
    将chrome复制出来的headers转成dict
    :param headers:
    :return:
    """
    if headers is not None:
        headers = headers.strip().split('\n')
        headers = {x.split(':')[0].strip(): x.split(':')[1].strip() for x in headers}
        return headers
    return {}

def parse_cookies(cookies):
    """
    将chrome中的cookies转成dict
    :param cookies:
    :return:
    """
    if cookies is not  None:
        from http.cookies import SimpleCookie
        cookies = SimpleCookie(cookies)
        cookies = {v.key: v.value for k, v in cookies.items()}
    return {}