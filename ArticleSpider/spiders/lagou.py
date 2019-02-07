# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS':{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'WEBTJ-ID=20190207150721-168c6c84a4920a-044ae5abe7815a-b781636-1327104-168c6c84a4d88; _ga=GA1.2.1470315449.1549523242; _gid=GA1.2.1655789576.1549523242; user_trace_token=20190207150722-03dd1dd9-2aa7-11e9-b8b0-5254005c3644; LGUID=20190207150722-03dd20b0-2aa7-11e9-b8b0-5254005c3644; JSESSIONID=ABAAABAAADEAAFI5FFF7090B4DDBE201F54421322146DB2; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549523242,1549523276; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=c90acb761f69438bb5a187b1baa1743e; _qddaz=QD.qdt64o.m91a2q.jruocyex; sajssdk_2015_cross_new_user=1; LGSID=20190207214548-ad19f177-2ade-11e9-8e07-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=http%3A%2F%2Fforbidden.lagou.com%2Fforbidden%2Ffbl.html%3Fip%3D171.91.107.29; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22%24device_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gat=1; hasDeliver=0; TG-TRACK-CODE=gongsi_banner; _putrc=9811B0A4E80F5AE2123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75914; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=57d159ca17f68192846c3c51ff5eace04a55c2bdeb62c6d274dc83c2f56a7958; LGRID=20190207221352-98f7bd66-2ae2-11e9-b8b1-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549548833',
            'Host': 'www.lagou.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
    }

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)),follow=True),
        # Rule(LinkExtractor(allow=("zhaopin/.*",)),callback='parse_job',follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)),follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=False),
    )

    # def parse_start_url(self, response):
    #     return []
    #
    # def process_results(self, response, results):
    #     return results

    def parse_job(self, response):
        # 解析拉勾网的职位
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
