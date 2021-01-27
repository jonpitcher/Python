from sys import exit

inputName = input("Enter the input file name: ") #asks user what file they want to get info from

try :
    inf = open(inputName, "r") #tests to see if file exists if it does it opens it
    
except :
    
    exit("File not found.") #if the file is not found reads file not found and ends program

outputName = input("Enter the ouput file name: ") #user decides what file output name is 

try : 
    outf = open(outputName, "w")

except :
    
    exit("error")

total = 0  #total to be calculated later starts at zero
 
print("%-15s %-12s %-12s %-12s " %("ISBN", "Cost","Copies","Total Cost")) #creates columns to organize info later

for line in inf :

    line = line.rstrip() #removes white spaces

    parts = line.split(",") #creates list dividing where there is a comma

    cost = float(parts[1])*int(parts[2]) #finds cost by multiplying two values from document together

    roundedCost = round(cost,2) #rounds cost to two digit dollar amount

    strRoundedCost = str(roundedCost) 

    print("%-15s %-12s %-12s %-12s " %(parts[0], parts[1], parts[2], strRoundedCost)) #prints info from document into columns

    total = total + cost #finds the total by adding to total every time for loop is run

    outf.write( str(parts[0]) + "," + str(parts[2])+ "," + str(cost) + "\n" ) #writes info to new document

print("\nThe total of all orders is:", "$%.2f " % total) #prints total cost of all orders

inf.close() #closes documents we have been working on

outf.close()



