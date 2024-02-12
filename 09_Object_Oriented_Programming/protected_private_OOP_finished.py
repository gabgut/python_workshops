"""

Example file for OOP private/protected

"""

# Class protected and private attributes

class Base_class():
    # Class constructor
    def __init__(self):
        self._protected_attr = "protected"
        self.__private_attr = "private"

    # Get method
    def get_private_attr(self):
        return self.__private_attr
    

# Derived class
class Derived_class(Base_class):
    # Class constructor
    def __init__(self):
        super().__init__()

    # Method to access attr
    def access_protected_attr(self):
        return self._protected_attr
    

def main():
    # Creating object from derived class
    obj = Derived_class()

    # Accessing protected member
    print(obj.access_protected_attr())

    # Accessing private member -> Not recommended
    print(obj.get_private_attr()) 

if __name__ == "__main__":
    main()    