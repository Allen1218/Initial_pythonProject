import urllib.request
import os

def get_page(url):
    pass

def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    pagenum = int(get_page(url))

    #http://jandan.net/ooxx/MjAyMDA1MTMtMTgw#comments
    for i in range(pages):
        pagenum -= i
        page_url=url+'page-'+str(pagenum) + 'comments'