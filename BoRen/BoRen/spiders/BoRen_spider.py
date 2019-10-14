# -*- coding: utf-8 -*-
import scrapy, json, time
from ..items import BorenItem


class BorenSpiderSpider(scrapy.Spider):
    name = 'BoRen_spider'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']
    base_url = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=5978&folded=0&page_size=20&sort=0&cursor={0}'

    def start_requests(self):
        for cursor in range(78091104618569, 78095392476036, 900):
            print('cursor为{0}'.format(cursor))
            yield scrapy.Request(url=self.base_url.format(cursor), callback=self.parse)

    def parse(self, response):
        item = BorenItem()
        data = json.loads(response.text)
        for one_item in data['result']['list']:
            item['uname'] = one_item['author']['uname']
            item['content'] = one_item['content']
            ctime = one_item['ctime']
            timeStamp = ctime
            timeArray = time.localtime(timeStamp)
            item['ctime'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            item['review_id'] = one_item['review_id']
            yield item
