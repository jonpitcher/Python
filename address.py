
class Address:

    TotalNoOfAdd = 0  #total number of addresses  --every time new address "Happy street" goes up 
    NumOfAddWithApt = 0 #number of addresses with apartments  --- has to be more than 0 in an object total number... this depends on no of apartments

    def __init__(self, hNum= 0, st="st", cty = "Toronto", prov="Ontario", pCode= 68512, noOfApts = 0): #default values for instance variables 

        self.__HouseNumber = hNum
        self.__street = st
        self.__city = cty
        self.__prov = prov
        self.__postalCode = pCode
        self.__numberApartments = noOfApts #this is different for each apartment and should not increment.... 

        Address.TotalNoOfAdd += 1 #every time an object is created the amounto of addresses go up 

        if self.__numberApartments <= 1: #if the number is more than 0 then NumOfAddWithApt goes up 
            Address.NumOfAddWithApt += 1

    def getHouseNum(self):
        return self.__HouseNumber

    def getStreet(self):
        return self.__street 

    def setAptNos(self,apt):
        if self.__numberApartments == 0 and apt > 0: #this checks to see if the apartment already had an address or not 
            Address.NumOfAddWithApt += 1
        self.__numberApartments = apt #this changes the apartment number to the one inputed by the user in the main function 

    def __str__(self):
      
        return "Name and Street: " + str(self.__HouseNumber) + " " + self.__street + " \nCity, Province:  " + self.__city + "\nPostal Code: " + " "*4 +str(self.__postalCode) + "\nNumber of Apartments: " + str(self.__numberApartments) + "\n"

        #this prints of the formated version of the details of each address 
          
def main():

    object1 = Address(66, "Happy Street", "Happy Town", "NL", "A1A 1Z1", 1) #these create the four addresses 
    object2 = Address(15, "Catwalk Street", "Catalina", "NB", "C1C 3C3", 2)
    object3 = Address(33, "Peet Street", "Peterville", "ON", "A1A 2Z2")
    object4 = Address(20, "Berrybury Close", "Gooseberry", "NS", "A2A 2B2")

    print(str(object1))  #these print each address in turn
    print(str(object2))
    print(str(object3))
    print(str(object4))

    object1.setAptNos(3) #this changes the apartment number of the third address to 3 
    
    print(str(object1))

    object3.setAptNos(2)
    
    print(str(object3))

    print("The total number of addresses are:", Address.TotalNoOfAdd) #gives total using the class variables 

    print("The total number of addresses with apartments are:", Address.NumOfAddWithApt)

main()
