import re

#  1. Display Information
#Create a method that displays all collected information for an individual called "displayInformation".



#What type of individual we're dealing with (instructor or student)
#There will be an Instructor class and a Student Class (which should be pretty simple), 
# and your submission must use inheritance principles.
class gen_info:

    def __init__(self, name, email): 
        self.name = name
        self.email = email

class student(gen_info): 
    def __init__(self, name, email, student_ID, program_of_study):
        super().__init__(name, email)                                     #calling the init of the gen_info class, to use the name and email without repeating the code
        self.program_of_study = program_of_study
        self.student_ID = student_ID
       

class instructor(gen_info):
    def __init__(self, name, email, highest_degree_earned,last_institution_att,instructor_ID,):
        super().__init__(name, email)                                      #calling the init of the gen_info class, to use the name and email without repeating the code
        self.highest_degree_earned = highest_degree_earned 
        self.last_institution_att = last_institution_att
        self.instructor_ID = instructor_ID

# If the individual is a student, we need to get their Student ID (this is required, and must be a number that is 7 or less digits long)
#If the individual is an instructor, we need to get their Instructor ID (this is required, and must be a number that is 5 or less digits long)
#You must also create a class called "Validator" that has methods attached to it that validate submitted information.

class validator():
    def user_type(self):
        opti = 'Please select either "Student" or "Instructor"'
        while True:
            id = input("Please enter your ID: ")
            if opti == "Student":
                int(id)
                len(id) <= 7
                return id
            else:
                print("Please enter a valid ID")
            if opti == "Instructor":
                int(id)
                len(id) <= 5    	

                return id
            else:
                print("Please enter a valid ID")


#The individual's email address (this is required, and must be primarily comprised of alphanumeric characters. 
# It also cannot contain any of the following characters: ! " ' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \ ).
    def valid_email(self,email):
        while True:
            invalid_characters = ['"', "'", '@', '$', 
                              '%','^', '&', '*', 
                              '_', '=', '+', '<', 
                              '>', '?', ';',':', 
                              '[', ']', '{', '}'
                             ]
            enter_email = input("Please enter the employees email address: ")
            if re.match('[\S]+[@][\S]+[.]\w{2,3}$', enter_email,):
                for value in email:
                    if value in invalid_characters:
                        return False

#The individual's name (this is required, and must be primarily comprised of upper- and lower-case letters. 
# It also cannot contain any of the following characters: ! " @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \ ).
    def name_valid(self, name):
        """check if name is valid or not"""
        invalid = ['!', '"', "'", '#', '$',
                            '%', '^', '&', '*', '(', 
                            ')', '=', '+', ',', '<', 
                            '>', '/', '?', ';', ':', 
                            '[', ']', '{', '}','\\',
                           ]
        if not name.isalpha():
            return 0
        for value in name:
            if value in invalid:
                return 0
            return 1

#Write your program such that if a user inputs any of the above information incorrectly, 
# the program asks the user to re-enter it before continuing on. Your program should accept any 
# number of individuals until the person using the program says they are done.

            """if all the cases are passed"""


         '''def student_answers(self):
        stu_input = {'Name': self.name, 'Student ID': self.studentid, 'Degreeprogram:': self.degreeprogram, 'Email': self.email}  
        return stu_input 
        self.studentid = studentid
        self.degreeprogram = degreeprogram'''   
    
    def user_type(self):
        opti = 'Please select either "Student" or "Instructor"'
        while True:
            id = input("Please enter your ID: ")
            if opti == "Student":
                int(id)
                len(id) <= 7
                return id
            else:
                print("Please enter a valid ID")
            if opti == "Instructor":
                int(id)
                len(id) <= 5    	
                return id
            else:
                print("Please enter a valid ID")