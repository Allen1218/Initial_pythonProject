import urllib.request
import urllib.parse
import json
import time


while True:
    content = input('''请输入需要翻译的内容 (输入"q!"退出程序)：''')
    if content == 'q!':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data["i"] = content  #"我爱中国"
    data["from"] = "AUTO"
    data["to"] = "AUTO"
    data["smartresult"] = "dict"
    data["client"] = "fanyideskweb"
    data["salt"] = "15834926807363"
    data["sign"] = "937448b30a8475cbf70d5239627352d3"
    data["ts"] = "1583492680736"
    data["bv"] = "bc250de095a39eeec212da07435b6924"
    data["doctype"] = "json"
    data["version"] = "2.1"
    data["keyfrom"] = "fanyi.web"
    data["action"] = "FY_BY_CLICKBUTTION"
    data["action"] = "FY_BY_CLICKBUTTION"

    data = urllib.parse.urlencode(data).encode("utf-8")
    response = urllib.request.urlopen(url, data)
    html = response.read().decode("utf-8")
    # print(html)

    target = json.loads(html)
    # print(type(target))
    # print(target['translateResult'])
    # print(type(target['translateResult']))

    # print(target['translateResult'][0][0]['tgt'])
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

    time.sleep(5)