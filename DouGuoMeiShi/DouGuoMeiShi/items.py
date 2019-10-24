# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouguomeishiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cover_imgUrl = scrapy.Field()  # 封面
    title = scrapy.Field()  # 标题
    author = scrapy.Field()  # 作者
    browse = scrapy.Field()  # 浏览量
    collect = scrapy.Field()  # 收藏量
    intro = scrapy.Field()  # 简介
    food_list = scrapy.Field()  # 食材清单
    cook_step = scrapy.Field()  # 烹饪步骤
