# 封装了requests和beautifysoup
# 导入
from DrissionPage import SessionPage
# 创建页面对象
page = SessionPage()
url = 'https://oglobo.globo.com/brasil/index/feed/pagina-{}.ghtml'
# 访问网页
for i in range(1, 5):
    print('url', url)
    page.get(url.format(i))
    # 在页面中查找元素
    items = page.eles('.feed-post-body')
    print(items)
    # 遍历元素
    for item in items:
        # 获取当前<h3>元素下的<a>元素
        lnk = item('.feed-post-link')
        # 打印<a>元素文本和href属性
        print(lnk.text, lnk.href)
