import requests
from bs4 import BeautifulSoup
import re
import random

base_dir = r'C:\\Users\\shrip\\Pictures\\url_downloads\\'

url_to_crawl = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"


def crawler_method(url_to_crawl):
    domain = get_domain_name(url_to_crawl)
    i = 0

    source_code = requests.get(url_to_crawl)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text,"html.parser")
    for sidebar_titles in soup.findAll('a',{'class': 'reference internal'}):
        if i is 0:
            header = "Titles and Links for " + domain
            file_to_write.write(header)
            file_to_write.write('\n---------------------------------------------------------------------------- \n \n')
            i+=1

        href = sidebar_titles.get('href')
        if str(href).find(".com") == -1:
            href = url_to_crawl + href
        title = sidebar_titles.string
        Index = str(i) + ": \t"
        file_to_write.write(Index)
        if title is not None:
            file_to_write.write(title)
        else:
            file_to_write.write('### NO TITLE ###')
        file_to_write.write('\n')
        file_to_write.write(href)
        file_to_write.write('\n\n---------------------------------------------------------------------------- \n \n')
        i+=1

        print_to_file()


def get_domain_name(url):
    pattern = re.compile('^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?(?P<dom>[^:\/\n]+)')
    print(pattern)
    rand_name = random.randrange(0, 999999)
    matc = pattern.match(url)
    if matc is not None:
        dom = matc.groupdict()['dom']
        print('Dom', dom)

    return dom[:-4]

def print_to_file(collectn_to_parse,domain):
    file_name = base_dir + domain + ".txt"
    file_to_write = open(file_name, 'w')

crawler_method(url_to_crawl)