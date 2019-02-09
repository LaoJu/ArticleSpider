# -*- coding: utf-8 -*-
import scrapy
import random
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ArticleSpider.items import LagouJobItemLoader,LagouJobItem
from ArticleSpider.utils.common import get_md5
from ArticleSpider.settings import user_agent_list


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    #获取随机user_agent
    user_agent_index = random.randint(0,len(user_agent_list)-1)
    random_agent = user_agent_list[user_agent_index]

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.8',
            # 'Connection': 'keep-alive',
            # 'Cookie': '_ga=GA1.2.1470315449.1549523242; _gid=GA1.2.1655789576.1549523242; user_trace_token=20190207150722-03dd1dd9-2aa7-11e9-b8b0-5254005c3644; LGUID=20190207150722-03dd20b0-2aa7-11e9-b8b0-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; _qddaz=QD.qdt64o.m91a2q.jruocyex; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22%24device_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; WEBTJ-ID=20190208174327-168cc7d923f3b8-0ef9ff8d519f05-b781636-1327104-168cc7d9240354; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549523242,1549523276,1549619008; _putrc=9811B0A4E80F5AE2123F89F2B170EADC; JSESSIONID=ABAAABAAAFCAAEG5246179A0A3D2DDA35613AA55A25E293; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75914; SEARCH_ID=48592ac94e1147dfabe3e7841edf037e; X_MIDDLE_TOKEN=1ba8b660c57507c6115ba534f2de1707; LGSID=20190208214820-31f2bb3d-2ba8-11e9-9107-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3526873.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; gate_login_token=044b8ff66d6432c822d9f66663fcf6e75dce887e61687b18ef5f3f79c953d3a0; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549634809; LGRID=20190208220648-c66781d0-2baa-11e9-9108-525400f775ce; TG-TRACK-CODE=index_navigation',
            # 'Host': 'www.lagou.com',
            # 'Origin': 'https://www.lagou.com',
            # 'Referer': 'https://www.lagou.com/',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.1470315449.1549523242; _gid=GA1.2.1655789576.1549523242; user_trace_token=20190207150722-03dd1dd9-2aa7-11e9-b8b0-5254005c3644; LGUID=20190207150722-03dd20b0-2aa7-11e9-b8b0-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; _qddaz=QD.qdt64o.m91a2q.jruocyex; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22%24device_id%22%3A%22168c835151378a-07bb516ba4256c-b781636-1327104-168c835151466f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; SEARCH_ID=da983bd053724e45a0d972876eee6181; WEBTJ-ID=20190209141838-168d0e86a373cb-0dbce1e3149459-b781636-1327104-168d0e86a392c9; _gat=1; LGSID=20190209141838-89be2bf5-2c32-11e9-92e8-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tn%3D98012088_5_dg%26ch%3D11; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549523242,1549523276,1549619008,1549693119; _putrc=9811B0A4E80F5AE2123F89F2B170EADC; JSESSIONID=ABAAABAAAGGABCB6B707DB22D138100B20EC2799648F26C; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75914; gate_login_token=0c3c98f68281c4c56f61d47fca91bf93e74c7c5cb172f04dc3659351b2eaef4c; LGRID=20190209141842-8c40b1bf-2c32-11e9-92e8-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549693124',
            'Host': 'www.lagou.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.lagou.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'User-Agent': random_agent,




        }
    }

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
        # Rule(LinkExtractor(allow=("zhaopin/.*",)),callback='parse_job',follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    # def parse_start_url(self, response):
    #     return []
    #
    # def process_results(self, response, results):
    #     return results

    def parse_job(self, response):
        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(),response=response)
        item_loader.add_css("title",".job-name::attr(title)")
        item_loader.add_value("url",response.url)
        item_loader.add_value("url_object_id",get_md5(response.url))
        item_loader.add_css("salary",".job_request .salary::text")

        #灵活变换方法 span处的数组下标从1开始
        item_loader.add_xpath("job_city","//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years","//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need","//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type","//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags",".position-label li::text")
        item_loader.add_css("publish_time",".publish_time::text")
        item_loader.add_css("job_advantage",".job-advantage p::text")
        item_loader.add_css("job_desc",".job_bt div")
        item_loader.add_css("job_addr",".work_addr")
        # class用. id用#
        item_loader.add_css("company_name","#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url","#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time",datetime.now())

        job_item = item_loader.load_item()

        return job_item
