#Multiples
x=0
for x in range(0,1000): #print mult of 2x+1
    if x%2 == 1:
        print(x)
for x in range(5,1000000): #print mult of 5
    if x%5 ==0:
        print(x)

#Sum List
a = [1, 2, 5, 10, 255, 3]
length=len(a)
summation = 0
for z in range(0,length):
    summation += a[z]
print(summation)

#Average List
a = [1, 2, 5, 10, 255, 3]
length=len(a)
summation = 0
for z in range(0,length):
    summation += a[z]
print(summation/length)