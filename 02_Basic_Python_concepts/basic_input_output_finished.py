"""

Exmple file of basic input/ouput

"""

def main():
    # Taking input from the user
    name = input("Enter your name: ")

    # Output
    print(f"Hello {name}")

    # Numeric input
    num = float(input("Enter a number: "))
    print(f"You entered {num}")

    # Taking multiple inputs of the same data type
    a, b, c = map(int, input("Enter the numbers separated by space: ").split())
    print(a, b, c)

    # Taking multiple inputs for a list (strings)
    inputs = input("Enter three days of the week separated by space: ").split()
    print(inputs)

    # Taking multiple inputs for a list (numbers)
    inputs = list(map(float, input("Enter the numbers separated by space: ").split()))
    print(inputs)

    # Taking multiple inputs for a list with finite amount of elements
    inputs = list()
    l = int(input("Enter the size of the list: "))
    print("Enter the list elements: ")
    for i in range(l):
        inputs.append(int(input()))
    print(inputs)

    # Taking input for a set (numbers)
    int_set = set(map(int, input("Enter numbers separated by space: ").split()))
    print(int_set)

    # Taking input for a set (numbers) with finite amount of elements
    inputs = set()
    s = int(input("Enter the size of the set: "))
    print("Enter the set elements: ")
    for i in range(s):
        inputs.add(int(input()))
    print(inputs)

    # Taking input for a tuple (strings)
    str_tuple = tuple(input("Enter elements separated by space: ").split())
    print(str_tuple)

    # Taking input for a tuple (numbers)
    num_tuple = tuple(map(float, input("Enter tuple numbers separated by space: ").split()))
    print(num_tuple)

if __name__ == "__main__":
    main()