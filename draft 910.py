import re             #importing regular expressions, to use with the name class to ensure input is the letters a-z lower or uppercase

class display_information:
    '''#repr - used to return a printable version of the object
       #will iterate through instances and update the dictionary with the results, using the name of the attributes as the key
    '''
    def __repr__(self):                                                     
        item = {}
        for key in self.__dict__:
            item.update({key: getattr(self,key)})
        return str(item)



class validator():
    '''#creating class - validator 
       class will make sure user input is valid, for the name, id, email
       the items that the student and teacher have in common. Each items has criteria that must be present or absent to be considered accurate
    '''
    def __init__(self):
        bad_characters = ['!', '"', "'", '#', '$',                    #list of prohibited characters for the email
                                '%', '^', '&', '*', '(', 
                                ')', '=', '+', ',', '<', 
                                '>', '/', '?', ';', ':', 
                                '[', ']', '{', '}','\\',
                         ]

        def bad_characters_check(characters_used, bad_characters_used):
            for character in characters_used:
                if character in bad_characters_used:
                    return True


#creating a function to check for bad characters, iterate through each character entered and if bad characters are found the function will be returned as true

        def valid_email():

            ''' valid email function - while true the user will enter the email address, the email address will have to match the format in the regular expression line. 
                if bad charcters from the bad characters check are found in the enter_email varibale a message will appear letting the user know invalid characters have been found.
                If no characters are found the function will be returned, if an email is not entered the invalid email format message will appear
            '''
            while True: 
                enter_email = input("Please enter the users email address: ")
                if re.match('[\S]+[@][\S]+[.]\w{2,3}$', enter_email):  
                    if bad_characters_check(enter_email, bad_characters):
                        print("Invalid bad characters found.")
                    else:
                        return enter_email
                else:
                    print("Invalid email format")



        def valid_name():

            ''' valid name function - while true the user will enter the name, the name will have to match the format in the regular expression line. 
                if bad charcters from the bad characters check are found in the print message will appear letting the user know invalid characters have been found.
                If no characters are found the function will be returned, if a name is not entered the invalid email format message will appear
            '''
            while True:   
                enter_name = input("Please enter name : ")
                if re.match("^[a-zA-Z][a-zA-Z '-]", enter_name):
                    if bad_characters_check(enter_name, bad_characters):
                        print("Invalid characters found.")
                    else:
                        return enter_name
                else:
                    print("Invalid name entered")

    
# 

        def valid_id():
            ''' function will aks for the user ID, the length of the ID will vary based on the user type.  
                if the length is correct and an integer the Id will be retured. 
                if incorrect messages will appear if the entry is too long, too short, or not an id 
                calling functions to generate id, email and name
            '''

            if self.__class__.__name__ == 'Student':
                max_ID_length = 7
            elif self.__class__.__name__ == 'Instructor':
                max_ID_length = 5
            while True:
                user_id = input('Please enter the user ID: ')
                if user_id :
                    try:
                        int(user_id )                              # The input must be an integer.
                        if len(user_id ) <= max_ID_length :         # The input needs to be less than the max id length.
                            return user_id                               
                        else:
                            print("The user ID is too long")
                    except:
                        print("The user ID is invalid")
                else:
                    exit("You did not enter an user ID")


        self.ID = valid_id()   
        self.email = valid_email()
        self.name = valid_name()



class student(validator,display_information): 
    ''' Class student - inheriting validator (name, id, and email) and display information (creating a printable objects to add to the library). 
        Calling itself first, role is student, initalizing the validator next, asking the student for their program of study
    '''

    def __init__(self): 
        self.role = 'Student'
        validator.__init__(self)  
        self.program_of_study = input('Please enter the program of study: ')                   
       
#class student - inheriting validator (name, id, and email) and display information (creating a printable objects to add to the library). 
# Calling itself first, role is student, initalizing the validator next, asking the student for their program of study

class instructor(validator,display_information):
    '''Class instructor - inheriting validator (name, id, and email) and display information (creating a printable objects to add to the library). 
       Calling itself first, role is instructor, initalizing the validator next, asking the instructor for last institution attended and highest degree obtained 
    '''

    def __init__(self):                     
        self.role = 'Instructor'
        validator.__init__(self)
        self.last_institution_they_graduated_from = input('Please enter the name of the last institution the Instructor graduated from: ') 
        self.highest_degree_attained = input('Please enter the highest degree attained by the Instructor: ')

#class instructor - inheriting validator (name, id, and email) and display information (creating a printable objects to add to the library). 
# Calling itself first, role is instructor, initalizing the validator next, asking the instructor for last institution attended and highest degree obtained 


def collect_ind_info():

    '''Asking if the user is a student or instructor
       Information will return accordingly based on the users answer
    ''' 

    while True:
        user_type = input("Is this a Student or Instructor: ")
        if user_type == 'Student':
            return student()
        elif user_type == 'Instructor' :
            return instructor()
        else:
            print("Please select Student or Instructor")


def keep_going(): 
    '''Asking the user to enter more employees by entering N to stop, or preesing any other key to continue
    '''
    kg = input('Would you like to enter more users? Answer "n" to stop. Press any other key to continue.')
    if kg == "n":
        print('Finished entering user information.')                          #if they press "n", the program will end and the list will print
        return False
    else:
        print('Please enter more users')                                      #if they press any key other than "n", the program will restart
        return True


college_records = []
run_program = True
while run_program:

    ind = collect_ind_info()

    if ind not in college_records:
        college_records.append(ind)

    run_program = keep_going()

print(college_records)
     

# Creating list - college records to hold dictionary entries. creating program to iterate thorugh each entry, if it is not already present it will be appended
# to college records
# calling the keep going function
#printing the list 




                

