import re   #importing regular expression to match the string input for the name input

emp_info = []      #blank list to be used later, global variable

run_program = True   #  setting value of run program to true, so it will run until the user chooses to stop

while run_program:     #setting rules during the use of the program

    emp_id_ok = False

    while not emp_id_ok:
        emp_id = input("Please enter the employee ID: ")
        if emp_id:
            try:
                int(emp_id)
                if len(emp_id) <= 7:
                    print("Your employee ID is correct")
                    emp_id_ok = True
                else:
                    print("The employee ID is too long")
            except:
                print("The employee ID is invalid")
        else:
            exit("You did not enter an employee ID")
#emp id set to false because the ID has not been accepted yet
#while loop will run until the input is accepted
#has to be an interger and seven digits or less, if correct message will appear. if too long else message will appear, if the character is bad excecpt message will appear
# if nothing is entered else message will appear

    valid_name_entered = False
    while not valid_name_entered:
        name = input('Enter name: ')

        if re.match("^[a-zA-Z][a-zA-Z '-]", name):
            valid_name_entered = True
        else:
            print('Invalid characters found.')

#emp name set to false because the ID has not been accepted yet
#re.match function will o thorugh character to make sure the are letters between a and z, in lower or uppercase
#while loop will run until the input is accepted,
#Looking for bad characters, if a bad character is found else message will appear


    bad_email_characters = ['!', '"', "'", '#', '$',           #list of prohibited characters for the email
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
        else:
            print("The employees email address contains unrecognized characters and could not be stored")  

#set to false, email has not been entered yet. asking for input.  If a bad character is found the email address will be rejected. for loop will cycle through looking for bad characters, if there are none the loop store info and skip to next loop
#re.match used to ensure email address has the proper format
#If theres is a bad charter else message will appear. 


    bad_address_characters = ['"', "'", '@', '$',          #list of prohibited characters for the address
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
                print("the employees address has been stored")
                emp_add_ok = True
        else:
            print("The employees address contains unrecognized characters and could not be stored")
  

#Address not found yet, while loop will review the input from user for bad characters. If there are not any bad characters true variable will enf loop and move onto the next and store the address, if not else message will appear 
    
    emp_sal_ok = False

    while not emp_sal_ok:
        emp_salary = float(input("Please enter the employees salary: "))
        if emp_salary:
            try:
                float(emp_salary)
                if 18 < float(emp_salary) < 27:
                    print("Your employee salary is accepted")
                    emp_sal_ok = True
                else:
                    print("The employee salary is not between 18 and 27")
            except:
                 print("The employee salary is invalid")
        else:
            exit("You did not enter an employee salary")
    
#set to false salary has not been found yet. floating number for salary that must be between 18 to 27, if it meets those criteria it will be accepted.
#If an not floating number is entered except message will appear, if nothing is entered else message will appear. 






