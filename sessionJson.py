
# 封装了requests和beautifysoup
# 导入
from DrissionPage import SessionPage
import re
# 创建页面对象
page = SessionPage()
urls = 'https://falkor-cda.bastian.globo.com/tenants/g1/instances/5de8a589-29a6-4e3b-add5-8cb4040717f4/posts/page/{}'
# 访问网页
article_links = []
for i in range(1, 5):

    page.get(urls.format(i))
    data = page.json  # 将解析 JSON 数据的操作放在这里
    items = data.get('items', [])
    for item in items:
        content = item.get('content', {})
        url = content.get('url', '')
        if re.search(r'/noticia/', url):
            article_links.append(url)


print('article_links', len(article_links))
