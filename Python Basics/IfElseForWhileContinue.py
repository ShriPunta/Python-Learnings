A = [200,300,400,600,1000]
x = 500
y = 240

#Entire Python works on indentations, there are no brackets
#Writing 0 to 2 will clip the array of its first 3 elements
for i in A[0:2]:
    z = (i - x)/y
    print(z)

name = "Lucy"

if name is "Lucy":
    print("Hey Guys!")
elif name is "Samantha":
    print("My name")
else:
    print("ssup")

print("Its time to stop")
print('\n')

#Range creates a temporary list 5 means 5 integers 0,1,2,3,4
for i in range(5):
    print(i)
    print("Lol")
#Writing 5,10 means 5,6,7,8,9
for i in range(5,10):
    print(i)

print("Its time to stop")
print('\n')
#This range means 5,6,7,... but in intervals of 2 i.e. 5,7,9,11,...
for i in range(5,20,2):
    if i is 17:
        print("go go more",i)
        break
    else:
        print (i)

#Prints the OS type
print(os.name)
print("Its time to stop")
print('\n')

#Keeps on iterating until this condition is false
while i < 50:
    print(i)
    i+=1

#Temporary Integer list of 100 numbers
for i in range(101):
    print(i)
    if i%4==0:
        print("Hey")

challenge = [1,2,3,4,5,6,7,8,9]

for n in challenge:
    if n%2==0:
        continue
        print('\n')
    else:
        print(n)

#For Anonymous looping use '_'
#0,1,2,3,4,5,6,7,8
k=0
for _ in range(1, 10):
    print("beh {}".format(k))
    k+=1