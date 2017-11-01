class Enemy:
    health_points = 5
    _foo__is_dead = False

    #Defining a Constructor
    def __init__(self):
        print("This is basically a constructor {}")

    #Always returns a string || called when the object is to be "printed"
    def __repr__(self):
        return str(self.health_points)+':'+str(self._foo__is_dead)

    def set_hp(self,points_to_set):
        if self._foo__is_dead == False:
            self.health_points = points_to_set
        else:
            print("Enemy is already dead")

    def attack(self):
        print("Hint confirmed")
        self.health_points -= 1


        print(self._foo__is_dead)
        print(self.health_points)

        if (self.health_points <= -1):
            if not self._foo__is_dead:
                self._foo__is_dead = True
                print("Enemy Terminated")
            else:
              print("Enemy is  dead")
        else:
            print("Enemy has {} health remaining ".format(self.health_points))

    def reveal_hp(self):
        if self._foo__is_dead == False:
            print(self.health_points, " health points remaining")
        else:
            print("Enemy is already dead")


first_enemy = Enemy()

try:
    one_hp = int(input("Enter hit points for first enemy"))
except ValueError or one_hp > 100:
    print("Enter only numerical values and less than 100")
    exit(0)

#value_to_set = 10
first_enemy.set_hp(one_hp)
first_enemy.attack()
first_enemy.reveal_hp()

#----------------------------------------------------------------------------------------------
#Sorting Custom Objects
from operator import attrgetter
class User:

    def __init__(self,x,y):
        self.name = x
        self.id = y

    def __repr__(self):
        return self.name + ": " + str(self.id)


Userlist = [
    User('Sam',3),
    User('Dean',77),
    User('Craig',83),
    User('Josh',23),
    User('Tim',33),
    User('Riley',63),
    User('Kim',13),
]

for u in Userlist:
    print(u)

print('------------------------------------------------')

for u in sorted(Userlist,key=attrgetter('id')):
    print(u)