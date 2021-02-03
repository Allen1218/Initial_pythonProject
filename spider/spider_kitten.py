import urllib.request

response = urllib.request.urlopen("https://cn.bing.com/th?id=OHR.ChipmunkJP_ZH-CN1697070440_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp")
cat_img = response.read()

with open('111111.jpg', 'wb') as f:
    f.write(cat_img)


print(response.geturl())
print(response.getcode())
print(response.info())