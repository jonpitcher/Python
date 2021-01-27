




inputMaruvians = int(input("please enter the number of Maruvians ")) #Receives input from user to know how many of each kind of currency we have
inputCaruvians = int(input("please enter the number of Caruvians "))
inputTaruvians = int(input("please enter the number of Taruvians "))
inputParuvians = int(input("please enter the number of Paruvians "))

friends = int(input("please enter number of friends"))

MARVIN= 1 #Marvin is a constant one person, in this problem there will always be marvin

totalPeople= friends + MARVIN #Need to divide the amount by the number of friends and Marvin

maruvians = inputMaruvians * 24 #following three lines are the equivalents of each kind of currency

caruvians = inputCaruvians * 12

taruvians = inputTaruvians * 6

maruviansParuvianRatio= 24 

totalParuvians= maruvians + caruvians + taruvians + inputParuvians #All calculations done in paruvians to ensure there is no error while rounding 

totalMaruvians= totalParuvians/maruviansParuvianRatio 

shareFriends= totalMaruvians//totalPeople

remainderMaruvians= totalMaruvians % (totalPeople) 

remainderParuvians=  round((remainderMaruvians-(remainderMaruvians//1))*maruviansParuvianRatio)          

print("Marvin has", int(totalMaruvians) ,"Maruvians in total") #Since all numbers must be rounded int() is used to avoid having long decimal place and avoid rounding mistakes

print("He gives", int(shareFriends) ,"Maruvian(s) to himself and to each of his", friends, "friends")

print("Marvin puts", int(remainderMaruvians), "Maruvian(s) and", int(remainderParuvians),"Paruvian(s) back in the jar.")
