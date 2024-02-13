"""

Example file for exception handling

"""

import sys

# Exception when you try to divide by zero

dividend = 10
divisor = 0

try:
    quotient = dividend / divisor
except ZeroDivisionError:
    print("Error, you cannot divide by zero!")

# Exception when you apply an operator to an object of the wrong king
    
x = 5
y = "hello"

try:
    z = x + y
except TypeError:
    print("You cannot add a string to an integer!")  

# Catching exceptions (in general)  
    
list = [0, 1, 2]
length = len(list) + 1

try:
    for i in range(length):
        print(f"List element number {i} is {list[i]}")
except:
    print("An error ocurred!")

# Catching multiple and specific exceptions
    
def fun(a):
    if a < 4:
        b = a/(a-3)
    print(f"The value of b is {b}")

try:
    fun(3)    
    fun(5)
except ZeroDivisionError:    
    print(f"Division by zero ocurred but was handled")
except NameError:
    print("Name error ocurred but was handled")    

# Exceptions within a function

def div(a, b):
    try:
        c = ((a+b) / (a-b))
        print(f"c value is {c}")
    except ZeroDivisionError:
        print("You cannot divide by zero!")

div(2, 3)        
div(3, 3)

# You can add else statement on the try-except block

def div(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        print(f"c value is {c}")
        
div(2, 3)        
div(3, 3)

# Keyword finally for try-except clause

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.readlines()
            for line in data:
                word = line.split()
                print(word)
    except OSError:
        print("File not found or incorrect path!") 
    finally:
        print("The file could've been opened or not, but this part will be always excecuted")                   

read_file("file.txt") 

# Raising an exception

db = {'user1': 1234, 'user2': 1234}

def check_user(str):
    users = db.keys()
    if str not in users:
        raise NameError("Your user is not in the db")
    else:
        print(f"The user {str} is in the db")
    
str = input("Please enter your user: ")
check_user(str)    