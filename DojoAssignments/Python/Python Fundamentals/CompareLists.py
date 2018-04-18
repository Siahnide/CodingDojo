l = [1,2,3,4,5]
l2 = [1,2,3,4,5]


test = True
for x in range(0,len(l2)):
    
    if l[x] != l2[x]:
        test = False
        
if test == False:
    print "Your lists are not the same"
    
else:
    print "You lists are the same!"