import random

#Random values below are chosen at random then if statements below determine how many points are given

randomValue1 = random.randint(0,1)
randomValue2 = random.randint(0,1)
randomValue3 = random.randint(0,1)


rewardPoints= 0 #most of the if statements are made to determine the final value of rewardPoints 

BonusPoints1 = 1 #Perhaps this is unnecessary but to ensure that the bonusPoints are organized and not random numbers, heads = 1 and BonusPoints = 1 can be confusing
BonusPoints2 = 2
BonusPoints3 = 3 
BonusPoints4 = 4
BonusPoints5 = 5

heads = 1 # Heads and tails are later compared with the randomValue to assigned points 
tails = 0

#These three letterValues are for the final output of the results which must be converted as a number in randomValue to a letter (H or T) in letterValue

letterValue1= "H"
letterValue2= "H"
letterValue3= "H"


#These nested if statements below determine if the first number is heads then if both are heads

if randomValue1 == heads:
    rewardPoints = rewardPoints + BonusPoints3
    if randomValue1 and randomValue2 == heads:
        rewardPoints = rewardPoints + BonusPoints4
        print("final rewards points", rewardPoints)
    else: rewardPoints = rewardPoints + BonusPoints1
else:
    rewardPoints += BonusPoints2
   

#The code below determines if the 2nd and 3rd value are equal to 1 (heads) but not both

if (randomValue2 != randomValue3) and (randomValue2 == heads or randomValue3 == heads) :
    rewardPoints += BonusPoints5
    
else: rewardPoints = rewardPoints + BonusPoints1

#These three if statements below help convert the numerical random numbers 1 and 0 into letters, they are set as H unless the randomValue is 0 for tails which becomes T 

if randomValue1 == tails: 
    
    letterValue1= "T"

if randomValue2 == tails:
    
    letterValue2 = "T"

if randomValue3 == tails:
    
    letterValue3 = "T"


#These below are for the final output that the user sees

print("The three random coins are: ", letterValue1, letterValue2, letterValue3)

print("You have earned", rewardPoints, "points")








    

