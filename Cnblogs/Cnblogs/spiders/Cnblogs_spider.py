# -*- coding: utf-8 -*-
import scrapy
from ..items import CnblogsItem


class CnblogsSpiderSpider(scrapy.Spider):
    name = 'Cnblogs_spider'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']
    base_url = 'https://www.cnblogs.com/cate/python#p{0}'

    def start_requests(self):
        for i in range(1, 2):
            yield scrapy.Request(url=self.base_url.format(i), callback=self.parse)

    def parse(self, response):
        item = CnblogsItem()
        divs = response.xpath("//div[@id='post_list']/div")
        for div in divs:
            item['title'] = div.xpath("./div[@class='post_item_body']/h3/a/text()").extract_first()
            item['article_url'] = div.xpath("./div[@class='post_item_body']/h3/a/@href").extract_first()
            item['author'] = div.xpath(
                "./div[@class='post_item_body']/div[@class='post_item_foot']/a/text()").extract_first()
            item['pub_date'] = ".".join(
                div.xpath("./div[@class='post_item_body']/div[@class='post_item_foot']/text()").re("发布于 (.*?) "))
            yield item
