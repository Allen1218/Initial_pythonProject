import urllib.request
import re

headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}
url = urllib.request.Request("https://www.jianshu.com/u/7f2a43e92b56", headers=headers)
response = urllib.request.urlopen(url, timeout=15)
html = response.read().decode("utf-8")

# print(html)
# <div class="title">
#    <a class="name" href="https://www.jianshu.com/u/7f2a43e92b56">守住这块热土</a>
# </div>

# re.S : 多行，算作一行
m = re.finditer(r'<div class="title"><a class="name" href=(.*?)</a>', html, re.S)
for t in m:
    print(t)


