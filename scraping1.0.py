#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:34:05 2018

@author: kmanchel
"""

from requests import get
from bs4 import BeautifulSoup, re
from urllib import parse 


def download(response, soup):
    html = response.text
    title_tag = str(soup.title)
    file_name = title_tag.strip('</title>')
    file_name+='.html'
    f = open(file_name,"w")
    f.write(html)
    f = open(file_name,"w")
    f.write(html)
    print("Successfully Downloaded file: ",file_name)
    return True
    
def scrape_links(url, soup):
    first = soup.find('a', attrs={'href': re.compile("/")})
    try:
        l1 = first.get('href')
        a = [first]
        links = [l1]
        n = 0
        length = len(soup.findAll('a',attrs={'href': re.compile("/")}))
        while n<(length-1):
            #extracting the relevant a tags and putting into an array
            blah = a[n].find_next('a', attrs={'href': re.compile("/")})
            a.append(blah)
            #extracting the href links from a and placing them in an array
            link = blah.get('href')
            clean_link = parse.urljoin(url, link)
            links.append(clean_link)
            n+=1
        return links
    except: 
        print("\nThis Link is not scrapable!!!!!")




def crawl(start_url, levels):
    print("Crawling URL: ",start_url,"\n")
    url = start_url
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = scrape_links(url,soup)
    try:
        print(len(links))
    except:
        print("0")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    download(response,soup)
    i = 1
    while i<levels:
        remaining = levels - i
        num = len(links)
        c = 0
        while c<(num-1):
            print("Link list number: ",c)
            crawl(links[c],remaining)
            c+=1
        i+=1
        
#RUNNING THE ABOVE FUNCTIONS
url = 'http://www.stat.purdue.edu/~lingsong/'
levels = 2
crawl(url,levels)
    
 
