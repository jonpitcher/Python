
SMALL_BOX_MARKUP= .9 #Constant numbers that are assumed won't change

LARGE_BOX_MARKUP=.8

DISTRIBUTION_TOTAL_BARS= .5

COST_JUNE= .5

COST_JULY= 1

COST_AUGUST= .75

SMALL_BOXES_UNIT= 5

LARGE_BOXES_UNIT= 20


barsJune =  int(input("Enter the numbers of bars ordered in June ")) #Receives input from the user 

barsJuly = int(input("Enter the numbers of bars ordered in July "))

barsAugust = int(input("Enter the numbers of bars ordered in August "))


totalBars= barsJune+ barsJuly+ barsAugust #Beginning of processing mathematical figures

totalCost= barsJune*COST_JUNE + barsJuly*COST_JULY+ barsAugust*COST_AUGUST

smallBoxesCount= (totalBars*DISTRIBUTION_TOTAL_BARS)//SMALL_BOXES_UNIT

largeBoxesCount= (totalBars*DISTRIBUTION_TOTAL_BARS)//LARGE_BOXES_UNIT


smallBoxPrice= (totalCost/totalBars*SMALL_BOXES_UNIT) 

smallBoxPriceWithMarkUp= (smallBoxPrice*SMALL_BOX_MARKUP)+ smallBoxPrice


largeBoxPrice= totalCost/totalBars*LARGE_BOXES_UNIT

largeBoxPriceWithMarkUp= (largeBoxPrice*LARGE_BOX_MARKUP)+ largeBoxPrice


print("Number of Small Boxes packed: %.f " % (smallBoxesCount) ) #Displays final calculations keeping in mind the need to limit decimals

print("Number of Large Boxes packed: %.f " % (largeBoxesCount) )

print("Selling Price Per Small Box: $ %.2f " % (smallBoxPriceWithMarkUp) )

print("Selling Price Per Large Box: $ %.2f " % (largeBoxPriceWithMarkUp))


