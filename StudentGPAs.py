try:
    
    inFile = open("students.txt", "r") #opens file from which we will get information about students

    outFile = open("classGPA.txt", "w")

    print("%-15s %s " %("Student Num", "GPA"))

    aLine = inFile.readline() #reads the first line of the dcument

    while aLine != "" :  #program will run until lines are empty, end of document
    
        lineItems = aLine.rstrip().split(" ") #turns line into a list removing white spaces
    
        sumMarks = 0

        for i in range(2,7): #for loop prints of grades according to their position in an array
        
            sumMarks = sumMarks + float(lineItems[i]) #finds total of all grades 
        
        avg = sumMarks/5 #find the average by dividing the total of marks by how many marks 

        gpa = 4 #if GPA is not below averages in if statements below then it is 4
    
        if avg >= 65: # if statements determine what their GPA is accoding to the grading system
            gpa = 3 
        
        elif avg >= 55: 
            gpa = 2 
        
        elif avg >= 50: 
            gpa = 1
            
        elif avg < 50: 
            gpa = 0
    
        print("%-15s %-15d" %(lineItems[1], gpa)) #prints off information from document in console in python

        outFile.write("STNUM: " + lineItems[1] +" GPA: " + str(gpa) + "\n") #prints info into new document

        aLine = inFile.readline() #moves onto next line

    inFile.close() #closes the file 

    outFile.close() #closes the other file
    
except :  #if there is an error prints error and stops files from running
    print("error") 
