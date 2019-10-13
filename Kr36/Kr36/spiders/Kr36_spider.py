# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import Kr36Item


class Kr36SpiderSpider(scrapy.Spider):
    name = 'Kr36_spider'
    allowed_domains = ['www.36kr.com']
    start_urls = ['https://www.36kr.com/']
    base_url = 'https://36kr.com/pp/api/search/entity-search'
    headers = {
        # 'cookie': 'acw_tc=2760821915709740004908150e5e1a542c803d369ff4378ea8cb085eb751e2; krnewsfrontss=f09709fa20577575b659fad918b5b87d; kr_stat_uuid=yC2pP26182899; Hm_lvt_713123c60a0e86982326bae1a51083e1=1570973998; sajssdk_2015_cross_new_user=1; Hm_lvt_1684191ccae0314c6254306a8333d090=1570973998; M-XSRF-TOKEN=dd21a021c378ecdf84276d25ac345b195afadf2cc5c05fc3a5572d56ec5d9307; device-uid=ba37b420-edbf-11e9-967f-6dcb6a70b567; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22yC2pP26182899%22%2C%22%24device_id%22%3A%2216dc558dcb980b-05d3c14d29a2ae-67e1b3f-2073600-16dc558dcba211%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2F36kr.com%2Finformation%2Ftechnology%22%2C%22%24latest_referrer_host%22%3A%2236kr.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2216dc558dcb980b-05d3c14d29a2ae-67e1b3f-2073600-16dc558dcba211%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1570975212; Hm_lpvt_1684191ccae0314c6254306a8333d090=1570975212; SERVERID=d36083915ff24d6bb8cb3b8490c52181|1570975215|1570974001',
        'content-type': 'application/json',
        'm-x-xsrf-token': 'dd21a021c378ecdf84276d25ac345b195afadf2cc5c05fc3a5572d56ec5d9307',
        'origin': 'https://36kr.com',
        'referer': 'https://36kr.com/search/articles/NBA',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    params = {"page": '1', "per_page": '40', "sort": "date", "entity_type": "post", "keyword": "NBA"}
    # 转换cookie为dict
    cookie = 'acw_tc=2760821915709740004908150e5e1a542c803d369ff4378ea8cb085eb751e2; krnewsfrontss=f09709fa20577575b659fad918b5b87d; kr_stat_uuid=yC2pP26182899; Hm_lvt_713123c60a0e86982326bae1a51083e1=1570973998; sajssdk_2015_cross_new_user=1; Hm_lvt_1684191ccae0314c6254306a8333d090=1570973998; M-XSRF-TOKEN=dd21a021c378ecdf84276d25ac345b195afadf2cc5c05fc3a5572d56ec5d9307; device-uid=ba37b420-edbf-11e9-967f-6dcb6a70b567; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22yC2pP26182899%22%2C%22%24device_id%22%3A%2216dc558dcb980b-05d3c14d29a2ae-67e1b3f-2073600-16dc558dcba211%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2F36kr.com%2Finformation%2Ftechnology%22%2C%22%24latest_referrer_host%22%3A%2236kr.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2216dc558dcb980b-05d3c14d29a2ae-67e1b3f-2073600-16dc558dcba211%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1570975212; Hm_lpvt_1684191ccae0314c6254306a8333d090=1570975212; SERVERID=d36083915ff24d6bb8cb3b8490c52181|1570975215|1570974001'
    cookie_list = cookie.split(";")
    cookies = {}
    for c in cookie_list:
        cookie_dict = c.split('=')
        cookies[cookie_dict[0]] = cookie_dict[1]

    def start_requests(self):
        # 以post方式访问，并传入参数self.params
        for page in range(1, 50):
            print('您正在访问第{0}页的数据'.format(page))
            yield scrapy.FormRequest(url=self.base_url, headers=self.headers, cookies=self.cookies,
                                     formdata={"page": str(page), "per_page": '40', "sort": "date",
                                               "entity_type": "post",
                                               "keyword": "NBA"})

    def parse(self, response):
        item = Kr36Item()
        data = json.loads(response.body_as_unicode())
        for one_item in data['data']['items']:
            item['app_views_count'] = one_item['app_views_count'] if "app_views_count" in one_item else 0
            item['mobile_views_count'] = one_item['mobile_views_count'] if "mobile_views_count" in one_item else 0
            item['views_count'] = one_item['views_count'] if "views_count" in one_item else 0
            item['column_name'] = one_item['column_name']
            item['title'] = one_item['title']
            item['published_at'] = one_item['published_at']
            item['is_free'] = one_item['is_free']
            item['username'] = one_item['user_name']
            item['content'] = one_item['highlight']['content']
            yield item
