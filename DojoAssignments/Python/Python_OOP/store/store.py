class store(object):
    def __init__(self,products,location,owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,product):
        self.products.pop(len(products)-1)
    def inventory(self):
        for x in self.products:
            x.displayinfo()



class product(object):
    def __init__(self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "sold"
        return self.status
    def addtax(self,rate):
        self.tax = self.price * rate
        return self.tax
    def returns(self,reason):
        self.status = reason
        if reason == "defective":
            self.price = 0
        if reason == "like new":
            self.status ="For Sale"
        if reason == "opened":
            self.status = "used"
            self.price = self.price * .8
        return self
    def displayinfo(self):
        print self.price
        print self.name
        print self.weight
        print self.brand
        print self.status
        return self










toy = product(10,"toy",100,"nameco")
box = product(30,"toy",100,"nameco")




x = [toy,box,toy,box,toy,box]



Bigma = store(x,"WA","Boblin Frankson")
Bigma.inventory()


