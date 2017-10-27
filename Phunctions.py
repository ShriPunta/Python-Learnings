#Each Function named with keyword 'def'
def firstFuncEver(x,y,z):
    sum=x+y+z
    return sum

#Scope of Variable is defined by where its  declaration in the program
#Higher (higher from start of program) declarations means greater scope of variable

#if you give value in the function start, it is the default value
def secFuncEver(x,y=2,z=1):
    return firstFuncEver(x,y,z+6)

for x in range(0,10):
    print("Add ", x,"them",secFuncEver(x,y=45), " ")
    print(secFuncEver(x))
    print('\n')

#This gives Flexibility, it means whatever number of variables there are
#they will be taken in an array format
def flexi_Param(*args):
    sum = 2
    print(args)
    for n in args:
        sum+=n
    return sum

print(flexi_Param(1))
print(flexi_Param(1,2,4))

flexi=[9,8,7]

def Flexi_Args(add1,add2,add3):
    print(add1,add2,add3)
    sum1=add1+add2+add3
    return sum1

#Flexi is sent as a an array itself, and taken up 1 by 1
#The number of elements should perfectly match number of parameters
#Called UnPacking of Arguments
Flexi_Args(*flexi)

import Collecshuns

Collecshuns.modu()

#Using Unpacking of variables
#We can use this unpacking if we do not know the variables
#What it does is, it stores the first number in 'first' and last number in 'last'
#All the middle numbers are stored in 'middle'
def Flexi_Args(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)

Flexi_Args([1,2,3,4,5,6,7,8,9])
Flexi_Args([200,1,1,1,1,1,1,1,200])