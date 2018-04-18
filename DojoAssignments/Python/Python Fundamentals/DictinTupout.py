# function input

my_dict = [
  {"Speros": "(555) 555-5555"},
  {"Michael": "(999) 999-9999"},
  {"Jay": "(777) 777-7777"}
]

# function output

# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dictTup (my_dict):
    my_tuple = []
    for x in range(0,len(my_dict)):
        my_tuple.append(my_dict[x])
    print (my_tuple)


dictTup(my_dict)
print (my_dict[0])