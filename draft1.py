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








