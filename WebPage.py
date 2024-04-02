
from DrissionPage import WebPage

# 创建对象
page = WebPage()

urls = 'https://www.cnnbrasil.com.br'
# 访问网页

page.get(urls)

page('.politica-2 menu-item politica').click()
# 等待页面跳转
page.wait.load_start()

links = page.eles('.home__list__tag')
# 修改为sessionPage 模式
page.change_mode()
for link in links:
    if link.link is not None:
        page.get(link.link)
        print(page.html)
