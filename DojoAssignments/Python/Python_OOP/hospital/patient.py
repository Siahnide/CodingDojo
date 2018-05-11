from hospital import hospital

x=0
class patient (object):
    def __init__(self,ids,name,allergies,bed):
        self.ids = ids
        self.name = name
        self.allergies = allergies
        try: 
            self.bed = bed
        except:
            self.bed = 0
            
            
    def admit(self,hospitalname):
        if hospitalname.capacity != 0:
            hospitalname.patients.append(self)
            hospitalname.capacity -= 1
            print "Success!"
        else:
            print "Capacity full!"
    def discharge(self,hospitalname):
        self.bed = 0
        for x in range(0,len(hospitalname.patients)):
            if hospitalname.patients[x].name == self.name:
                hospitalname.capacity += 1
                del hospitalname.patients[x]
                break



tim = patient(1,"tim",0,14)
bob = patient(2,"bob","apples",13)
john = patient(3,"John",0,12)
garry = patient(4,"Garry",0,11)
jake = patient(5,"jake",0,10)
jans = patient(6,"jans","stuff",9)

harrison = hospital("harrison",5)

tim.admit(harrison)
bob.admit(harrison)
john.admit(harrison)
garry.admit(harrison)
jake.admit(harrison)

jans.admit(harrison)

harrison.info()
jake.discharge(harrison)
jans.admit(harrison)
harrison.info()