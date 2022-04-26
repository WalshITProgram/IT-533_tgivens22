ltv = float(input("Enter a value for ltv:"))  #using the float data type for the non intergers
if ltv > int(79.99):                          # if statement, input more than 79.99 mortage insurance is required
    print("Mortgage Insurance is required")   # response for user

#  the following can be used to determine if mortgage insurance is required for a mortgage. If the loan to value (ltv) is greater than 79.99 than mortgage insurance is required
#  assigning a varible for the LTV, asking the user to enter the Ltv for their loan
#  if the LTV is greater than %79.99 then a message will appear letting them know its a requirement for the loan

#  monthly food budget

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
