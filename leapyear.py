
january = 31 #the variables determine how many days are in each month
normalFebruary = 28
leapYearFebruary= 29
march =	31
april =	30
may = 31
june = 30
july = 31
august = 31
september = 30
october	= 31
november = 30
december = 31

days= 0 #This number acts as a placeholder

randomOne= 0

month= int(input("Enter a month as an integer (1-12): "))
year = int(input("Enter a year "))    

#There is no convenient way to put the number of days in each month and the string value to be printed so the number is changed to a string 

if month == 1:
    days= january
    month= "January"
elif month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) : #this tests to see if the conditions are apt for a leap year if not it gives the normal value of February other years 
    days= leapYearFebruary
    month="February"
elif month==2:
    days= normalFebruary
    month="February"
elif month == 3:
    days= march
    month= "March"
elif month == 4:
    days= april
    month= "April"
elif month == 5:
    days= may
    month= "May"
elif month == 6:
    days= june
    month= "June"
elif month == 7:
    days= july
    month= "July"
elif month == 8:
    days= august
    month= "August"
elif month == 9:
    days= september
    month= "September"
elif month == 10:
    days= october
    month= "October"
elif month == 11:
    days= november
    month= "November"
elif month == 12:
    days= december
    month= "December"

print("There are", days, "days in", month, "of", year) 
   
    
