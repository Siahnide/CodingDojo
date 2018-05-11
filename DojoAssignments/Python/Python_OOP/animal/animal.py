class animal(object):
    def __init__(self,name):
        self.name = str(name)
        self.health = 150
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display(self):
        print self.health
        
        return self


dog = animal("dog")
dragon = animal("dragon")

dog.walk()
dog.display()
dog.walk()
dog.display()
dog.walk()
dog.display()
dog.run()
dog.display()
dog.run()
dog.display()
