from call import call
class callcenter (call):
    def __init__(self,*call):
        self.calls = list(call)
        self.queue = len(self.calls)
        
    def add(self,new):
        self.calls.append(new)
        return self
    def remove(self):
        del self.calls[0]
        return self
    def info(self):
        for x in range(0,self.queue):
            print self.calls[x].name,self.calls[x].number
        return self
    # def removeuser(self,phonenumber):
    #     for x in range(0,self.queue-1):
    #         if self.calls[x].number == phonenumber:           I'm going to come back to this assignment to achieve hacker eventually.
    #             del self.calls[x]
                
    #     return self
            



call1 = call(1,"John",123,"Need a car")
call2 = call(2,"Mary",456,"Have a car")
call3 = call(3,"Does",789,"Sold a car")
calls = callcenter(call1,call2,call3)

calls.info()

# calls.removeuser(456)
# calls.info()


