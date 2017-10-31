

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
notSoSimpleMap = {'price1':1,'price2':2,'price3':3,'price4':4}
#HeapQ
#Finding the largest
print(heapq.nsmallest(2,notSoSimpleMap))
