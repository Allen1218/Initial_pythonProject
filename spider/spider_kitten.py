import urllib.request

response = urllib.request.urlopen("http://placekitten.com/500/760")
cat_img = response.read()

with open('cat_500600.jpg', 'wb') as f:
    f.write(cat_img)


print(response.geturl())
print(response.getcode())
print(response.info())