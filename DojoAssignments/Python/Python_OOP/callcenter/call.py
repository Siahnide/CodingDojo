class call (object):
    def __init__(self,ids,name,number,reason):
        self.ids = ids
        self.name = name
        self.number = number
        self.reason = reason
    
    def display(self):
        print "-",self.ids,"-", "Hello, my name is",self.name,"My number is",self.number," and I am calling because",self.reason
            


# call1 = call(1,"John",123,"Need a car")
# call1.display()