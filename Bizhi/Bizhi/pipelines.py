# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#
# class BizhiPipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


# 保存图片到本地
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 从item中获取要下载的图片的url，根据url构造Request()对象，并返回该对象
        yield Request(item['url'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 从item中获取要下载的图片的url，根据url构造Request()对象，并返回该对象
        item = request.meta['item']
        # 分类的名称
        category = item['category']
        # 图片的文件名
        img_name = item['title']
        # 构造目录文件
        path = category + '/' + img_name + '.jpg'
        return path

    def item_completed(self, results, item, info):
        images_paths = [x['path'] for ok, x in results if ok]
        if not images_paths:
            return DropItem('图片下载失败')
        return item
