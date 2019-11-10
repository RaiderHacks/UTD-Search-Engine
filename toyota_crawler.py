from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
c = 0
def recursive_search(url):

    if url=='':
        url = 'https://en.wikipedia.org/wiki/List_of_Toyota_vehicles'    

    html = urlopen(url)

    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            recursive_search(link.attrs)

recursive_search('')
