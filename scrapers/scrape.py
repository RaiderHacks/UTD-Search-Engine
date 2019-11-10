import requests 
import re
from bs4 import BeautifulSoup

# word is defined by user input but the base url is hardcoded rn.  
def find_links(word):
    url = 'https://www.toyota.com/'
    
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')


    
    # soup.find_all("a", href=re.compile(word))
    # raw_links = soup.find_all("a", href=lambda href: href or word in href)
    
    # for tag in soup.find_all(True):
        # print(tag.name)

    objects_with_key = soup.find_all('a',text=re.compile(word))

    for object in objects_with_key:
        print(str(object) + '\n')


    # print(raw_links)
    # return(raw_links)




find_links('car')



