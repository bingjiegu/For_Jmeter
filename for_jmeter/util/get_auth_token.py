# coding:utf-8
import requests
from util.config import MY_LOGIN_INFO, MY_LOGIN_INFO_dam
from util.format_res import dict_res


# 获取登录后返回的X-AUTH-TOKEN
def get_auth_token(HOST):
    if '57' in HOST:
        res = requests.post(url=MY_LOGIN_INFO_dam["URL"], headers=MY_LOGIN_INFO_dam["HEADERS"], data=MY_LOGIN_INFO_dam["DATA"])
        dict_headers = dict(res.headers)
        token = dict_headers['X-AUTH-TOKEN']
        # print(token)
        return token
    else:
        res = requests.post(url=MY_LOGIN_INFO["URL"], headers=MY_LOGIN_INFO["HEADERS"], data=MY_LOGIN_INFO["DATA"])
        # print(res.url)
        dict_headers = dict_res(res.text)
        # print(dict_headers)
        token = dict_headers['content']["accessToken"]
        # print(token)
        return 'Bearer ' + token


# 组装headers， 接口请求时调用
def get_headers(HOST):
    x_auth_token = get_auth_token(HOST)
    headers = {'Content-Type': 'application/json', "X-AUTH-TOKEN": x_auth_token, "Accept": "application/json"}
    # print(headers)
    return headers


#
# from util.get_host import HOST#
# print(get_auth_token(HOST))