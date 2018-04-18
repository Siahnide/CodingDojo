def even_odd (x):
    if x%2 == 0:
        print "Number is",x,"This is an Even Number"
    if x%2 == 1:
        print "Number is",x,"This is an Odd Number"

for i in range(0,2001):
    even_odd(i)

def multiply(arr,mult):
    
    for j in range(0,len(arr)):
        
        arr[j] *= mult
    return arr
a = [1,2,3]
b = multiply(a,5)
print b

def layered_multiples(arr,mult):
    new_array =[]
    for i in range(0,len(b)):
        array = []
        
        for j in range(0,b[i]*2):
            array.append(1)
        new_array.append(array)


    return new_array

x = layered_multiples(b,2)

print x