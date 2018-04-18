def draw_stars(x):

    for i in range(0,len(x)):
        string = ""
        isInt = isinstance(x[i],int)
        isStr = isinstance(x[i],str)
        if isInt == True:
            for j in range(1,x[i]+1):
                string += "*"
        
        elif isStr == True:
            for j in range(0,len(x[i])):
                string += x[i][0]
        print string
            


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)