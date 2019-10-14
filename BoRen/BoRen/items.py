# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BorenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uname = scrapy.Field()  # 用户名
    content = scrapy.Field()  # 发表内容
    ctime = scrapy.Field()  # 评论时间
    review_id = scrapy.Field()  # 评论ID
