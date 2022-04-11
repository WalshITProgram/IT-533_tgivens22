# 1. Stores your first name as a variable. Use all lowercase letters when you declare it.

first_name = "Thomas" #Storing first name as variable

print(first_name.lower()) #declaring in lower case letters

# 2. Stores your last name as a variable. Use all uppercase letters when you declare it.

last_name = "Givens"  #storing last name

print(last_name.upper())  #delcaring in upper case letters 

# 3.    Prints out, "Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.

print("Hello," +  " " + first_name.upper() + " " + last_name.lower())   #concatenation hello, first name upper case last name lower case

#4. Prints out two newlines.

print(2* "\n")  

# 5.    Creates a new variable that stores your first and last name together with a space between both parts.

my_name = "Thomas" + " Givens"  #storing
print(my_name)                  #printing

#6. Slices your last name from the variable you created in step 5 and prints it out. This must take place on one line. 

print(my_name[7:13])  #slicing last name from variable starts at 7 and ends at 13

