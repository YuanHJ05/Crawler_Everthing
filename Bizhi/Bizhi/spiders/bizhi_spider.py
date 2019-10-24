# -*- coding: utf-8 -*-
import scrapy
from ..items import BizhiItem


class BizhiSpiderSpider(scrapy.Spider):
    name = 'bizhi_spider'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/']

    def parse(self, response):
        sels = response.xpath("//div[@class='classify clearfix']/a")
        for url in sels:
            category_url = url.xpath("./@href").extract_first()
            category = url.xpath("./text()").extract_first()
            real_url = response.urljoin(category_url)
            # print(real_url, title)
            yield scrapy.Request(url=real_url, callback=self.parse_img, meta={'category': category})

    def parse_img(self, response):
        category = response.meta['category']
        sels = response.xpath("//div[@class='slist']/ul/li")
        for li in sels:
            title = li.xpath("./a/b/text()").get()
            url = response.urljoin(li.xpath("./a/@href").get())
            yield scrapy.Request(url=url, callback=self.parse_download, meta={'title': title, 'category': category})
        next_word = response.xpath("//div[@class='page']/a[text()='下一页']/text()").get()
        print("名称：", next_word)
        if next_word == '下一页':
            next_url = response.xpath("//div[@class='page']/a[text()='下一页']/@href").get()
            next_url = response.urljoin(next_url)
            print("地址：", next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_img, meta={'category': category})

    def parse_download(self, response):
        item = BizhiItem()
        item['title'] = response.meta['title']
        item['category'] = response.meta['category']
        item['url'] = response.urljoin(response.xpath("//a[@id='img']/img/@src").get())
        yield item
