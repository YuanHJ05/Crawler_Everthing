# SougouWx-爬取搜狗微信公众号文章

## 创建工程

### 安装执行环境
```
pipenv install 
```

### 创建scrapy工程

```
scrapy startproject SougouWx
scrapy genspider wx_spider weixin.sogou.com
```

### 修改settings.py

```
ROBOTSTXT_OBEY = False
```

### middlewares.py 

添加随机请求头,和阿布云动态转发
设置好了后，在settings.py里面开启中间件


###设置item

```
class SougouwxItem(scrapy.Item):
    title = scrapy.Field()  # 题目
    about = scrapy.Field()  # 简介
    author = scrapy.Field()  # 作者
    pub_date = scrapy.Field()  # 发表日期
    img_url = scrapy.Field()  # 缩略图片连接
    content_url = scrapy.Field()  # 文章内容
```

###写spider程序

###存储到mongodb


###疑难点

1、每次访问要用不同的IP，不然会被禁止访问
2、不能访问文章的外链，一点击就会出现anitspider页面
3、访问过多，还是存在被封情况