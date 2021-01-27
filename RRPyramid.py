import math 

class RRPyramid:

    pProcessed = 0

    nextID = 50 #since it goes up every time by 1 it's easier to start at 0 or 50 and then the numbers for each triangle are correct
    
    def __init__ (self, h = 0.0, l = 0.0, w = 0.0, pID = "51"): #Default values for each measurement 

        self.__height = h

        self.__length = l

        self.__width = w

        self.__pyramidId = pID

        RRPyramid.pProcessed += 1 #counts how many triangles have been calculated

        RRPyramid.nextID += 1  #counts id of each triangle
 
        
    def getPyramidId(self): #get variables enable user to access private variables indirectly

        return self.__pyramidId

    def getHeight(self):

        return self.__height
    
    def getLength(self):

        return self.__length

    def getWidth(self):

        return self.__width

    def setHeight(self, newHeight): #changes height of the pyramid entered by the user 

        self.__height = newHeight

    def calcSurfaceArea(self): #calculates total surface area taking the instance variables from above

        surfaceArea = self.__length * self.__width + self.__length * math.sqrt((self.__width/2)**2 + self.__height**2) + self.__width * math.sqrt(((self.__length/2)**2+ self.__height**2))

        return surfaceArea
        
    def calcVolume(self): #calculats volume taking instance variables 

        volume = (self.__length * self.__width * self.__height)/3

        return volume

    def __str__(self): #gives formated version of the second and third triangles

        space = " " * 4 

        return "Pyramid ID: " + str(RRPyramid.nextID) + "\n" + space + "Pyramid Height: " + str(self.__height) + " mm." + "\n" + space +  "Pyramid Length: " + str(self.__length) + " mm." + "\n" + space + "Pyramid Width: " + str(self.__width) + " mm.\n" + space + "The surface area is " + "%.2f " % (self.calcSurfaceArea()) + "cu.mm.\n" + space + "The volume is " + "%.2f " % (self.calcVolume()) + "cu.mm."+ "\n"

        
def main():

    firstPyramid = RRPyramid(10, 5, 5) #creates first object pyramid 

    print("Surface area and volume of pyramid with ID: 51") #gives information about the first pyramid

    print(" " *3, "The surface area is", "%.2f " % (firstPyramid.calcSurfaceArea()), "sq.mm." )

    print(" " *3,"The volume is", "%.2f " % (firstPyramid.calcVolume()),"cu.mm." ,"\n" )

    secondPyramid = RRPyramid(8, 4, 4)

    print(str(secondPyramid))

    secondPyramid.setHeight(20) #changes the height of the second pyramid 

    print("The updated surface area is", "%.2f " % (secondPyramid.calcSurfaceArea())  )

    print("The updated volume is","%.2f " % (secondPyramid.calcVolume()) , "\n" )
    
    thirdPyramid = RRPyramid(15, 3, 3) #creates third pyramid

    print(str(thirdPyramid)) #prints information third pyramid

    totalSurfaceArea = firstPyramid.calcSurfaceArea() + secondPyramid.calcSurfaceArea() + thirdPyramid.calcSurfaceArea() #calculates total surface area adding them all together

    print("The total surface area covered by all", RRPyramid.pProcessed, "pyramids is", "%.2f " % (totalSurfaceArea), "sq.mm." )
   
main()

