# -*- coding: utf-8 -*-
import scrapy, re
from ..items import KuanItem


class KuanSpiderSpider(scrapy.Spider):
    name = 'KuAn_spider'
    allowed_domains = ['www.coolapk.com']
    start_urls = ['http://www.coolapk.com/']
    base_url = 'https://www.coolapk.com/apk?p={0}'

    def start_requests(self):
        for i in range(1, 302):
            print('正在爬取第{0}页数据'.format(i))
            yield scrapy.Request(url=self.base_url.format(i))

    def parse(self, response):
        a_list = response.xpath("//div[@class='app_left_list']/a")
        for one_item in a_list:
            app_url = one_item.xpath("./@href").extract_first()
            real_url = 'https://www.coolapk.com' + str(app_url)
            yield scrapy.Request(url=real_url, callback=self.parse_app)

    def parse_app(self, response):
        item = KuanItem()
        app_name = response.xpath(
            "//div[@class='apk_topba_appinfo']/div[@class='apk_topbar_mss']/p[@class='detail_app_title']/text()").extract_first()
        app_infos = response.xpath(
            "//div[@class='apk_topba_appinfo']/div[@class='apk_topbar_mss']/p[@class='apk_topba_message']/text()").extract_first()
        app_info_list = app_infos.replace("\n", "").strip().split('/')
        app_size = app_info_list[0]
        app_down_num = app_info_list[1]
        app_follow = app_info_list[2]
        app_review = app_info_list[3].strip()
        app_rank = response.xpath("//div[@class='apk_rank']/p[@class='rank_num']/text()").extract_first()
        category = response.xpath("//span[@class='apk_left_span2']/text()").extract()
        app_detail = response.xpath(
            "//div[@class='apk_left_title']/p[@class='apk_left_title_info']/text()").extract()
        app_deve_name = app_detail[-1].split("：")[-1]
        yield KuanItem(app_name=app_name, app_rank=app_rank, category=category, app_size=app_size,
                       app_down_num=app_down_num,
                       app_follow=app_follow, app_review=app_review, app_deve_name=app_deve_name)
