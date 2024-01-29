"""

Exmple file of functions

"""

# Defining and calling a function
def func1():
    print("My function")

func1()
print(func1())
print(func1)

# Function that takes argurments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

func2("hola", 123)
func2(arg1="hola", arg2=123)

# Function with return value
def square(num):
    return num ** num

pow = square(2)
print(pow)

# Function with variable number of non-keyword arguements
def addition(*args):
    result = 0
    for i in args:
        result += i
    return result    

add = addition(1, 2, 3, 4, 5)
print(add)

# Function with variable number of keyword arguements
def example_func(**kwargs):
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

example_func(name='Gabo', city='San Jose')

# Function with default value for an argument
def power(base, exp=1):
    print(base ** exp)

power(2)
power(2, 2)

# Defining return type and data type of arguments
def add_2_numbers(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

add_ints = add_2_numbers(3, 5)
print(f"result: {add_ints}, data type: {type(add_ints)}")

add_ints = add_2_numbers(3.4456, 5.1425)
print(f"result: {add_ints}, data type: {type(add_ints)}")

# Function scope and variable visibility
var = 0
print(var)

def myFunc1():
    var = 5
    print(var)

myFunc1()    
print(var)

def myFunc2():
    global var
    var = 1
    print(var)

myFunc2()
print(var)   

# Inner (or nested) functions
def f1():
    h = "Hello World!"
    def f2():
        print(h)
    f2()    

f1()

# Anonymous functions 

x = 3

cube = lambda x: x*x*x

print(cube(x))