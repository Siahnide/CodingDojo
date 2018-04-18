step = 1
for row in range(0,5):
    rowstring = ""
    for x in range(0,9):
        if step == 1:
            rowstring += "*"
            step = 0 
            continue
        elif step == 0:
            rowstring += " "
            step = 1
            continue
    print rowstring