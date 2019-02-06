# -*- coding: utf-8 -*-
# @File  : zhihu_login_test4.py
# @Author: LaoJu
# @Date  : 2019/2/6
# @Desc  :

import requests

#初始化一个session
session = requests.session()

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

#step1 设置_xsrf，_zap，tgw_17
session.get(url="https://www.zhihu.com/signup",headers=HEADERS)

#step2 设置d_c0
session.post(url="https://www.zhihu.com/udid",headers=HEADERS)

#step3 设置capsion_ticket
session.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=en",headers=HEADERS)

#step4 获取token 拼接二维码图片请求链接
response = session.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode",headers=HEADERS)
token = response.json().get("token")
#step5 获取二维码图片
imageurl = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)

response = session.get(url=imageurl,headers=HEADERS)
if response.status_code == 200:
    with open("qr.jpg","wb") as file:
        file.write(response.content)
    print("[保存成功]")
else:
    print("[保存失败]")

#阻塞程序，留出时间扫码
input("随便输入后回车")

print(session.get("https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/scan_info".format(token), headers=HEADERS).status_code)

response = session.get("https://www.zhihu.com/people/edit",headers=HEADERS)

if response.status_code == 200:
    print("[登录成功]")
    print(response.text[:10000])


