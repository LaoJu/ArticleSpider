# -*- coding: utf-8 -*-
# @File  : selenium_spider.py
# @Author: LaoJu
# @Date  : 2019/2/13
# @Desc  :

from selenium import webdriver
from scrapy.selector import Selector

# 指定下载的driver的exe文件路径  注意路径斜杠方向
#
# browser.get("https://guang.taobao.com/detail/index.htm?spm=a21bo.2017.2001.6.5af911d9LEMIFC&uid=2634026521&sid=8093690604&scm=1007.15939.89001.100200300000000&pvid=04c1ecb8-8a9e-46ea-95df-e111b7d8450a&itemid=534180635565")
#
# print(browser.page_source)
#
# t_selector = Selector(text=browser.page_source)
# print(t_selector.css(".item-link .item-price::text").extract())
#
# browser.quit()


#知乎登录
# options = webdriver.ChromeOptions()
# options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument(
#     'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"')
#
#
# browser = webdriver.Chrome(executable_path="E:/chromedriver_win32/chromedriver.exe",chrome_options=options)
#
# browser.get("https://www.zhihu.com/signup?next=%2F")
#
# # 点击登录跳转页面至用户名密码登录
# browser.find_element_by_css_selector(".SignContainer-switch span").click()
# # 找到用户名填充
# browser.find_element_by_css_selector("input[name='username']").send_keys("XX")
# # 找到密码填充
# browser.find_element_by_css_selector("input[name='password']").send_keys("XX")
#
# # 点击登录
# browser.find_element_by_css_selector("button.SignFlow-submitButton").click()




#微博登陆

browser = webdriver.Chrome(executable_path="E:/chromedriver_win32/chromedriver.exe")
browser.get("https://weibo.com/")
import time
time.sleep(15)
browser.find_element_by_css_selector("#loginname").send_keys("15082408104")
browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("864196621chen")
browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn").click()