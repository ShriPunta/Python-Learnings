import requests
from bs4 import BeautifulSoup
import operator
import sys

def get_site_and_parse(url_to_parse):
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

    #print(len(word_list))
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
        word_list[i] = word_list[i].strip()
        word_list[i] = word_list[i].replace(" ", "")
    #print(word_list)
    create_dic(word_list)

def create_dic(clean_words):
    freq_map = {}
    sorted_freq_map = {}
    #equivalent to creating a new map in Salesforce
    for word in clean_words:
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1

    #print(freq_map)

    #For Sorting purposes
    #Operator.itemgetter sorts accordng to the input
    #if itemgetter(1) then according to the value/frequency
    #if itemgetter(0) then according to the key in dictionary i.e alphabetically in this case
    for key,value in sorted(freq_map.items(),key=operator.itemgetter(1)):
        sorted_freq_map[key] = value
        print(key,value)
    #print(sorted_freq_map)

get_site_and_parse('http://www.cs.sjsu.edu/~stamp/evals.html')


# -----------------------------using COunter to get the frequency---------------------------------------------
from collections import Counter

zxc = 'yaada yaada yaada bada bada bada yada yada badda badda badda poda poda poda bum bum pum pum'
words = zxc.split()
counter= Counter(words)
first_two = counter.most_common(2)
print(first_two)