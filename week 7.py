import re   #importing regular expression to match the string input for the name input
import json   #importing json

def emp_id( ):
    enter_id_ok = False
    while not enter_id_ok:
        enter_id = input("Please enter the employee ID: ")
        if enter_id:
            try:
                int(enter_id)                 # The input needs to be digits.
                if len(enter_id) <= 7:         # The input needs to be less than 7 digits.
                    print("Your employee id is: " + enter_id)
                    print("Your employee ID is correct")
                    enter_id_ok = True           # Break the loop if the input is a number of 7 or less digits long.
                    return enter_id
                else:
                        print("The employee ID is too long")
            except:
                print("The employee ID is invalid")
        else:
            exit("You did not enter an employee ID")
#defining function for the employee id
#emp id set to false because the ID has not been accepted yet
#while loop will run until the input is accepted
#has to be an integer and seven digits or less, if correct message will appear. if too long else message will appear, if the character is bad except message will appear
# returning the function back to the object to show its value,  after true Boolean
# if nothing is entered else message will appear









               


        





  

 