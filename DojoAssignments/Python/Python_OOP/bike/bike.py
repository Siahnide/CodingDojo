class bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        

    def displayinfo(self):
        print("price",self.price,"max speed", self.max_speed,"total miles", self.miles)
    def ride(self):
        print "riding..."
        self.miles += 10
        print "Rode for 10 miles putting miles at",self.miles
    def reverse(self):
        print "reversing..."
        if self.miles <=5:
            self.miles -= 5
            print "Reversed 5 miles putting miles at",self.miles



mybike = bike(100,27)
mybike.ride()
mybike.ride()
mybike.ride()
mybike.reverse()
mybike.displayinfo()
