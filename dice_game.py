
import random


def main():

    counter = 0

    done = False  #this helps while loop search later for a specific number

    while counter <= 10 :

        dice1 = random.randint(1,6) #first dice rolls

        dice2 = random.randint(1,6)  #second dice rolls

        diceCalculation = diceRoll(dice1, dice2) #method determines total of dice

        print(diceCalculation)

        if diceCalculation == 2 or diceCalculation == 3 or diceCalculation == 12:

            print("You lose...") #if sum is 2,3 or 12 then player loses 

            return

        elif diceCalculation == 7 or diceCalculation == 11:

            print("You win") #if player rolls total of 7 or 11 player wins 

            return 

        elif diceCalculation == 1 or diceCalculation == 4 or diceCalculation == 5 or diceCalculation == 6 or diceCalculation == 8 or diceCalculation == 9 or diceCalculation == 10:
            #if any of the numbers above are rolled then the dice will be rolled again
            
            while not done : #continues code until certain value has been found 
                
                diceTest1 = random.randint(1,6) #dice is rolled again

                diceTest2 = random.randint(1,6) #dice is rolled again

                diceCalculation2 = diceRoll(diceTest1, diceTest2) #dice sum is determined again 

                if diceCalculation2 == diceCalculation: #if they roll the same number already rolled at beginning of code then they win

                    print("You win")
                    
                    return True #terminates code 

                elif diceCalculation2 == 7:  #if they get a 7 they lose 

                    print("You lose...")

                    return True #terminates code 
                
        counter += 1



def diceRoll(diceOne, diceTwo): #this method determines sum of dice and then outputs the original amounts and the sum

    diceSum = diceOne + diceTwo  

    print("You rolled", diceOne, "+", diceTwo, "=", diceSum)
    
    return diceSum  #the return makes the dice roll method equal dice sum 
    

main()





