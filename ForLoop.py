import os
A = [200,300,400,600,1000]
x = 500
y = 240

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

for i in range(5):
    print(i)
    print("Lol")

for i in range(5,10):
    print(i)

print("Its time to stop")
print('\n')

for i in range(5,20,2):
    if i is 17:
        print("go go more",i)
        break
    else:
        print (i)


print(os.name)
print("Its time to stop")
print('\n')

while i < 50:
    print(i)
    i+=1

for i in range(101):
    print(i)
    if i%4==0:
        print("Hey")