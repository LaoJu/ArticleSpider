# -*- coding: utf-8 -*-
# @File  : zhihu_login_test2.py
# @Author: LaoJu
# @Date  : 2019/2/6
# @Desc  :

import requests

headers = {
    # 'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'cache-control':'no-cache',
    # 'content-length':'0',
    'cookie':'tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _zap=cf62835e-20ce-462f-ab43-d6ceeb660b07; _xsrf=753c21ee-4c0b-4e2b-992a-57374fa65e97',
    # 'origin':'https://www.zhihu.com',
    # 'pragma':'no-cache',
    # 'referer':'https://www.zhihu.com/signup?next=%2F',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'x-xsrftoken':'753c21ee-4c0b-4e2b-992a-57374fa65e97',
}

response = requests.post(url="https://www.zhihu.com/udid",headers=headers)

print(response.status_code)
print(response.text)