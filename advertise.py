
class Advertisement:

    totalNumOfAds = 0

    adNum = 100

    def __init__(self, prime = "F", duration = 0, adId = "100AA" ): #these are the default values for the variables if none are entered 

        self.__adPrime = prime
    
        self.__duration = duration
    
        self.__adId = adId

        self.__finalCost = 0

        self.computeAdCost() #the cost of the add will be determined automatically each time the object is made 

        Advertisement.totalNumOfAds += 1

        Advertisement.adNum += 1 #this makes the add Number go up every time with the creation of each object 


    def computeAdCost(self):

        basicCost = 1000

        if self.__adPrime == "T": #if they do have a prime time the cost increases by 5000 

            initialCalculation = basicCost + 5000 + (1500* self.__duration)

            taxes = initialCalculation * .15

            self.__finalCost = initialCalculation + taxes

            return self.__finalCost


        elif self.__adPrime == "F":

            initialCalculation = basicCost + 1500 * self.__duration

            taxes = initialCalculation * .15 #to calculate the taxes you must multiply it by 15 percent 

            self.__finalCost = initialCalculation + taxes

            return self.__finalCost
        
    def getAdPrime(self): #this returns the private variable 

        return self.__adPrime

    def getDuration(self):

        return self.__duration

    def getAdId(self):

        return self.__adId

    def __str__(self):

        return "Advertisement" + "\n" + "ID: " + str(Advertisement.adNum) + str(self.__adPrime) + str(self.__duration)  + "%18s " % ( "Total Cost: " )+ "$" + "%.2f " % (self.__finalCost) + "\n"

        
def main():

    firstAd = Advertisement("T", 3) #this creates the first object, the first ad 

    print(str(firstAd)) #this prints off the modified version of the str method 

    secondAd = Advertisement("F", 6)

    print(str(secondAd))

    print("The total number of ads are", Advertisement.totalNumOfAds , ".")


main()



 
