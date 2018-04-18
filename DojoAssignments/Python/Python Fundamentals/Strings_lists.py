words = "It's thanksgiving day. It's my birthday,too!"
words.find("day")
print (words.find("day"))
print (words.replace("day","month"))
new_words = words.replace("day","month")


x = [2,54,-2,7,12,98]
print (max(x))
print (min(x))


x = ["hello",2,54,-2,7,12,98,"world"]
x_length = len(x)
print(x[0] , x[x_length-1])


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print(x)

x_length=len(x)/2
print (x_length)

count=0
new_string=[x[0]]
for count in range(1,x_length):
    new_string.append(x[count])
print(new_string)

count=0
for count in range(0,x_length):
    x.pop(0)
print(x)

x.insert(0,new_string)
print(x)

