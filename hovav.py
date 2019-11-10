from urllib.request import urlopen
from bs4 import BeautifulSoup


def recursive_search(url):

    if url=='':
        url = 'https://hovav.net/ucsd/dist/noret-ccs.pdf'
    html = urlopen(url)

    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            if 'attack' in link.attrs['href']:
                print(link.attrs['href'])
            # recursive_search(link.attrs)

recursive_search('')
