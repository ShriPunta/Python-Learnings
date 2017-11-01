

#putting curly braces will create a set which can only contain unique items
this_Is_A_Set={1,2,1,2,3,4,5,1,2}
print(this_Is_A_Set)

#Like a contains function
if 2 in this_Is_A_Set:
    print("this is a set.contains() function")


#This is equivalent to a map in Apex
#They are called Dictionaries
simpleMap = {'a':1,'b':2,'c':3,'d':4}

print(simpleMap)

#for iteration
for k,v in simpleMap.items():
    print(k,v)

def modu():
    print("hey Nice import")


#Unpacking a list
date, item, price = ['October 27,2017','Mouse',112]
print(item)

import heapq

notSoSimpleMap = [{'price':1},{'price':2},{'price':3},{'price':4}]
print(type(notSoSimpleMap))
#HeapQ
#Finding the largest
print(heapq.nsmallest(2,notSoSimpleMap,key = lambda x: x['price']))


#Sorting Dictionaries multiple keys
from operator import itemgetter
allUsers = [
    {'fname': 'Cate', 'lname':'Blanchett'},
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Chris', 'lname': 'Hemsworth'},
    {'fname': 'Tom', 'lname': 'Hiddleston'},
    {'fname': 'Tom', 'lname': 'Felton'},
    {'fname': 'Tom', 'lname': 'Hanks'}
]

#Sorted with fname, if the fname is same, we can give another argument to resolve the issue
for x in sorted(allUsers, key = itemgetter('fname')):
    print(x)

print('------------------------')

for x in sorted(allUsers, key = itemgetter('fname','lname')):
    print(x)