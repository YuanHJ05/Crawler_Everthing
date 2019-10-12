# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SougouwxItem(scrapy.Item):
    title = scrapy.Field()  # 题目
    about = scrapy.Field()  # 简介
    author = scrapy.Field()  # 作者
    pub_date = scrapy.Field()  # 发表日期
    img_url = scrapy.Field()  # 缩略图片连接
    content_url = scrapy.Field()  # 文章内容
