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


def emp_name():
    valid_name_entered = False
    while not valid_name_entered:
        ent_name = input('Enter name: ')
        if re.match("^[a-zA-Z][a-zA-Z '-]", ent_name):
            valid_name_entered = True
            print("Your name is: " + ent_name)
            return ent_name
        else:
            print('Invalid characters found.')

#defining function for the employee name
#emp name set to false because the ID has not been accepted yet
#re.match function will o thorugh character to make sure the are letters between a and z, in lower or uppercase
#while loop will run until the input is accepted,  # returning the function back to the object to show its value,  after true boolen
#Looking for bad characters, if a bad character is found else message will appear






               


        





  

 