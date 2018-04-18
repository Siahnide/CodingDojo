import random
def cointoss(tries):
    print "Starting the Program..."
    heads = 0
    tails = 0
    for x in range(1,tries+1):
        random_num = random.randint(1,2)
        if random_num==1:
            heads +=1
            print "Attempt #",x,": Throwing a coin... It's a Head! ... Got",heads,"head(s) so far and",tails,"tail(s) so far."
        if random_num==2:
            tails +=1
            print "Attempt #", x,": Throwing a coin... It's a Head! ... Got",heads,"head(s) so far and",tails,"tail(s) so far."
    print "Ending the program now, Thankyou!"

cointoss(100)




# def cointoss(tries)