"""

Example file for OOP

"""

import random

# Creating a class

class Pokemon():
    # Class constructor
    def __init__(self, hp, atk, defense, sp_atk, sp_def, speed):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.types = {'type1': None, 'type2': None}

    # Class methods
    def total_stats(self):
        total_stats = 0
        for attr_name, attr_value in vars(self).items():
            if attr_name != "types":
                total_stats += attr_value
        print(f"Pokemon total stats is {total_stats}")

    def set_types(self, type1="normal", type2=None):
        self.types['type1'] = type1
        self.types['type2'] = type2

    def show_types(self):
        print(f"Pokemon types are {self.types['type1']} and {self.types['type2']}")


# Creating a derived class
class Pikachu(Pokemon):
    # Class constructor (attributes inherited)
    def __init__(self, hp, atk, defense, sp_atk, sp_def, speed):
        Pokemon.__init__(self, hp, atk, defense, sp_atk, sp_def, speed)

    # Overridden methods with Polymporphism
    def total_stats(self):
        total_stats = 0
        for attr_name, attr_value in vars(self).items():
            if attr_name != "types":
                total_stats += attr_value
        print(f"Pikachu total stats is {total_stats}")    

    def show_types(self):
        print(f"Pikachu's type is {self.types['type1']}")


def main():
    # Creating object (class instance)
    pikachu1 = Pokemon(35, 55, 40, 50, 50, 90)

    # Calling class methods
    pikachu1.total_stats()
    pikachu1.show_types()
    pikachu1.set_types("electric")
    pikachu1.show_types()

    # Creating object from derived class
    pikachu2 = Pikachu(35, 55, 40, 50, 50, 90)

    # Calling overridden methods
    pikachu2.total_stats()
    pikachu2.show_types()

    # Calling inherited method
    pikachu2.set_types("electric")
    pikachu2.show_types()

if __name__ == "__main__":
    main()