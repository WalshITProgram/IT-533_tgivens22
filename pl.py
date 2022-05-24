
def square_number(my_number):
      """Square a number provided by a user"""
      squared_number = my_number * my_number
      print("Your number squared is: " + str(squared_number))

my_number = input("Please input a number: ")
square_number(int(my_number))