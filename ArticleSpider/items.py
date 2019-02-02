# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst,Join


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
    #去掉tags中的“评论”
    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    #不做任何操作返回，使单个值变成list
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
