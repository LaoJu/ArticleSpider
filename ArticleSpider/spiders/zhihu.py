# -*- coding: utf-8 -*-
import scrapy
import json
import re
import datetime
from PIL import Image
from urllib import parse
from scrapy.loader import ItemLoader
from ArticleSpider.items import ZhihuQuestionItem, zhihuAnswerItem

token = ""


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    start_answer_url = "https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit={1}&offset={2}&platform=desktop&sort_by=default"

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def parse(self, response):
        """
        1.提取html页面中所有url，跟踪这些url进一步爬取
        2.如果url格式 /question/xxx -->下载后直接解析字段
        :param response:
        :return:
        """

        # 提取所有url
        all_urls = response.css("a::attr(href)").extract()
        all_urls = [parse.urljoin(response.url, url) for url in all_urls]
        # 过滤无意义url
        # all_urls = filter(lambda x:True if x.startswith("https") else False,all_urls)
        for url in all_urls:
            # 提取问答的url
            match_obj = re.match("(.*zhihu.com/question/(\d+))(/|$).*", url)
            if match_obj:
                # 如果是问题页面，跳转到问题处理页面
                request_url = match_obj.group(1)
                print(request_url)
                yield scrapy.Request(request_url, headers=self.headers, callback=self.parse_question)
            else:
                pass
                # 不是问题页面，跟随此页面寻找其他url
                # yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse_question(self, response):

        match_obj = re.match("(.*zhihu.com/question/(\d+))(/|$).*", response.url)
        if match_obj:
            question_id = int(match_obj.group(2))

        item_loader = ItemLoader(item=ZhihuQuestionItem(), response=response)
        item_loader.add_css("title", "h1.QuestionHeader-title::text")
        item_loader.add_css("content", ".QuestionHeader-detail span::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("zhihu_id", question_id)
        item_loader.add_css("answer_num", ".List-headerText span::text")
        item_loader.add_css("comments_num", ".QuestionHeader-Comment button::text")
        item_loader.add_css("watch_user_num", ".NumberBoard-itemValue::text")
        item_loader.add_css("topics", ".QuestionHeader-topics .Popover div::text")

        question_item = item_loader.load_item()
        print("sth")
        #分析回答 最多只能一次提取20条
        # answer_num = int(question_item.get("answer_num"))
        yield scrapy.Request(self.start_answer_url.format(question_id, 20, 0), headers=self.headers,
                             callback=self.parse_answer)
        #yield 出去的item 被路由到pipline里面
        # yield question_item

    def parse_answer(self, response):
        #解析回答
        ans_json = json.load(response.text)
        is_end = ans_json["paging"]["is_end"]
        next_url = ans_json["paging"]["next"]

        #解析回答中的字段 一次请求返回多条回答信息
        for answer in ans_json["data"]:
            answer_item = zhihuAnswerItem()
            answer_item["zhihu_id"] = answer["id"]
            answer_item["url"] = answer["url"]
            answer_item["question_id"] = answer["question"]["id"]
            #匿名回答没有author_id
            answer_item["author_id"] = answer["author"]["id"] if "id" in answer["author"] else None
            answer_item["content"] = answer["content"] if "content" in answer else None
            answer_item["praise_num"] = answer["voteup_count"]
            answer_item["comments_num"] = answer["comment_count"]
            answer_item["create_time"] = answer["created_time"]
            answer_item["update_time"] = answer["updated_time"]
            answer_item["crawl_time"] = datetime.datetime.now()

            yield answer_item

        if not is_end:
            yield scrapy.Request(next_url,headers=self.headers,callback=self.parse_answer)

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/signup', headers=self.headers, callback=self.step1)]

    def step1(self, response):
        url = "https://www.zhihu.com/udid"
        yield scrapy.Request(url, method="POST", headers=self.headers, callback=self.step2)

    def step2(self, response):
        url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
        yield scrapy.Request(url, headers=self.headers, callback=self.step3)

    def step3(self, response):
        url = "https://www.zhihu.com/api/v3/account/api/login/qrcode"
        return [scrapy.Request(url, method="POST", headers=self.headers, callback=self.step4)]

    def step4(self, response):
        global token
        text_json = json.loads(response.text)
        token = text_json["token"]
        imageurl = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)
        yield scrapy.Request(imageurl, headers=self.headers, callback=self.step5)

    def step5(self, response):
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
                yield scrapy.Request(url, headers=self.headers, callback=self.step6)
        else:
            print("[保存二维码失败]")

    def step6(self, response):
        url = "https://www.zhihu.com/"
        yield scrapy.Request(url, headers=self.headers, callback=self.check_login)

    def check_login(self, response):
        # print(response.text)
        # TODO check_login逻辑未完成
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, headers=self.headers)
