from mitmproxy import ctx
import json
import pymongo


def response(flow):
    # 配置mongodb,要放在类里面，不然会报错
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = client['igetget']
    collection = db['books']
    url = "https://entree.igetget.com/ebook2/v1/ebook/list"
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title': book.get('operating_title'),
                'cover': book.get('cover'),
                'summary': book.get('other_share_summary'),
                'price': book.get('price')
            }
            ctx.log.info(str(data))
            collection.insert(data)

# https://entree.igetget.com/ebook2/v1/ebook/list
