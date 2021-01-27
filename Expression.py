
counter = 0 # this number will be increased until it reaches the value of N which stops the loop

n = int(input("Enter a value for n: " )) #user gives us the value o fn

finalResult = 0 #the final answer 

while counter <= n: #the code will repeat up until the number of times the user inputs

    myCalculation = counter / (counter + 1) #(for example 1/1+1 = 1/2)

    counter += 1  #counter goes up by one every time loop runs

    finalResult = finalResult + myCalculation #saves the result from this loop into a variable and its value goes up every time


print("the sum of ", n, "terms is %0.2f" % (finalResult)) 



