bad_characters = ["*", "!", "?", "#", "$", "%", "^", "&", "*","=", "+",]
count = 0

#declaring bad characters list and staring the count at the beginning 

empid_list_tmp = []
empname_list_tmp = []
emp_email_list_tmp = []
emp_address__tmp = []
emp_salary_tmp = []

#temporary lists to house input

#limiting issues to 4

emp_id_ok = False

while not emp_id_ok:
    emp_id = input("Please enter the employee ID: ")
    empid_list_tmp.append(emp_id)
    if emp_id:
        try:
                int(emp_id)
                if len(emp_id) <8:
                    print("Your employee ID is correct")
                    emp_id_ok = True
                else:
                    print("The employee ID is too long")
        except:
                print("The employee ID is invalid")
        else:
            exit("You did not enter an employee ID")
#emp id set to false because the ID has not been accepted yet
#while loop will run until the input is accepted, appending accepted input to temp list
#has to be an interger and seven digits or less, if correct message will appear. if too long else message will appear, if the character is bad excecpt message will appear
# if nothing is entered else message will appear

emp_name_ok = False

while not emp_name_ok:
    emp_name = input("Please enter the employees First and Last name: ").split(",")
    empname_list_tmp.append(emp_name)
    if emp_name:
        bad_characters_found = False
            
        for character in bad_characters:
            if character in emp_name:
                bad_characters_found = True

        if not bad_characters_found:
            print("the employees First and last name: " + str(emp_name) + "has been stored")
            emp_name_ok = True
        else:
            print("Your employees name contains unrecognized character and could not be stored")

#emp name set to false because the ID has not been accepted yet
#while loop will run until the input is accepted, appending accepted input to temp list. When accepted it will be split with a comma
#Looking for bad characters, if a bad character is found name will be rejected. If there are no bad characters found message will print. if too bad character appears a message will appear letting them know it could not be stored

emp_email_ok = False


while not emp_email_ok:
    emp_email = input("Please enter the employees email address: ")
    emp_email_list_tmp.append(emp_email)
    if emp_email:
        bad_characters_found = False
            
        for character in bad_characters:
            if character in emp_email:
                bad_characters_found = True

        if not bad_characters_found:
            print("the employees email address is: " + str(emp_email_ok) + "has been stored")
            emp_email_ok = True
        else:
            print("The employees email address contains unrecognized characters and could not be stored")   

#set to false, email has not been entered yet. asking for input, appending to temp list.  If a bad character is found the email address will be rejected.
#If theres is not a bad charter concatenated message will appear, if found else message will appear.

emp_address_ok = False

while not emp_address_ok:
        emp_address = input("please enter the employees address: ")
        emp_address__tmp.append(emp_address)
        if emp_address:
            bad_characters_found = False
            
            for character in bad_characters:
                if character in emp_address:
                    bad_characters_found = True

            if not bad_characters_found:
                print("the employees address has been stored")
                emp_address_ok = True
        else:
            print("The employees address contains unrecognized characters and could not be stored")

#Address not found yet, while loop looking for correct input to append to tmp list. cycling through looking for bad characters, if none found address will be stored, else the message cannot be stored
    

emp_salary_ok = False

while not emp_salary_ok:
    emp_salary = float(input("Please enter the employees salary: "))
    emp_salary_tmp.append(emp_salary)
    if emp_salary:
        try:
            float(emp_salary)
            if emp_salary >= 18 < 27:
                print("Your employee salary is accepted")
                emp_salary = True
            else:
                print("The employee salary is not between 18 and 27")
        except:
            print("The employee salary is invalid")
    else:
        exit("You did not enter an employee salary")
#set to false salary has not been found yet. floating number for salary that must be between 18 to 27, if it meets those criteria it will be accepted.
#If an not floating number is entered except message will appear, if nothing is entered else message will appear. 
         
count = count + 1 
#setting count to go one item after another


empid_list = []
empname_list = []
emp_email_list = []
emp_address = []
emp_salary = []

#creating real lists 

p = 0

#p will start at the beginning of each list and p += 1 move from one item to the next until the end and start over

for value in empid_list_tmp:
    if value not in empid_list:
        empid_list.append(value)
        empname_list.append(empname_list_tmp[p])
        emp_email.append(emp_email_list_tmp[p])
        emp_address.append(emp_address__tmp[p])
        emp_salary.append(emp_salary_tmp[p])

    p += 1 
#going through each item in the temp list that is not in the perm list. Empid_list p will start at 0 and go through each item one by one until the end of the list.
#The same will happen with the next four lists, the items will be appended bc of th [p] and it will go thorugh each item until it reaches the end and start over again at the beginning of the next list

emp_info = []

#new list that will contain the sorted info in dinctioaries 

i = 0

for value in empid_list:
    emp_info.append({
    "employee_id":value,
    "employee_name":empname_list[i],
    "employee email":emp_email[i],
    "emp address":emp_address[i],
    "emp salary":emp_salary[i],
    })

    i += 1
## the four loop will begin at 0 the first entry in the list, and will move forward 1 value at a time
# the perm lists are being appended to a new list with with a 5 key dictionary inside the list
# each key is being appended from 0 to the end moving one entry at a time 
#  a the final list for he emp information was created
# # Programmatically sorting the information into a list of dictionary items. Each dictionary must be in a database-like format.

for item in emp_info:
    item.update({"IT Department": item["updated salary"]* 1.3})

#adding IT Dept and multiplying each salary by 1.3


print(emp_info, end = '.....employee info.....\n')

#print statement with label 