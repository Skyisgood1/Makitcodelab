#2022-04-08

#001
'''
class seal:
    pass
stamp = seal()
print(type(stamp))

arr = []
print(type(arr))
'''

'''
class Block:
    def print_name(self):
        print("HI. I'm BLOCk")
b = Block ()
b.print_name()
'''

'''
class Factory:
    def __init__(self, company, product, manager):
        self.company = company
        self.product = product
        self.manager = manager

        def __str__(self):
            result = ''
            result += "This factory belongs to" + self.company
            result += "This factory makes" + self.product
            result += "This factory manager's name is" + self.manager
            return result

factory1 = Factory("Apple","Macbook","Tim Cook")
factory2 = Factory("Braun","LP Player","Dieter Rams")
factory3 = Factory("Nintendo","Switch","Satoru Iwata")

print(factory1.__str__())
print(factory1)
'''

'''
import random
import time

class Character:
    def __init__(self,physical,role,hp):
        self.physical = physical
        self.role = role
        self.hp = 100
        self.power = random.randint(1,20)

    def attack(self, target):
        self.power = random.randint(1,20)
        target.hp -= self.power

    def defense(self, attacker):
        self.hp -= attacker.power*0.5 
    
me = Character("신승민","흑마법사",100)
enemy = Character("누군가",'얼음용사',100)

while True:
    if me.hp<=0:
        print('ENEMY WINS')
        break
    elif enemy.hp<=0:
        print('YOU WIN')
        break
    
    me.num = random.randint(1,100)
    enemy.num = random.randint(1,100)
    
    if me.num != enemy.num:
        if me.num > enemy.num:
            me.attack(enemy)
            print(me.physical + "공격함")
        else:
            enemy.attack(me)
            print(enemy.physical + "공격함")
        print('My character HP: ' + str(me.hp) + "/Enemy HP: " + str(enemy.hp))
        time.sleep(1)
'''



























