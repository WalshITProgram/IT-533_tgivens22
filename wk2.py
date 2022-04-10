# 1. Stores your first name as a variable. Use all lowercase letters when you declare it.

first_name = "Thomas" #Storing first name as variable

print(first_name.lower()) #declaring in lower case letters

# 2. Stores your last name as a variable. Use all uppercase letters when you declare it.

last_name = "Givens"  #storing last name

print(last_name.upper())  #delcaring in upper case letters 

# 3.	Prints out, "Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.

print("Hello," +  " " + first_name.upper() + " " + last_name.lower())  # Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.

#4.	Prints out two newlines.

print(2* "\n")  

# 5.	Creates a new variable that stores your first and last name together with a space between both parts.

my_name = "Thomas" + " Givens"  #storing
print(my_name)                  #printing

#6.	Slices your last name from the variable you created in step 5 and prints it out. This must take place on one line. 

print(my_name[7:13])  #slicing last name from variable starts at 7 and ends at 13

# 7.	Replaces your last name in the variable you created in step 5 with "<your last name>, Walsh College Student"; print out the new value of this variable.

print(my_name.replace("Givens", "Givens, Walsh College Student")) #replacing last name 

# 8.	Prints out the following: "Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi" Your output must have quotes at the beginning and the end of your outputted text.

print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# 9.	Stores 2 decimal numbers as variables.

d1 = 1.25  #storing variables 

d2 = 2.50

#10 Stores one addition, one subtraction, one multiplication, and one division operation of these variables as variables.

a = d1 + d2   # addition

print("The addition results in: " + str(a))      # printing to check

s = d1 - d2   # subtraction

print("The subtraction results in: " + str(s))     # printing to check

m = d1 * d2   # multiplication

print("The multiplication results in: " + str(m))    # printing to check

di = d1 / d2  # div

print("The division results in: " + str(di))     # printing to check

#11 a Prints out each of the four results as: <numeric value of variable 1> plus <numeric value of variable 2> equals <value of variable that stored the result of addition>

print( str(1.25) + " plus" + " " + str(2.50)  + " equals : " + str(a))

#11 b <numeric value of variable 1> minus <numeric value of variable 2> equals <value of variable that stored the result of subtraction>
print (f'the value of variable 1 is {d1} minus the value of variable 2 {d2} equals {s}')

#11 c  <numeric value of variable 1> multiplied by <numeric value of variable 2> equals <value of variable that stored the result of subtraction>

x = 1.25  
y = 2.50
z = x*y
print(z)

# 12 sq root

import math  #importing math
sq_root = math.sqrt(3.125)  # sq rt vari
print(f"The sqaure root of" + " " + str(3.125) + " " + "equals" + " " +  str(sq_root))   # fstring




#13.	Stores the current month as a string variable (e.g. March, June, etc.) and day of the month as a numeric variable.

mon = "April"   #Stores the current month as a string variable

numb = 9 #day of the month as a numeric variable

# 14. Outputs "Today is day <day of month> of the month of <month variable>." This should be on a new line and tabbed over two times. You may pick your own method for displaying this information, but it should be different than the technique you used in step 12.

mess = "        Today is Day" + " " + str(numb) + " of the month" + " " + mon 

print(mess)
