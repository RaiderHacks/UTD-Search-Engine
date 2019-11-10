from urllib.request import urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')

except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"

except URLError as e:
    print('The server could not be found!')

else:
    # program continues. Note: If you return or break in the
    # exception catch, yo do not need to use the "else" statement
    print('It Worked!')

bs = BeautifulSoup(html.read(),'html.parser')

print(bs.h1)
