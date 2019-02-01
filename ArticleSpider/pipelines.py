# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

#保存json文件
class Json

#定制处理封面图的pipeline
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok,value in results:
            #提取图片下载后在本地的路径
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path

        return item
        pass