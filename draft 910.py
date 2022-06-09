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

        
                

