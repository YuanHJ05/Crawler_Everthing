# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Kr36Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_views_count = scrapy.Field()  # APP观看数量
    mobile_views_count = scrapy.Field()  # 移动端观看数量
    views_count = scrapy.Field()  # PC观看数量
    column_name = scrapy.Field()  # 类别
    title = scrapy.Field()  # 标题
    published_at = scrapy.Field()  # 发布时间
    is_free = scrapy.Field()  # 是否免费
    username = scrapy.Field()
    content=scrapy.Field()

