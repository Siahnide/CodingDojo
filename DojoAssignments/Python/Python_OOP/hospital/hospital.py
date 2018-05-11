
class hospital (object):
    def __init__(self,name,capacity,*patients):
        self.patients = list(patients)
        self.name = name
        self.capacity = capacity - len(self.patients)
    def info(self):
        print self.name
        names = ""
        for x in range(0,len(self.patients)):
            names += str(self.patients[x].ids)
            names += " "
            names += self.patients[x].name
            names += " "
            names += str(self.patients[x].bed)
            names += ", "
        print names
        print self.capacity

        
        
    
        
