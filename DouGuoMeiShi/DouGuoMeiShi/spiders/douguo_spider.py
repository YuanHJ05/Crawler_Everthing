# -*- coding: utf-8 -*-
import scrapy
from ..items import DouguomeishiItem


class DouguoSpiderSpider(scrapy.Spider):
    name = 'douguo_spider'
    allowed_domains = ['www.douguo.com', 'cp1.douguo.com']
    start_urls = ['http://www.douguo.com/']
    base_url = 'https://www.douguo.com/caipu/0'

    def start_requests(self):
        yield scrapy.Request(url=self.base_url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath("//ul[@id='jxlist']/li")
        for li in lis:
            cover_imgUrl = li.xpath("./a/img/@src").extract_first()
            title = li.xpath("./div[@class='relative']/a[1]/text()").extract_first()
            author = li.xpath("./div[@class='relative']/a[@class='author text-lips']/text()").extract_first()
            detail_url = li.xpath("./a/@href").get()
            url = response.urljoin(detail_url)
            yield scrapy.Request(url=url, meta={'cover_imgUrl': cover_imgUrl, "title": title, "author": author},
                                 callback=self.parse_detail)

        # next_url = response.xpath("//a[@class='anext']/@href").get()
        # if next_url:
        #     yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item = DouguomeishiItem()
        item['cover_imgUrl'] = response.meta['cover_imgUrl']
        item['title'] = response.meta['title']
        item['author'] = response.meta['author']
        item['browse'] = response.xpath("//div[@class='vcnum relative']/span/text()").get()
        item['collect'] = response.xpath("//div[@class='vcnum relative']/span[@class='collectnum']/text()").get()
        item['intro'] = response.xpath("//p[@class='intro']/text()").get()
        food_list_tr = response.xpath("//table/tbody/tr")
        print(food_list_tr)
        food_list = []
        item['food_list'] = food_list
        for tr in food_list_tr:
            food_lis = tr.xpath("./td[1]/span/text()").extract()
            # food_list.append(food_lis)
            # print(food_lis)
        yield item
