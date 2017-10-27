import requests
from bs4 import BeautifulSoup
import operator
import sys

def make_dic(url_to_parse):
    word_list = []
    src_code = requests.get(url_to_parse).text
    soup = BeautifulSoup(src_code, "html.parser")
    for src_text in soup.findAll('li'):
            content = src_text.string
            try:
                words = content.lower().split()
            except:
                print('Unexpected Error :', sys.exc_info()[0])
                continue
            for each_word in words:
                word_list.append(each_word)
    print(len(word_list))
    #print(word_list)
    clean_words(word_list)

def clean_words(word_list):
    #From Key creates a map(dictionary in python words) -->( 0 , A)
    #ord converts a character to ASCII decimal i.e.  A --> 97
    #Map function is a discreet way of applying the same function on a list of input [http://book.pythontips.com/en/latest/map_filter.html]


    #translation_table = dict.fromkeys(map(ord, '!@#$'), None)
    #unicode_line = unicode_line.translate(translation_table)
    for i in range(len(word_list)):
        word_list[i] = word_list[i].translate({ord(c): None for c in '~!@#$%^&*()_+=-,./\'\"[]{}\\|?'})
    print(word_list)

make_dic('http://www.cs.sjsu.edu/~stamp/evals.html')