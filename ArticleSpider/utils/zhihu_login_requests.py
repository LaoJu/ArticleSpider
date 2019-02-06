# -*- coding: utf-8 -*-
# @File  : zhihu_login_requests.py
# @Author: LaoJu
# @Date  : 2019/2/2
# @Desc  :

import requests
import http.cookiejar as cookielib
import re

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referer":"https://zhihu.com",
    "User-Agent":agent
}
def get_xsrf():
    response = requests.get("https://www.zhihu.com",headers = header)
    print(response.text)
    return ""


def zhihu_login(account,password):
    #知乎登录
    if re.match("^1\d{10}",account):
       # print("手机号登录")
       post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
       post_data = {
           "_xsrf":get_xsrf(),
           "phone_num":account,
           "password":password
       }

