

def main():

    codeInput = input("Please enter the code (or Done to terminate): ") #inputs letters from user 
        
    while codeInput != "Done": #continues loop until user stops loop by typing done 

        print("The code for this number is: ", codeInput)
        
        firstCode = isCorrect(codeInput) #checks to see if code in correct format 

        nonFormatedNumber = decodeCode(codeInput) #if code is valid format then turns it into numbers 

        printNum(nonFormatedNumber) #prints number in correct format 

        codeInput = input("Please enter the code (or Done to terminate): ")



def isCorrect(code):

    for x in code:

        ASCIIValue = ord(x) #gets the ASCII value of each letter in the code 

        if len(code) == 10 and ASCIIValue >= 65 and ASCIIValue <= 90: #determines if code is valid must be between 65 and 9 and 10 characters long

            return True 
       
        else:
        
            print("invalid code") #if code doesn't meet conditions above prints false 

            return False
        
    return True

def decodeCode(code):

    
    finalString = ""

    for x in code:

        if x == "q": #if it equals to q then x equals to zero

            x = "0" #equals to zero but needs to be a string to be able to concatenate correctly

            finalString = finalString + x #adds each time to create full final string 
        

        if x == "z":

            x = "1"
            
            finalString = finalString + x

            
        if x == "A" or x == "B" or x == "C": #this repeats for every letter in the alphabet 

            x = "2"
            
            finalString = finalString + x

            
        if x == "D" or x == "E" or x == "F":

            x = "3"
            
            finalString = finalString + x

            
        if x == "G" or x == "H" or x == "I":

            x = "4"
            
            finalString = finalString + x

            
        if x == "J" or x == "K" or x == "L":

            x = "5"
            
            finalString = finalString + x


        if x == "M" or x == "N" or x == "O":

            x = "6"
            
            finalString = finalString + x

            
        if x == "P" or x == "R" or x == "S":

            x = "7"
            

            finalString = finalString + x

        if x == "T" or x == "U" or x == "V":

            x = "8"
            
            finalString = finalString + x

            
        if x == "W" or x == "X" or x == "Y":

            x = "9"
            
            finalString = finalString + x


    return finalString #returns final string in number format 



def printNum(num):

    print(num[:3]+ "-" + num[3:6] + "-" + num[6:])  #outputs final code in telephone number format 

    

main()



      
