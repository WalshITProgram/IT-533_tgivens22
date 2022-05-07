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

employee_id = []
employee_name = []
hourly_wage = []

# permenant lists to store each object type without true false and duplicated 

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










 
                                             
        