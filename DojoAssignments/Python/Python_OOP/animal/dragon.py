from animal import animal
class dragon (animal):
    def __init__(self,name):
        super(dragon,self).__init__(name)
    def fly(self):
        self.health -=10
    def display(self):
        print "I AM A DRAGON WITH",self.health,"HEALTH"

drake = dragon("drake")
drake.fly()
drake.fly()
drake.fly()
drake.fly()
drake.display()
