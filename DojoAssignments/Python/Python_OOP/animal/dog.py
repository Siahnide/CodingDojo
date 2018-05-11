from animal import animal
class dog(animal):
    def __init__(self,name):
        super(dog,self).__init__(name)
        self.health = 150
        self.name = name
    def pet(self):
        self.health += 5

boi = dog("boi")

boi.pet()
boi.pet()
boi.pet()
boi.pet()
boi.pet()
boi.pet()
boi.display()