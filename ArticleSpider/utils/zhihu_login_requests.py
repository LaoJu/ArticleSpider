# -*- coding: utf-8 -*-
# @File  : zhihu_login_requests.py
# @Author: LaoJu
# @Date  : 2019/2/2
# @Desc  :

import requests
import http.cookiejar as cookielib
import re

def get_xsrf():
    response = requests.get("https://www.zhihu.com")
    print(response.text)
    return ""


def zhihu_login(account,password):
    #知乎登录
    if re.match("^1\d{10}",account):
       print("手机号登录")
       post_url = "https://www.zhihu.com/login/phone_num"
       post_data = {
           "_xsrf":"",
           "phone_num":account,
           "password":password
       }