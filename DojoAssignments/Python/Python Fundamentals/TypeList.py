l = ['magical unicorns',19,'hello',98.98,'world']
num = 0
char = 0
lists = 0
x=0
string = ""

for x in range(0,len(l)):
    isFloat = isinstance(l[x],float)
    isInt = isinstance(l[x],int)
    isString = isinstance(l[x],str)
    isList = isinstance(l[x],list)
    
    if isFloat == True or isInt == True:
        num += l[x]
        numswitch = True
        string += " "
    if isString == True:
        stringswitch = True
        string += l[x]

if numswitch == True and stringswitch !=True:
    print "Your list is of Integer Type"
if numswitch != True and stringswitch ==True:
    print "Your list is of String Type"
if numswitch == True and stringswitch ==True:
    print "Your list is of Mixed Type"


print "String:", string
print "Sum:",num






