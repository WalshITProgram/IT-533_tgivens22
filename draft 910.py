import re             #importing regular expressions, to use with the name class to ensure input is the letters a-z lower or uppercase

class display_information:

    def __repr__(self):                                                     #repr - used to return a printable version of the object
        item = {}
        for key in self.__dict__:
            item.update({key: getattr(self,key)})
        return str(item)

#  will iterate through instances and update the dictionary with the attributes, using the name of the attributes as the key

