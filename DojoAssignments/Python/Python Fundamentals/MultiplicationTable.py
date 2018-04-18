step = 1
for row in range(1,13):
    rowstring = ""
    if row==1:
        rowstring += "x"
        rowstring += " "
    rowstring += str(row)
    rowstring += " "
    for x in range(1,13):
        fac = row*x
        rowstring += str(fac) + " "
    print rowstring