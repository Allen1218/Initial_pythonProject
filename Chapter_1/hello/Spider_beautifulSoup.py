import re
import requests
import html
import time
import urllib.request as spider
from bs4 import BeautifulSoup

def craml_joke_list(page=1):
    # url = "https://www.qiushibaike.com/text/page/" + str(page)
    # res = requests.get(url)
    # requests.adapters.DEFAULT_RETRIES = 5
    # s = requests.session()
    # s.keep_alive = False

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' +
                             '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/' +
                             '537.36'}
    url = "https://www.qiushibaike.com/text/page/" + str(page)
    url = spider.Request(url, headers=headers)
    res = spider.urlopen(url)
    ret = res.read().decode('utf-8')
    #print(ret)

    # 1. 获取每一个段子的div正则
    reExp = "<div class=\"article block untagged mb15.*?" \
            "<div class=\"content\">.*?</div>";
    print(reExp)

    pattern = re.compile(reExp, re.S)

    # 2. 替换<br/>---> 换行
    body = html.unescape(ret).replace("<br/>", "\n")
    #print(body)
    m = pattern.findall(body)
    #print(m)

#<div class="author clearfix">
# \n<a rel="nofollow" style="height: 35px" onclick="_hmt.push([\'_trackEvent\',\'web-list-author-img\',\'
# chick\'])">\n\n<img src="//pic.qiushibaike.com/system/avtnew/3788/37883273/thumb/20180805220452.jpg?
# imageView2/1/w/90/h/90" alt="天热打鼓球">\n</a>\n<a onclick="_hmt.push([\'_trackEvent\',\
# 'web-list-author-text\',\'chick\'])">\n<h2>\n天热打鼓球\n</h2>\n</a>\n<div class="articleGender manIcon">
# 101</div>\n</div>\n\n<a href="/article/123119244" target="_blank" class="contentHerf"
# onclick="_hmt.push([\'_trackEvent\',\'web-list-content\',\'chick\'])">\n


#<div class="content">\n<span>\n\n\n
    # 十八岁那年，我喜欢的女孩给我发来一张小时候家族的全家福，说只要猜出哪个是她，就答应和我在一起。\n我猜了几次都没猜对！\n她失望的说，看来我俩是没缘分了，当时我就在妈妈肚子里，这么明显你居然就看不出来！
    # \n\n</span>\n\n</div>',

    #
    # 3. 抽取内容
    # 3.1 抽取用户名
    user_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>", re.S)
    # 3.2 段子内容正则
    content_pattern = re.compile("<div class=\"content\">(.*?)</div>", re.S)

    for joke in m:
        userName = user_pattern.findall(joke)
        #print(userName)
        output = []
        if len(userName) > 0:
            output.append(userName[0])

        content = content_pattern.findall(joke)
        if len(content) > 0:
            tmp = re.sub(r'[<span>:</span>]*', '', content[0])
            output.append(tmp.replace('\\n', ''))

        print("\t".join(output))

    # time.sleep(1)

# if __name__=='1__main__':
#     a=10
#     print(a)
#     for i in range(1, a):
#         craml_joke_list()


def craml_joke_bs4(page=1):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' +
                             '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/' +
                             '537.36'}
    url = "https://www.qiushibaike.com/text/page/" + str(page)
    url = spider.Request(url, headers=headers)
    res = spider.urlopen(url)
    ret = res.read()
    #print(ret)

    soup = BeautifulSoup(ret, "html5lib")
    joke_list = soup.find_all("div")
    print(joke_list)

    # for child in joke_list:
    #     print(child.find("h2").string() + "\t" +
    #           "".join(child.find("div", class_="content")))

if __name__ == '__main__':
    craml_joke_bs4()