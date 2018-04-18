def make_dict(list1, list2):
    new_dict = {}

    if len(list1) >= len(list2):
        key = list1
        values = list2
    elif len(list1) < len(list2) :
        key = list2
        values = list1
    
    for x in range(0,len(values)):

        new_dict[key[x]] = values[x]
    

    return new_dict
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print make_dict(name,favorite_animal)
