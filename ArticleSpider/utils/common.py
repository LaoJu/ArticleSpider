# -*- coding: utf-8 -*-
# @File  : common.py
# @Author: LaoJu
# @Date  : 2019/2/1
# @Desc  :

import hashlib

def get_md5(url):
    #先对参数进行检查，py3字符串默认unicode
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print(get_md5("https://stackoverflow.com/".encode("utf-8")))