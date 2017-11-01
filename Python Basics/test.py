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