import re             #importing regular expressions, to use with the name class to ensure input is the letters a-z lower or uppercase

class display_information:

    def __repr__(self):                                                     #repr - used to return a printable version of the object
        item = {}
        for key in self.__dict__:
            item.update({key: getattr(self,key)})
        return str(item)

#  will iterate through instances and update the dictionary with the results, using the name of the attributes as the key

class validator():
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

#creating class - validator
#creating a function to check for bad characters, iterate through each character entered and if bad characters are found the function will be returned as true

        def valid_email():
            while True: 
                enter_email = input("Please enter the users email address: ")
                if re.match('[\S]+[@][\S]+[.]\w{2,3}$', enter_email):  
                    if bad_characters_check(enter_email, bad_characters):
                        print("Invalid bad characters found.")
                    else:
                        return enter_email
                else:
                    print("Invalid email format")

# valid email function - while true the user will enter the email address, the email address will have to match the format in the regular expression line. 
# if bad charcters from the bad characters check are found in the enter_email varibale a message will appear letting the user know invalid characters have been found.
# If no characters are found the function will be returned, if an email is not entered the invalid email format message will appear

        def valid_name():
            while True:   
                enter_name = input("Please enter name : ")
                if re.match("^[a-zA-Z][a-zA-Z '-]", enter_name):
                    if bad_characters_check(enter_name, bad_characters):
                        print("Invalid characters found.")
                    else:
                        return enter_name
                else:
                    print("Invalid name entered")

# valid name function - while true the user will enter the name, the name will have to match the format in the regular expression line. 
# if bad charcters from the bad characters check are found in the print message will appear letting the user know invalid characters have been found.
# If no characters are found the function will be returned, if a name is not entered the invalid email format message will appear              


                

