

while word != "zzz": #if you type zzz it will break the loop 

    word = input("Please enter a word (zzz to exit) : ")

    print("The original word is:", word) # just repeats the word the user inputed 

    print("The word without vowels is ", end="") #the following foor loop creates the word without vowels 

    for x in word:

        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y": #if the word contains these letters they will be replaced with * 
        
            print("*", end="") #if the condition is true it prints * 

        else:

            print(x, end="") #prints any letters that are not a,e,i,o,u
            
    print() #You need this print to create a space 





"""

 #for loop behaves differently with string vs numbers? numbers print as they get bigger string just prints off letters

            
#tried it even with 1 letter and says that x == a,e,i,o,u but I put only "w" doesn't make sense... 


#two loops because it needs to go through the word first to get individual letters then from there take each individual letters and run it...???

#it needs to be two loops because it needs to run the letter first....

#issue it's just printing all stars or all letters the if statement doesn't work properly...

#issue can print off the write word but it needs to be in a variable not sure how to do that with the for loop 


#why do i need a nested loop does it need to have two for loops but why see example

#i need two loops because one needs to do the if statement then the other needs to print...? 

#so I need to know if it equals a,e,i,o,u,y

#not supposed to use replace in this one... so do I need to break it down reconstruct it letter by letter/...?



string= "LLove"
uppercase = 0
for x in string :

print(x)


x=== the number

string === how many







adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry















"""
