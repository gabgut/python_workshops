"""

Exmple file of loops structures

"""

def main():
    # While loop
    counter = 0
    while (counter < 5):
        print(f"{counter} ")
        counter += 1

    # While loop with else statement
    counter = 0
    while (counter < 5):
        print(f"{counter} ")
        counter += 1
    else: 
        print("Entering else block")  

    # Infite while loop (Uncomment next 
    # lines to see example)    
    
    """
    # Infinite while loop
    while (True):
        print("Infinite loop")
    """    

    # For loop
    n = 5
    for i in range(n):
        print(f"{i} ")

    # For loop to iterate a string
    s = "Hello World!"        
    for i in s:
        print(i)

    # For loop iterating a list
    l = ["Client", "Computing", "Group"]        
    for i in l:
        print(i)

    # For loop iterating a tuple
    t = ("Client", "Computing", "Group")        
    for i in t:
        print(i)

    # For loop to iterate a dictionary
    d = {"key1": 1, "key2": 2}
    for i in d:
        print(f"key = {i}, value = {d[i]}")  

    # For loop to iterate a set
    s = {1, 2, 3, 4}          
    for i in s:
        print(i)

    # Iterating by the index of the sequence
    for i in range(len(l)):
        print(l[i])

    # For loop with else statement
    for i in range(n):
        print(f"{i} ")
    else:
        print("Entering else statement")

    # Nested for loop
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()       

    # Nested while loop
    i, j = 0, 0
    while (i < len(matrix)):
        while (j < len(matrix[i])):
            print(matrix[i][j], end='\t')
            j += 1
        i += 1    
        j = 0
        print()        

    """
    Loop control statements:
    - continue
    - break
    - pass   
    """

    s = "Hello World!"  

    # Continue statement
    vocals = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vocals:
            continue
        else:
            print(i)      
    
    # Break statement
    for i in s:
        if i in vocals:
            break
        else:
            print(i)    

    # Pass statement
    for i in s:
        pass                          
    print(f"Last letter/character: {i}")   

    # How iterators really work

    days = ["Mon", "Tue", "Wed"] 
    for day in days:
        print(day)

    iter_obj = iter(days)    
    while True:
        try:
            day = next(iter_obj)
            print(day)
        except StopIteration:
            break


if __name__ == "__main__":
    main()