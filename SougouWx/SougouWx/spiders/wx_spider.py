# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import SougouwxItem
import re


def cookie_to_dict(self, cookie):
    cookie_list = cookie.split(";")
    cookies = {}
    for c in cookie_list:
        cookie_dict = c.split('=')
        cookies[cookie_dict[0]] = cookie_dict[1]
    return cookies


class WxSpiderSpider(scrapy.Spider):
    name = 'wx_spider'
    # allowed_domains = ['weixin.sogou.com', 'http://img01.sogoucdn.com']
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/']
    base_url = 'https://weixin.sogou.com/weixin?query=nba&type=2&page=%s&ie=utf8'
    # 把request请求里面的cookie转换为字典模式，scrapy带cookie以这种参数为准
    cookie = "ABTEST=3|1570630045|v1; IPLOC=CN5000; SUID=2895507D721A910A000000005D9DE99D; SUID=2895507D2513910A000000005D9DE99D; weixinIndexVisited=1; SUV=007BAE1F7D5095285D9DE99F86C0C414; ppinf=5|1570630124|1571839724|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyMjpZdWFuJUU2JUI1JUE5JUU2JUExJTk0fGNydDoxMDoxNTcwNjMwMTI0fHJlZm5pY2s6MjI6WXVhbiVFNiVCNSVBOSVFNiVBMSU5NHx1c2VyaWQ6NDQ6bzl0Mmx1SWVyRlB3WERRMGh0U1BWcXRaUDlITUB3ZWl4aW4uc29odS5jb218; pprdig=qLnOzwQ63nOTT1M_g8K2PKFUUPlASSnZqin-m1MDTzyFzG5TZrynZu8975oHXShUNX5Ih4_eZeKC26gZeD9fDuZAuPRtxQtri3USUmg_v8TNXFpkJCK7dz-MUlEoXtID_B2S_EF_7TP3BydwzpafSIdboZh959---hE_NiKA1Ww; sgid=04-40856679-AV2d6ezWsEvRYKhSHC9TxA0; LCLKINT=9768; LSTMV=245%2C72; JSESSIONID=aaar4ZkJ7EYiC9Jdv_r1w; PHPSESSID=6c27fja3pcgjoih1catppr0ap1; SNUID=189B7E20989203391AE558539857E8EB; sct=3; ppmdig=1570858362000000459db64c750e54594cc2722887866b99"
    cookie_list = cookie.split(";")
    cookies = {}
    for c in cookie_list:
        cookie_dict = c.split('=')
        cookies[cookie_dict[0]] = cookie_dict[1]

    def start_requests(self):
        for i in range(1, 100):
            # print("正在爬取第{0}页的数据".format(i))
            yield scrapy.Request(url=self.base_url % i, callback=self.parse, cookies=self.cookies)

    def parse(self, response):

        item = SougouwxItem()
        lis = response.xpath("//div[@class='news-box']/ul[@class='news-list']/li")
        for li in lis:
            a_word = li.xpath("./div[@class='txt-box']/h3/a/text()").get()
            em_word = li.xpath("./div[@class='txt-box']/h3/a/em/text()").get()
            item['title'] = em_word + a_word  # 标题
            item['about'] = li.xpath("./div[@class='txt-box']/p/text()").getall()  # 简介
            item['author'] = li.xpath("./div[@class='txt-box']/div/a/text()").get()  # 作者
            time_stamp = li.xpath("./div[@class='txt-box']/div/span/script/text()").re(
                "[1-9][0-9]{4,}")  # 获取时间戳，是list类型
            time_stamp_str = ''.join(time_stamp)
            # 把时间戳转换为日期格式
            timeArray = time.localtime(int(time_stamp_str))
            item['pub_date'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 发表日期
            item['img_url'] = li.xpath("./div[@class='img-box']/a/img/@src").get()
            item['content_url'] = li.xpath("./div[@class='txt-box']/h3/a/@href").get()
            yield item
        # next_url = response.xpath("//div[@id='pagebar_container']/a[@id='sogou_next']/@href").get()
        # url = "https://weixin.sogou.com/weixin" + str(next_url)
        # print('下一页的url是', url)
        # if url:
        #     print('正在爬取下一页的数据')
        #     scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)
