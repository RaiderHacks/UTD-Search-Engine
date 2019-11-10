from urllib.request import urlopen
from bs4 import BeautifulSoup


def recursive_search(url):

    if url=='':
        url = 'https://en.wikipedia.org/wiki/List_of_Toyota_vehicles'    

    html = urlopen(url)

    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            if 'toyota' in link.attrs['href']:
                print(link.attrs['href'])
            # recursive_search(link.attrs)

recursive_search('')
