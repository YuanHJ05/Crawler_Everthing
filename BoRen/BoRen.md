# 爬取B站，博人传的短评

## 疑难点
    - 短评是以ajax的方式传递，但是API后面分页参数无规律，这个有点棘手，API如下
 ```
https://bangumi.bilibili.com/review/web_api/short/list?media_id=5978&folded=0&page_size=20&sort=0&cursor=78091104618569
```
    - cursor的值，就是分页，但是无规律，我想的办法就是
```
    for cursor in range(78091104618569,78095392476036)
```
    -但是这样爬取，有个问题，就是会爬取很多重复的，效率不是很高，我想到的办法就是在pipeline里面根据item['review_id']进行去重