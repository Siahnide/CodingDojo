class car (object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = str(mileage) +str("mpg")
        if self.price > 10000:
            self.tax = 0.15
        elif self.price <10000:
            self.tax = 0.12
    def display_all(self):
      print self.price,self.fuel,self.mileage,self.price


mycar = car(10000,5,"full",56)
mycar1 = car(20000,5,"full",56)
mycar2 = car(30000,5,"full",56)
mycar3 = car(40000,5,"full",60)
mycar4 = car(50000,5,"full",70)
mycar5 = car(60000,5,"full",1000)

mycar.display_all()
mycar1.display_all()
mycar2.display_all()
mycar3.display_all()
mycar4.display_all()
mycar5.display_all()