import re
import json



#run_program = True

#while run_program:

def emp_id( ):
        enter_id_ok = False
        while not enter_id_ok:
            enter_id = input("Please enter the employee ID: ")
            if enter_id:
                try:
                    int(enter_id)
                    if len(enter_id) <= 7:
                        print("Your employee ID is correct")
                        enter_id_ok = True
                    else:
                        print("The employee ID is too long")
                except:
                    print("The employee ID is invalid")
            else:
                exit("You did not enter an employee ID")


def emp_name():
    valid_name_entered = False
    while not valid_name_entered:
        ent_name = input('Enter name: ')

        if re.match("^[a-zA-Z][a-zA-Z '-]", ent_name):
            valid_name_entered = True
        else:
            print('Invalid characters found.')




def emp_email():
    bad_email_characters = ['!', '"', "'", '#', '$',
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
                print("the employees address has been stored")
                emp_add_ok = True
        else:
            print("The employees address contains unrecognized characters and could not be stored")
  



def e_salary():
    enter_salary_ok = False

    while not enter_salary_ok:
        enter_salary = float(input("Please enter the employees salary: "))
    
        if enter_salary:
            try:
                float(enter_salary)
                if 18 < float(enter_salary) < 27:
                    print("Your employee salary is accepted")
                    enter_salary = True
                else:
                    print("The employee salary is not between 18 and 27")
            except:
                 print("The employee salary is invalid")
        else:
            exit("You did not enter an employee salary")


fin_emp_list = []

unique_id = emp_id()
first_last = emp_name()
email = emp_email()
address = emp_address()
#salary =  e_salary()

print(unique_id)
#print(salary)

fin_emp_list.append({'unique_id': unique_id,
                     'first_last': first_last, 'email': email,
                     'address': address, #11'salary': salary
                   })

print(fin_emp_list)
'''def fin_dict():
    d = {}
    d['employee_id'] = emp_id
    d['name'] = emp_name
    d['email_address'] = emp_email
    d['address'] = emp_address
    d['salary'] = enter_salary
    fin_emp_list.append(d)
fin_dict()'''


'''def end_of_loop(kg):
    kg = input('Would you like to enter more employees\' information? Answer "N" to stop. Press any other key to continue.')
    if kg == "N":
        print('Finished entering employee information.')
        # Break the "while run_problem:" loop to stop asking for inputs if the user chooses not to enter more information.
        run_program = False
    else:
        # Continue the "while run_problem:" loop to ask for more inputs if the user decides to enter more information.
        print('Please enter more employee information')
(end_of_loop)


for employee in fin_emp_list:
    employee.update((key, str(employee[key]) + ' ' + 'IT Department') for key, value in employee.items() if key == "name")
    employee.update((key, float(employee[key]) * 1.3) for key, value in employee.items() if key == "salary")


json.dump(fin_emp_list, fp=open("Employee List.json", "w"))   #using dump to transfer list to json, the bottom line returns the entire file
print(open("Employee List.json").read())                     

#final = sales_data                                        #setting variable for list in
#json_string = json.dumps(final)    '''

               
    


            





  

 