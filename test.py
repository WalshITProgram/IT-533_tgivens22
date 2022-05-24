import re
fin_emp_list = []

run_program = True

while run_program:

    def emp_id( ):
        enter_id_ok = False
        while not enter_id_ok:
            enter_id = dict(input("Please enter the employee ID: "))
            fin_emp_list.append(enter_id)
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
emp_id()

