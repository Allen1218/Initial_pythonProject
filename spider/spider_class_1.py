import urllib.request


headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}
url = "http://www.fishc.com"
#urllib.request.Request()与urllib.request.urlopen()
response = urllib.request.urlopen("http://www.fishc.com",)
html = response.read()
#print(html) # bytes


# decode utf-8
html = html.decode("utf-8")
print(html)

response.geturl()
print(response.geturl())
print(response.getcode())
print(response.info())


