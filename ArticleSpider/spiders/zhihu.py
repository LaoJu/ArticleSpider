# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
import json
import requests
from http import cookiejar
from ArticleSpider.utils.zhihu_login_requests import zhihu_login

token = ""
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def parse(self, response):
        print("sth")
        print(response.text[:10000])
        
        pass

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/signup', headers=self.headers, callback=self.step1)]

    def step1(self, response):
        url = "https://www.zhihu.com/udid"
        yield scrapy.Request(url,method="POST",headers=self.headers,callback=self.step2)

    def step2(self,response):
        url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
        yield scrapy.Request(url,headers=self.headers,callback=self.step3)

    def step3(self,response):
        url = "https://www.zhihu.com/api/v3/account/api/login/qrcode"
        return [scrapy.Request(url,method="POST",headers=self.headers,callback=self.step4)]

    def step4(self,response):
        global token
        text_json = json.loads(response.text)
        token = text_json["token"]
        imageurl = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)
        yield scrapy.Request(imageurl,headers=self.headers,callback=self.step5)

    def step5(self,response):
        print(type(response))
        if response.status == 200:
            with open("new_qr.jpg", "wb") as file:
                file.write(response.body)
            print("[保存二维码成功]")
            try:
                img = Image.open("new_qr.jpg")
            except FileNotFoundError:
                print("[没有图片文件]")
            except Exception:
                print("[打开二维码图片出错]")

            else:
                print("[请扫描二维码后关闭图片]")
                img.show()
                # 阻塞程序，给扫码留时间
                input("随便输入后回车")
                # step6 获取Cookie中的z_c0
                url = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/scan_info".format(token)
                yield scrapy.Request(url,headers=self.headers,callback=self.step6)
        else:
            print("[保存二维码失败]")


    def step6(self,response):
        url = "https://www.zhihu.com/"
        yield scrapy.Request(url,headers=self.headers,callback=self.check_login)

    def check_login(self,response):
        # print(response.text)
        #TODO check_login逻辑未完成
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, headers=self.headers)


