import requests 
import re
from bs4 import BeautifulSoup

# word is defined by user input but the base url is hardcoded rn.  
def find_links(word):
    url = 'https://www.toyota.com/'
    links_found = []  

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')


    
    soup.find_all("a", href=re.compile(word))
    raw_links = soup.find_all("a", href=lambda href: href and word in href)
    
    for link in raw_links:
        print(link)

    return(str(raw_links))







