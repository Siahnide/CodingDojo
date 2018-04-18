word_list = ['hello','world','my','name','is','Anna']
character = "o"
new_string = ""
for x in range(0,len(word_list)):

    if word_list[x].find(character) >=0:
        new_string += word_list[x]
        new_string += " "
print new_string





