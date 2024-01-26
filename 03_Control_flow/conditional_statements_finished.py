"""

Exmple file of conditional statements

"""

def main():
    # If-else statements
    num = int(input("Enter a number: "))
    if (num > 5):
        print("The number is bigger than 5")
    else:
        print("The number is smaller than 5")

    #If-elif-else statements
    num = int(input("Enter a number: "))
    if (num > 5):
        print("The number is bigger than 5")
    elif (num == 5):        
        print("The number is equal to 5")
    else:
        print("The number is smaller than 5")

    # Nested if-else statementd
    num = int(input("Enter a number: "))
    if (num > 5):
        if (num == 10):
            print("The number is bigger than 5, and it's 10")
        else:
            print("The number is bigger than 5")    
    elif (num == 5):        
        print("The number is equal to 5")
    else:
        print("The number is smaller than 5")   

    # If-else statement with list comprehension
    even_numbers = [i if i % 2 == 0 else "odd" for i in range(10)]                  
    print(even_numbers)

    # Short if statement
    num = int(input("Enter a number: "))
    print("Number is bigger or equal than 5") if num >= 5 else print("Number is smaller than 5")

if __name__ == "__main__":
    main()