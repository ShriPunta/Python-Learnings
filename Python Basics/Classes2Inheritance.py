class Parent():
    def method1(self):
        print("This is the parent")

class Child(Parent):
    def method2(self):
        print("This is the child")


p = Parent
c = Child
p.method1(p)
c.method2(p)

class Parent1():
    def method1(self):
        print("This is is the multiple inheritance method 1")

class Parent2():
    def method2(self):
        print("This is the multiple inheritance method 2")

#Multiple Inheritance
class kid(Parent1,Parent2):
    #line below is essentially a blank line, but to handle the syntax error
    pass

k1 = kid()
k1.method1()
k1.method2()