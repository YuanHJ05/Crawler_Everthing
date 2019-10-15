# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_name = scrapy.Field()  # 应用名称
    app_rank = scrapy.Field()
    category = scrapy.Field()
    app_size = scrapy.Field()
    app_down_num = scrapy.Field()
    app_follow = scrapy.Field()
    app_review = scrapy.Field()
    app_deve_name = scrapy.Field()
