# -*- coding: utf-8 -*-
# @File  : common.py
# @Author: LaoJu
# @Date  : 2019/2/1
# @Desc  :

import hashlib
import re


def get_md5(url):
    # 先对参数进行检查，py3字符串默认unicode
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def extract_num(value):
    # 字符串中提取数字
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


if __name__ == "__main__":
    print(get_md5("https://stackoverflow.com/".encode("utf-8")))
