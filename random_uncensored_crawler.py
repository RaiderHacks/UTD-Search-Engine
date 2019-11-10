from urllib.request import urlopen

from urllib.parse import urlparse

from bs4 import BeautifulSoup

import re

import datetime

import random

pages = set()

random.seed(datetime.datetime.now())

# Retrieves a list of all Internal links found on a page

def getInternalLinks(bs,includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)
    internalLinks = []

    # Finds all links that begin with a "/"

    for link in bs.find_all('a',href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks

# Retrieves a list of all external links found on a page

def getExternalLinks(bs,excludeUrl):
    externalLinks = []

    # Finds all links that start wiht "http" or "www" that do
    # not contain the current URL

    for link in bs.find_all('a',href=re.compile('^(https|http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html,'html.parser')
    externalLinks = getExternalLinks(bs,urlparse(startingPage).netloc)

    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')

        domain = '{}://{}'.format(urlparse(startingPage).scheme,urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs,domain)
        return getRandomExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)

    print('Random external link is: {}'.format(externalLink))
    
    followExternalOnly(externalLink)

followExternalOnly('https://oreilly.com')

'''
allExtLinks = set()

allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteURl).scheme,urlparse(siteUrl).netloc)

    bs = BeautifulSoup(html,'html.parser')

    internalLinks = getInternalLinks(bs,domain)

    externalLinks = getExternalLinks(bs,domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')

getAllExternalLinks('http://oreilly.com')
'''


