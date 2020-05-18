import re
import requests
import html
import time
import urllib.request as spider

local_path = "./spider_qiushi_pic/"

def craml_image(image_url, image_local_path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' +
                             '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/' +
                             '537.36'}
    # r = requests.get(image_url, headers=headers)
    url = spider.Request("http:" + image_url, headers=headers)
    res = spider.urlopen(url)
    ret = res.read()
    with open(image_local_path, "wb+") as f:
        f.write(ret)


def craml(page=1):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' +
                             '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/' +
                             '537.36'}
    url = "https://www.qiushibaike.com/imgrank/page/" + str(page)
    url = spider.Request(url, headers=headers)
    res = spider.urlopen(url)
    ret = res.read().decode('utf-8')

    content_list = re.findall("<div class=\"thumb\">(.*?)</div>", ret, re.S)

    for content in content_list:
        image_list = re.findall("img src=\"(.*?)\"", content)
        print(image_list)
        for image_url in image_list:
            strs = image_url.strip().split("/")[-1]
            print(strs)
            craml_image(image_url, local_path + strs)


if __name__=='__main__':
    craml()