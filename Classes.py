class Enemy:
    health_points = 5
    _foo__is_dead = False

    #Defining a Constructor
    def __init__(self):
        print("This is basically a constructor {}")

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