# -*- coding: utf-8 -*-
import scrapy
from ..items import CnblogsItem


class CnblogsSpiderSpider(scrapy.Spider):
    name = 'Cnblogs_spider'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/cate/python#p1']

    # base_url = 'https://www.cnblogs.com/cate/python#p{0}'

    # def start_requests(self):
    #     for i in range(1, 201):
    #         print(self.base_url.format(i))
    #         yield scrapy.Request(url=self.base_url.format(i), callback=self.parse)

    def parse(self, response):
        print(response.url)
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

        next_word = response.xpath("//div[@id='paging_block']/div[@class='pager']/a[last()]/text()").get()
        if next_word == "Next >":
            next_url = response.xpath("//div[@id='paging_block']/div[@class='pager']/a[last()]/@href").get()
            next_url = "https://www.cnblogs.com" + str(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)
