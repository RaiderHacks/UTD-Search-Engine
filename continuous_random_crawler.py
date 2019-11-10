from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(url):

    html = urlopen('https://en.wikipedia.org{}'.format(url))

    bs = BeautifulSoup(html,'html.parser')
    
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    
links = getLinks('/wiki/List_of_Toyota_vehicles')

while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']

    print(newArticle)

    links = getLinks(newArticle)
    
