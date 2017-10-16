import requests
import os  #  file system operations
import yaml # human-friendly data format
import re  # regular expressions
#import pandas as pd # pandas... the best time series library out there
import datetime as dt # date and time functions
import io

#import Image_Download_From_Url
#csv_url_to_download = r'https://query1.finance.yahoo.com/v7/finance/download/VALE?period1=1505499873&period2=1508091873&interval=1d&events=history&crumb=uc8SlFiAzf5'
url_of_finance_site = 'https://uk.finance.yahoo.com/quote/AAPL/history'
req = requests.get(url_of_finance_site)
print(req.cookies)
html_content = req.text
cookie = req.cookies['B']
print("Cookie : ",cookie)
base_dir = r'C:\\Users\\shrip\\Pictures\\url_downloads\\'


# Now we need to extract the token from html.
# the string we need looks like this: "CrumbStore":{"crumb":"lQHxbbYOBCq"}
# regular expressions will do the trick!

#Decompiling the regular expression
# .* --> simply means it doesn't matter what comes before .and *
# "{'cookie':cookie,'crumb':crumb}" --> this is the string that needs to be searched as it
# () --> inside the bracket is the capturing group
# ?P --> means group creation with the name specified in < >. text matched can be retrieved by the group name
# [] --> signify the set characters to be matched
# [^"] --> means capture all characters which is not ' " '
# + --> one or more times. The whole capturing group can occur more than once
# \{ and \} it means take the brackets literally and find them
pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')
print(pattern)


for each_line in html_content.splitlines():
    matc = pattern.match(each_line)
    if matc is not None:
        crumb = matc.groupdict()['crumb']
        print(("Crumb ==>", crumb))

cookie_data_needed = {'cookie':cookie,'crumb':crumb}

file_to_store_cookie = base_dir + 'yahoo_cookie.yml'

with open(file_to_store_cookie,'w') as fid:
    yaml.dump(cookie_data_needed,fid)

start_date = (2007,1,1)
end_date = (2019,5,20)
print(start_date)
print(dt.datetime(*start_date).timestamp())





















# def download_csv_data(csv_url):
#     response = request.urlopen(csv_url)
#     csv = response.read()
#     csv_str = str(csv)
#     lines = csv_str.split("\\n")
#     dest_url = base_dir + r'finance.csv'
#     file_write = open(dest_url,"w")
#     for each_line in lines[:40]:
#         file_write.write(each_line + "\n")
#     file_write.close()
#
# download_csv_data(csv_url_to_download)
