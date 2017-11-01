import urllib.request
import random
base_dir = r'C:\\Users\\shrip\\Pictures\\url_downloads\\'
def image_ret(url):
    rand_name= random.randrange(0,100)
    #Using r transforms the string into a raw string
    #using double backslash treats 2nd backslash into a string instead
    #of recognizing it as \u or \r  special character

    full_name= base_dir + str(rand_name) +".jpeg"
    urllib.request.urlretrieve(url,full_name)

image_ret(str("https://www.python-course.eu/images/RE.png"))