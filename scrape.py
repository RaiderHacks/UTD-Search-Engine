import requests 
import urllib.request
import re
from bs4 import BeautifulSoup
from vibe_check import analyze_sentiment
# tag is a link and contains key word



# word is defined by user input but the base url is hardcoded rn.  
# url = "https://www.vox.com/"
# text = "Trump"
links_to_check = []
def find_links(word, target_url):
    word = word
    url = target_url
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')


    objects_with_key = soup.find_all('a',text=re.compile(word))
        
    return objects_with_key
## ======= ============================================================
# Add links into array 
# for link in find_links(word, target_url):
#     links_to_check.append((link.get('href')))


list = links_to_check
# Return text of each link in the array
def retrieve_text(list_of_links):
    arts = []

    for link in list_of_links:
        html = requests.get(link)
        soup = BeautifulSoup(html.text, 'html.parser')
#     # kill all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()    # rip it out
#
#     # get text
        text = soup.get_text()
#
#     # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
#     # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#     # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        arts.append(text)
        print(text)
    return str(arts)

        








