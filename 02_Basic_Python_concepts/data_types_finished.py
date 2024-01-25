"""

Exmple file of data types

"""

def main():
    # Numeric data types
    a = 12
    print(f"a = {a}. Type of a is {type(a)}")

    b = 7.456
    print(f"b = {b}. Type of b is {type(b)}")

    c = 1 + 2j
    print(f"c = {c}. Type of c is {type(c)}")

    # Sequence data types
    s = "Hi! This is a string"
    print(f"s = '{s}'. Type of s is {type(s)}")

    l = ["Monday", "Tuesday", 123, "cat", 0 + 3j]
    print(f"l = {l}. Type of l is {type(l)}")

    t = ("dog", 10)
    print(f"t = {t}. Type of t is {type(t)}")

    # Boolean data types
    flag = True
    print(f"flag = {flag}. Type of flag is {type(flag)}")
    flag = False
    print(f"flag = {flag}. Type of flag is {type(flag)}")

    # Set data types
    Set = set("Client Computing Group")
    print(f"Set = {Set}. Type of Set is {type(Set)}")

    # Dictionary
    Dict = {1: 'Client', 2: 'Computing', 3: 'Group'}
    print(f"Dict = {Dict}. Type of Dict is {type(Dict)}")

    # Binary representation
    Bin = 0b00110
    print(f"Bin = {Bin}. Type of Bin is {type(Bin)}")

    Hex = 0xA2
    print(f"Hex = {Hex}. Type of Hex is {type(Hex)}")

    Oct = 0O20
    print(f"Oct = {Oct}. Type of Oct is {type(Oct)}")

    # "Null" type
    N = None
    print(f"N = {N}. Type of N is {type(N)}")


if __name__ == "__main__":
    main()