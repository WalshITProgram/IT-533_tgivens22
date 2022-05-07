#1
draft_list = [1121, "Jackie Grainger", 22.22,
1122, "Jignesh Thrakkar", 25.25,
1127, "Dion Green", 28.75, False,
24.32, 1132, "Jacob Gerber",
"Sarah Sanderson", 23.45, 1137, True,
"Brandon Heck", 1138, 25.84, True,
1152, "David Toma", 22.65,
23.75, 1157, "Charles King", False,
"Jackie Grainger", 1121, 22.22, False,
22.65, 1152, "David Toma"]


# creating list 

employee_id_tmp = []
employee_name_tmp = []
hourly_wage_tmp = []

# temp lists to store employee ids, names, and hourly wages from draft list that will be cleaned up in the next for loop
# these are temp lists becuase they still have the duplicates 

#2 
for item in draft_list:
    if type(item) is int:
        employee_id_tmp.append(item)
    elif type(item) is str:
        employee_name_tmp.append(item)
    elif type (item) is float:
        hourly_wage_tmp.append(item)

# for loop, varible declared is item. if "item" is an interger it will appended to employee_id_tmp
# if "item" is string it will be appended to name list
# if "item" is a floating number it wil be appended to hourly_wage_tmp
# true and false will be removed 
# permenant lists to store each object type without true false and duplicated items


employee_id = []
employee_name = []
hourly_wage = []



p = 0


for value in employee_id_tmp:
    if value not in employee_id:
        employee_id.append(value)
        employee_name.append(employee_name_tmp[p])
        hourly_wage.append(hourly_wage_tmp[p])
    p += 1 


# the p variable is telling the for loop to start at the beginning of the employee_id_tmp and append the updated list to employee id
# employee_name_tmp is being appended to employee_name starting at p
# hourly_wage_tmp is being appended to hourly wage starting at p
# p +=1 tells the four loop to move to the next item one at time

emp_info = []

i = 0
for value in employee_id:
    emp_info.append({
    "employee_id":value,
    "employee_name":employee_name[i],
    "hourly_wage":hourly_wage[i]
    })
    i += 1
   
# 3 the four loop will begin at 0 the first entry in the list, and will move forward 1 value at a time
# the perm lists are being appended to a new list with with a three key dictionary inside the list
# each key is being appended from 0 to the end moving one entry at a time 
#  a the final list for he emp information was created
# # Programmatically sorting the information into a list of dictionary items. Each dictionary must be in a database-like format.

underpaid_salaries = []

company_raises = []

#4
for item in emp_info:
    item.update({"total_hourly_rate": item["hourly_wage"]* 1.3})

#5
    if 28.15 < item["total_hourly_rate"] < 30.65:
        underpaid_salaries.append(item)

#6   
    if 22 <= item["hourly_wage"] < 24:
        company_raises.append({"employee_name":item["employee_name"], "hourly wage increase":item["hourly_wage"] *.05})
        if 24 >= item["hourly_wage"] < 26:
            company_raises.append({"employee_name":item["employee_name"], "hourly wage increase":item["hourly_wage"] *.04})
        if 26 >= item["hourly_wage"] < 28:
                company_raises.append({"employee_name":item["employee_name"], "hourly wage increase":item["hourly_wage"] *.03})
        else:
                company_raises.append({"employee_name":item["employee_name"], "hourly wage increase":item["hourly_wage"] *.02})




# 4 adding key to emp_info, the total hourly rate. the variable item will cycle through the list and each item will be multiplied by 1.3
# 5 salaries are being added to under_paid salaries if the are more than 28.15 and less than 30.65
# 6 if the hourly wage item is  =< 22 and > 24 it will be multiplied by .05 and added to company raises
# if the hourly wage item is  =< 24 and > 26 it will be multiplied by .04 and added to company raises
# if the hourly wage item is  =< 26 and > 28 it will be multiplied by .02 and added to company raises
# all of the items that dont fall into the ranges above will be mult by .02 and added to company raises
# Add to a new list called company_raises the name of the employee and the raise you calculated for each person. This information will be stored as a dictionary in database-like format. 


print(emp_info, end = '.....employee info.....\n')
print(underpaid_salaries, end = '.....underpaid salaries.....\n')
print(company_raises, end = '.....company raises.....\n')

#  printing the three final lists with custom line end to help tell when one ends and another begins







 
                                             
        