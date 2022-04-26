# 1 Determine LTV

ltv = float(input("Enter a value for ltv:"))  #using the float data type for the non intergers
if ltv > int(79.99):                          # if statement, input more than 79.99 mortage insurance is required
    print("Mortgage Insurance is required")   # response for user

#  the following can be used to determine if mortgage insurance is required for a mortgage. If the loan to value (ltv) is greater than 79.99 than mortgage insurance is required
#  assigning a varible for the LTV, asking the user to enter the Ltv for their loan
#  if the LTV is greater than %79.99 then a message will appear letting them know its a requirement for the loan

#  2 monthly food budget

fah = 150            # assigning varible for food at the home 
foth = 52            # assigning varible for food outside the home
minc = 1000          # assigning varible for total monthly income

total_spent = (fah + foth)                       # assigning expression for total spent on food 

percsah = (fah/total_spent)                      # assigning expression total percentage spent on food at home

percsoth = (foth/total_spent)                    # assigning expression total percentage for food outside the home

print(total_spent)                               # each print statement will reveal a total or percent of budget to the user, or all at the same time.   

print(percsah)
print(percsoth)
print(total_spent/minc)

# 3 assignment list

assignments = ["week 1 Source Control Assignment", "week 2 Variables and Simple Object Types Assignment", "week 3 List, Dictionaries, and Files Assignment", "week 4 Assignments, Expressions, and Prints Assignment"]
assignments.append("week 5 If Statements Assignment")
print(assignments)

# assigned list, populated list.  This is a list so it is mutable and can be updated each week using the append function.  The print statement allows the user to view the list, they can also use the index or slice to pull certain assignments
# create a list of assignments and update using apprend as more assignments are given

# 4  Python can be used to select what to cook from dinner when you are being indecisive

import random  # module to generate random meals in print screen
list_of_meals = "baked chicken and green beans", "beef wellington", "tacos", "crabcakes and rice", "cobb salad", "swordfish and capers"
print(random.choice(list_of_meals))

# assigned tuple, populated tuple with meals
# This is a tuple with my favorite meals and used the random module to pick from the foods within the list. 
# The print statement will one of the choices from the tuple to the use randomly
# This is good for days when I cannot decide what to eat on my own.
# The meal choices cannot be changed so I have to make sure they were my favorites

# 5 Investment tracker

price_of_etherium = 3000              # assigned varible current price
num_of_shares = 900                   # assigned varible number of shares owned
price_when_purchased = 1700           # assigned varible price the shares were purchased at
target_price = 10000                  # assigned varible price the owner is looking to sale at

original_val = num_of_shares * price_when_purchased           # assigned expression amount spent to purchase shares

current_val = num_of_shares * price_of_etherium               # assigned expression amount made or lost based on current price

exit_price = target_price * num_of_shares                     # assigned expression amount the shares will be worth once Etherium hits the target price

print(original_val)                                           # print commands will show the original value vs the current value vs the value when it reaches their target price
print(current_val)
print(exit_price)

# this can be used to track an investment in Etherium. It can be modified if shares are bought or sold, and if the current price increases or decreases. They can also compare how much they have made or lost and possibly decide to sell early or hold past the target price





