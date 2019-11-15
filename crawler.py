from urllib.request import urlopen
from bs4 import BeautifulSoup

def getLinks(url):
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])

html = urlopen('http://en.wikipedia.org/wiki/Toyota')
bs = BeautifulSoup(html,'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        getLinks('https://en.wikipedia.org/wiki/')

