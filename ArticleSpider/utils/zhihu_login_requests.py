# -*- coding: utf-8 -*-
# @File  : zhihu_login_requests.py
# @Author: LaoJu
# @Date  : 2019/2/2
# @Desc  :

import requests
from http import cookiejar
from urllib import error
from PIL import Image

# 初始化一个session
session = requests.session()
token = ""
session.cookies = cookiejar.LWPCookieJar(filename="cookies.txt")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def init():
    global session
    # 尝试加载本地cookies
    try:
        session.cookies.load(ignore_discard=True)
        return True
    except FileNotFoundError:
        return False


def is_login():
    # 判断是否是登录状态

    # 请求一个登录状态能访问的页面
    response = session.get("https://www.zhihu.com/people/edit", headers=HEADERS, allow_redirects=False)
    if response.status_code == 200:
        print(response.text[:10000])
        return True
    else:
        return False


def request_qrcode():
    # 请求二维码

    try:
        # step1 设置_xsrf，_zap，tgw_17
        session.get(url="https://www.zhihu.com/signup", headers=HEADERS)

        # step2 设置d_c0
        session.post(url="https://www.zhihu.com/udid", headers=HEADERS)

        # step3 设置capsion_ticket
        session.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=en", headers=HEADERS)

        # step4 获取token 拼接二维码图片请求链接
        response = session.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode", headers=HEADERS)
        global token
        token = response.json().get("token")
        # step5 获取二维码图片
        imageurl = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)

        response = session.get(url=imageurl, headers=HEADERS)
        if response.status_code == 200:
            with open("qr.jpg", "wb") as file:
                file.write(response.content)
            print("[保存二维码成功]")
        else:
            print("[保存二维码失败]")

    except error.HTTPError:
        print("[请求二维码，HTTP错误]")


def show_qr():
    # 自动弹出二维码，扫码登录

    try:
        img = Image.open("qr.jpg")
    except FileNotFoundError:
        print("[没有图片文件]")
    except Exception:
        print("[打开二维码图片出错]")

    else:
        print("[请扫描二维码后关闭图片]")
        img.show()
        #阻塞程序，给扫码留时间
        input("随便输入后回车")
        # step6 获取Cookie中的z_c0
        response = session.get("https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/scan_info".format(token),
                               headers=HEADERS)


def zhihu_login():
    """
    登录逻辑控制
    :return:
    """

    # 如果有本地cookie，则使用
    if init():
        login_status = is_login()
        if login_status:
            print("[已登录]")
            return session
        else:
            print("[cookie过期，删除本地cookie后重新登录]")
            request_qrcode()
            show_qr()

            if is_login():
                print("[登录成功]")
                # 保存cookie到本地
                session.cookies.save()
                return session
            else:
                print("[登录失败，正在重新登录]")
                zhihu_login()

    else:
        request_qrcode()
        show_qr()

        if is_login():
            print("[登录成功]")
            # 保存cookie到本地
            session.cookies.save()
            return session
        else:
            print("[登录失败，正在重新登录]")
            zhihu_login()


if __name__ == "__main__":
    zhihu_login()
