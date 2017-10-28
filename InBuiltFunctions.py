#Functions such as Zip, Map, Filter, Reduce
#'**********************************************************************************************************
#Zip Function
A  = ['1','1','1','1','1','1']
B  = ['2','2','2','2','2','2']
C = zip(A,B)

for x,y in C:
    print(x,y)
#**********************************************************************************************************
#Map Function allows us to pass a list of input to a function and collect the outputs
#We are taking the squares below
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print('1',squared)

#We can even pass a list of functions
def function1(x):
    return (x*x)
def function2(x):
    return (x+x)

funcs = [function1, function2]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print('2',value)
#**********************************************************************************************************
#Filter

less_than_3 = list(filter(lambda x: x < 3, items))
print('3',less_than_3)

#**********************************************************************************************************
#Reduce

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])