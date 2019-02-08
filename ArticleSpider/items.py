# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
from settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value + "-chj"


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


class ArticleItemLoader(ItemLoader):
    # 自定义ItemLoader
    # 设置默认output_processor
    default_output_processor = TakeFirst()


def remove_comment_tags(value):
    # 去掉tags中的“评论”
    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    # 不做任何操作返回，使单个值变成list
    return value


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        # input_processor=MapCompose(lambda x: x + "-jobbole", add_jobbole)
    )
    create_date = scrapy.Field(
        # 对string类型的时间做预处理变成date
        input_processor=MapCompose(date_convert),  # create_date作为参数传入date_convert()方法
        output_processor=TakeFirst()
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()  # url是变长的，做md5处理变成一样长度
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )  # 封面图url
    front_image_path = scrapy.Field()  # 封面图下载到本地路径
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
                    insert into jobbole_article(title, url, create_date, fav_nums)
                    VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
                """
        params = (self["title"], self["url"], self["create_date"], self["fav_nums"])

        return insert_sql, params


def remove_splash(value):
    # 去掉工作城市的斜线
    return value.replace("/", "")

def handle_publish_date(value):
    #去除发布时间中多余字段
    return value.split(" ")[0]

def handle_jobaddr(value):
    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list if item.strip()!="查看地图"]
    return "".join(addr_list)


class LagouJobItemLoader(ItemLoader):
    # 自定义拉勾网job的Itemloader
    pass



class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    publish_time = scrapy.Field(
        input_processor=MapCompose(handle_publish_date),
    )
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(
        input_processor=Join(",")
    )
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
            job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url,
            tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
        """
        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
            self["work_years"], self["degree_need"], self["job_type"],
            self["publish_time"], self["job_advantage"], self["job_desc"],
            self["job_addr"], self["company_name"], self["company_url"],
            self["job_addr"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
        )

        return insert_sql, params
