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
#re.match function will go through character to make sure the are letters between a and z, in lower or uppercase
#while loop will run until the input is accepted,  # returning the function back to the object to show its value,  after true boolen
#Looking for bad characters, if a bad character is found else message will appear


def emp_email():
    bad_email_characters = ['!', '"', "'", '#', '$',                    #list of prohibited characters for the email
                                '%', '^', '&', '*', '(', 
                                ')', '=', '+', ',', '<', 
                                '>', '/', '?', ';', ':', 
                                '[', ']', '{', '}','\\',
                           ]
    emp_email_ok = False
    while not emp_email_ok:
        enter_email = input("Please enter the employees email address: ")
        if re.match('[\S]+[@][\S]+[.]\w{2,3}$', enter_email):
            bad_email_characters_found = False
                        
            for character in bad_email_characters:
                if character in enter_email:
                    bad_email_characters_found = True

            if not bad_email_characters_found:
                emp_email_ok = True
                print("Email address entered is: " + enter_email)
                return enter_email
        else:
            print("The employees email address contains unrecognized characters and could not be stored") 

#defining function for the employee email. Emailed has not been entered yet. Asking for input, if a bad character is found the email address will be rejected. for loop will cycle through looking for bad characters, if there are none the loop store info and skip to next loop
#re.match used to ensure email address has the proper format, if the proper format is entered a message will appear showing the user what has been entered.  That input will be returned
# returning the function back to the object to show its value,  after true Boolean
#If there's is a bad charter else message will appear. 


def emp_address():
    bad_address_characters = ['"', "'", '@', '$', 
                              '%','^', '&', '*', 
                              '_', '=', '+', '<', 
                              '>', '?', ';',':', 
                              '[', ']', '{', '}'
                             ]

    emp_add_ok = False
    while not emp_add_ok:
        emp_home_add = input("please enter the employees address: ")
        if emp_home_add:
            bad_address_characters_found = False
            
            for character in bad_address_characters:
                if character in emp_home_add:
                    bad_address_characters_found = True

            if not bad_address_characters_found:
                print("The address entered is: " + emp_home_add)
                print("the employees address has been stored")
                emp_add_ok = True
                return emp_home_add
        else:
            print("The employees address contains unrecognized characters and could not be stored")

#Defining emp_address function  
#Address not found yet, while loop will review the input from user for bad characters. 
# If there are not any bad characters true variable will end loop and move onto the next and store the address, and return the function back to the object to show its value if not else message will appear.



def e_salary():
    
    while True:
        enter_salary = float(input("Please enter the employees salary: "))
    
        if enter_salary:
            try:
                float(enter_salary)
                if 18 < float(enter_salary) < 27:
                    return enter_salary
                      
                else:
                        print("The employee salary is not between 18 and 27")
            except:
                 print("The employee salary is invalid")
        else:
            exit("You did not enter an employee salary")

#Defining e_salary function
#set to false salary has not been found yet. floating number for salary that must be between 18 to 27, if it meets those criteria it will be accepted.  Returning the function back to the object to show its value
#If an not floating number is entered except message will appear, if nothing is entered else message will appear

fin_emp_list = []        # creating list to hold dictionaries

run_program = True        #Running program

while run_program:        #Setting protocol for program, to run loop until interrepted

    unique_id = emp_id()


    first_last = emp_name()


    email = emp_email()


    address = emp_address()


    salary =  e_salary()

#setting variables to call the functions for the id, name, email, address, and salary from the user input requested above.
#the variables will be appended to the dictionaires as keys, the information gathered from the functions above will be added to the corresponding keys
 
    fin_emp_list.append({'unique_id': unique_id,
                         'first_last': first_last, 'email': email,
                         'address': address, 'salary': salary
                       })


    
    kg = input('Would you like to enter more employees\' information? Answer "N" to stop. Press any other key to continue.')
    if kg == "N":
        print('Finished entering employee information.')
        # Break the "while run_problem:" loop to stop asking for inputs if the user chooses not to enter more information.
        run_program = False

    else:
        # Continue the "while run_problem:" loop to ask for more inputs if the user decides to enter more information.
        print('Please enter more employee information')


# Asking the user to enter more employees but entering N to stop, or preesing any other key to continue
#If the enter N the input request will stop, if they press any other key the program will start over at the id request


def comp_loop():
    for employee in fin_emp_list:
        employee.update((key, str(employee[key]) + ' ' + 'IT Department') for key, value in employee.items() if key == "first_last")
        employee.update((key, float(employee[key]) * 1.3) for key, value in employee.items() if key == "salary")
comp_loop()

#defining function for list comprehensions
#list comprehensions - adding IT department to the list under the name key. It will cycle thorugh each employee record and update the key that is == to name
# same as previous line expect its multiplying flotaing numbers by .3 under the emp_salary key

def js():
    json_file = open('C:/Users/THOMAS AND MONET/Desktop/programming 22/IT-533_tgivens22/IT-533_tgivens22/employee_data.json')
    json.dump(fin_emp_list, fp=open("employee_data.json", "w"))   #using dump to transfer list to json, the bottom line returns the entire file
    print(open("employee_data.json"))                    

    final = fin_emp_list                                        #setting variable for list in
    json_string = json.dumps(final) 
js()                         #dumping the list into json file as a string,


 # setting variable to dump infomation from final list into a json file #using dump to transfer list to json, the bottom line returns the entire file













               


        





  

 