import re
import builtins
pattern = re.compile('^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?(?P<dom>[^:\/\n]+)')
print (pattern)
url = "https://regex101.com/r/wN6cZ7/63"
matc = pattern.match(url)
if matc is not None:
    dom = matc.groupdict()['dom']
    print('Dom',dom)

print(url[:-4])

test_Dict = dict()
test_Dict = {'1':'a','2':'b','3':'c','4':'d'}
print(test_Dict)
# test_Dict[1]='d'
# print(test_Dict)
#
# test_Dict.update('1' : 'h')
# print(test_Dict)
# test_Dict.update()
# print(test_Dict)


for i in range(1,11):
    J = (3 * i )
    K = J + 7
    L = K % 11
    #For printing in binary
    print(i,' ',L,' ',"{0:04b}".format(L))

base_dir = r'C:\Users\shrip\Pictures\url_downloads\\'

curr_filepath = base_dir+r"test\\"

import os
for root, dirs, files in os.walk(curr_filepath, topdown=True):
      for filename in root:
          print(root)
          print('-----------------')
print('******************')


def defin_header():
    return (r"Latitude,Longitude,dele_colum,Altitude,dele_colum,Date,Time \n")

def line_pre_adder(filename):
    f = fileinput.input(filename, inplace=1)
    for xline in f:
        if f.isfirstline():
            print(defin_header().rstrip('\r\n') + '\n' + xline)
        else:
            print(xline)

#delete first 6 lines
def del_start_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.seek(0,0)

    f = open(filename, 'w')
    f.write(defin_header())
    f.write('\n')
    f.writelines(lines[6:])
    f.close()



filename = r"C:\Users\shrip\Pictures\url_downloads\test\20081027115449.txt"
del_start_lines(filename)
#line_prepender(filename)