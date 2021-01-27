
import random

def main():
    
    numberSets= int(input("Please enter the number of sets you wish to play:"))
    
    player1Name = input("Please enter the first players name:") #determines player name 

    player2Name = input("Please enter the second player's name:")

    endGameTotalPlayer1 = 0 #this will be computed as a global variable to determine who wins the game 

    endGameTotalPlayer2 = 0

    for x in range(0, numberSets):  #repeats the process by number of sets inputed by user

        redPinCounts1 = random.randint(0,3) #how many red pins fall down player 1

        goldPinCounts1 = random.randint(0,2) #how many gold pins fall down player 1

        bluePinCounts1 = random.randint(0,5)#how many blue pins fall down player 1
    

        redPinCounts2 = random.randint(0,3)

        goldPinCounts2 = random.randint(0,2) 

        bluePinCounts2 = random.randint(0,5)
    

        finalPointsPlayer1 = computePoints(redPinCounts1, goldPinCounts1, bluePinCounts1) #this calculates how many points taking in how many pins were knocked down 

        finalPointsPlayer2 = computePoints(redPinCounts2, goldPinCounts2, bluePinCounts2) #same but for player 2 



        print("For SET:", numberSets) 

        print(player1Name, "has earned", finalPointsPlayer1, "points this set for:") #ouputs info to the user about who has points and who wins below

        print(goldPinCounts1, "gold pin(s) down,", redPinCounts1, "red pin(s) down,", bluePinCounts1, "blue pin(s) down")


        print(player2Name, "has earned", finalPointsPlayer2, "points this set for:")

        print(goldPinCounts2, "gold pin(s) down,", redPinCounts2, "red pin(s) down,", bluePinCounts2, "blue pin(s) down")

        
        endGameTotalPlayer1 += finalPointsPlayer1 #with every iteration of the loop finalPointsPlayer is the result fo the calculation and it adds 
        
        endGameTotalPlayer2 += finalPointsPlayer2

        numberSets -= 1 #sets go down until it reaches 0 and loop ends

        
    printWinner(endGameTotalPlayer1, endGameTotalPlayer2, player1Name, player2Name)

    print(endGameTotalPlayer1)

    print(endGameTotalPlayer2)




def computePoints(redPins,goldPins,bluePins):

    blueValue = 1 #value of the points 

    goldValue = 10

    redValue = 7

    bluePoints = blueValue * bluePins # calculate blue points multiply by how many blue pins 

    goldPoints = goldValue * goldPins

    redPoints = redValue * redPins

    totalPoints = bluePoints + goldPoints + redPoints

    return totalPoints



def printWinner(player1Points, player2Points, player1Name, player2Name):

    if player1Points > player2Points : #if player1 has more points they win
        
        print(player1Name, "wins")

    elif player1Points == player2Points: #if they have the same amount of points it's a draw

        print("Draw")

    else:

        print(player2Name, "wins") 

    
    

main()

