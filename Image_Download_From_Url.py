import urllib.request
import random

def image_ret(url):
    rand_name= random.randrange(0,100)
    base_dir = "C:/Users/shrip/Pictures/url_downloads/"
    full_name= base_dir + str(rand_name) +".jpeg"
    urllib.request.urlretrieve(url,full_name)

image_ret(str("https://www.python-course.eu/images/RE.png"))