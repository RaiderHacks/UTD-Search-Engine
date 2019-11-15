from urllib.request import urlopen
from bs4 import BeautifulSoup
from config.py import *

def getLinks(url):
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs["href"])
            store_url(str(link))


def store_url(url):
    mycursor = mydb.cursor()
    sql = "INSERT INTO wiki (url) VALUES (%s)"
    val = (url,)
    mycursor.execute(sql, val)

    mydb.commit()

            

html = urlopen('http://en.wikipedia.org/wiki/Toyota')
bs = BeautifulSoup(html,'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs["href"])
        getLinks('https://en.wikipedia.org/wiki/')
        store_url(str(link))