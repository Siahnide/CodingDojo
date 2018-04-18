x = [1,2,3,4,5,6,7,8]





#if is number
isNumber = isinstance(x,int)
isString = isinstance(x,str)
isList = isinstance(x,list)


if isNumber == True and x>=100:
    print ("That's a big number!")
if isNumber == True and x<100:
    print ("That's a small number")

if isString == True and len(x)>=50:
    print ("That's a long sentence!")
if isString == True and len(x)<50:
    print ("Short sentence")

if isList == True and len(x)>=10:
    print ("Big List!")
if isList == True and len(x)<10:
    print ("Short List")

   
