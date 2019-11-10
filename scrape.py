import requests 
import re
from bs4 import BeautifulSoup
# tag is a link and contains key word



# word is defined by user input but the base url is hardcoded rn.  
def find_links(word, target_url):
    url = target_url

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    links_with_word = []
    
    # soup.find_all("a", href=re.compile(word))
    # raw_links = soup.find_all("a", href=lambda href: href or word in href)
    
    # for tag in soup.find_all(True):
        # print(tag.name)

    objects_with_key = soup.find_all('a',text=re.compile(word))
    
    for object in objects_with_key:
        # if the keyword is in the object append it to links with word
        links_with_word.append(url + object.get('href') + object.string)


    print(links_with_word)
    return links_with_word

        
    # return str(links_with_word)








