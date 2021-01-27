
totalPackageWeight = 0 #necessary to have total weight since user inputs individual weights to avoid confusion

packagesEastZone = 0 #these vowels are set from the beginning to give an initial value but serve as placeholders until user inputs data 

packagesWestZone = 0

packagesNorthZone = 0

packagesSouthZone = 0

totalNumberPackages = 0 

                                                                                           

while totalPackageWeight <= 1000:
    
    individualWeight = int(input("Please enter the weight of a package: ")) 

    totalPackageWeight = totalPackageWeight + individualWeight  #with each time it adds the weight entered by user and each time adds to the total weight 

    if totalPackageWeight > 1000: #this is to avoid the code running an additional time since it runs the entire code before it checks the weight again
        break
    
    
    int(input("Please enter the package ID number: "))

    packageZone = input("Please enter the zone: ")

    totalNumberPackages = totalNumberPackages + 1   #Every time you enter a package total packages go up 



    if packageZone == "east" or packageZone == "East":                                      

        packagesEastZone = packagesEastZone + 1 #this code repeats multiple times if the input is east, west etc. it increases the variable for east region by one to count how many packages are sent
        
         
    elif packageZone == "west" or packageZone == "West":
        
         packagesWestZone = packagesWestZone + 1
         

    elif packageZone == "north" or packageZone == "North":
        
         packagesNorthZone = packagesNorthZone + 1

         
    elif packageZone == "south" or packageZone == "South":
        
         packagesSouthZone = packagesSouthZone + 1
    
        
  
    print("total package weight is", totalPackageWeight)
    
    print("The following package is on the truck:  Pkg No.=", packageIdNumber, "Zone =", packageZone, "Pkg Wgt =", totalPackageWeight)

   

print(packagesEastZone, "packages are on the truck for the East zone")  #gives final amount tallied from how many 

print(packagesWestZone, "packages are on the truck for the West zone")

print(packagesNorthZone, "packages are on the truck for the North zone")

print(packagesSouthZone, "packages are on the truck for the South zone")

print(totalNumberPackages, "packages are loaded on the truck") 








"""
