#Program name: MO2 Lab - Case Study
#Author: Duncan Stephenson
#Date last updated: 01/24/2023
#Purpose: Accept student's names and use their
#GPA to determine if they are on the honor's or dean's list

Students = [["Last Name","First Name","GPA"]] #Creates list for students



while True: #While ZZZ isn't entered as last name the program loops
  print("Please enter a Student's Last name or ZZZ to quit") #prompts user for last name
  lastname = input(":")
  if lastname=="ZZZ": #ZZZ ends the program
      break
  else:
      #Any other last name leads to the first name being asked
      print (f"Please enter {lastname}\'s first name")
      firstname=input(":")
      #GPA is then asked for
      print(f"Please enter {firstname} {lastname}\'s GPA(Ex:3.10)")
      GPA = float(input(":")) #Stores GPA as float
      if GPA >= 3.25: #If the GPA is at least 3.25
          print("You made the honor roll!") #you are told you made honor roll
          if GPA >= 3.5: #If the GPA is also at least 3.5
            print("You also made the Dean's list!") #you are also told you made Dean's list
      #At the end of the loop iteration the student's info is added to the list    
      Students.append([lastname,firstname,GPA])  
# After the loop ends the Student list is sorted alphabetically       
Students[1:]=sorted(Students[1:])   
#Student list is printed as gradebook which
for gradebook in Students: #is in rows
    print(gradebook)  