
import math

price = 10.222222222
print("%.2f" % price) 
a= int(input("Enter an integer for a "))
p= int(input("Enter an integer for p "))
m1= int(input("Enter an integer for m1 "))
m2= int(input("Enter an integer for m2 "))
g= (4*pow(math.pi,2)*pow(a,3))/(pow(p,2)*(m1+m2))
print(" Value of G = %.2f " % (g)) 

