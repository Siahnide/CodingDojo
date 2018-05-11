from animal import animal
class nergigante(animal):
    def __init__(self,name):
        super(nergigante,self).__init__(name)
        self.health = 210
        self.defense = 20
    def spike_release(self):
        self.health -= 20
        self.defense += 20
    def display(self):
        print self.health,self.defense,"I AM NOOOT A DRAGON NOO"


char = nergigante("char")
char.display()
char.spike_release()
char.display()