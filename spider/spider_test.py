# python3的urllib2与urllib合并
import urllib.request as spider

# urlopen()函数用于实现对目标url的访问
headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}
url = "http://www.fishc.com"
url = spider.Request(url, headers=headers)
res = spider.urlopen(url)
ret = res.read().decode('utf-8')
print(ret)


# 参考文档
#1- https://blog.csdn.net/The_Time_Runner/article/details/86522700?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
#2-https://blog.csdn.net/NeverLate_gogogo/article/details/88417936
