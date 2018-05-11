import random

class char(object):
    def __init__(self):
        self.x = 1
        self.y = 1
        self.health  = 15
        self.armor  = 10
        self.attack  = 3
        self.damage  = 2
        self.speed  = 3
    def move(self,speed,direction):
        moves += 1
        if moves > self.speed:
            moves = 0
            
        if moves < self.speed:
            if direction == 1: #up
                self.y += 1
                return self
            elif direction == 2: #down
                self.y -= 1
                return self
            elif direction == 3: #left
                self.x += 1
                return self
            elif direction == 4: #right
                self.x -= 1
                return self
        return self
        
    def swing(self,target,*bonus):         
        
        try:attacks = random.randint(1 + self.attack,20 + self.attack) +bonus[0][0]
        except: attacks = random.randint(1 + self.attack,20 + self.attack)
        try: dmg = self.damage + bonus[0][1]
        except:dmg = self.damage

        if attacks > target.armor and target.health > 0:
            target.health -= dmg
            print "Hit with a",attacks,"| HP at",target.health
            if target.health == 0:
                target.destroy()
                print "dead"
        else:
            print "Missed with a",attacks
    def display(self):
        print "| HP",self.health,"| Armor",self.armor,"| Atk",self.attack,"| Dmg",self.damage,"| Speed",self.speed,"|"
    def destroy(self):
        self.x = 0
        self.y = 0
        #figure a way to remove from html

class Fighter(char):
    def __init__(self):
        super(Fighter,self).__init__()
        self.health = 20
        self.armor = 12
        self.damage = 3
    def spin(self,target):
        bonus = [2,1]
        super(Fighter,self).swing(target,bonus)
        
class Rogue(char):
    def __init__(self):
        super(Rogue,self).__init__()
        self.speed = 5
        self.attack = 4
        self.damage = 3
    def sneakatk(self,target):
        bonus = [-2,3]
        super(Rogue,self).swing(target,bonus)


