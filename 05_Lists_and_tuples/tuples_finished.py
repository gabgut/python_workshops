"""

Example files for tuples

"""

def main():
    # Creating a tuple
    t1 = (1, 2, 3)
    t2 = ("Hi", 2.5)
    t3 = tuple()

    print(t1, t2, t3)

    # Accessing tuples elements
    print(t1[0], t2[1])

    # Concatenating tuples
    t3 = t1 + t2
    print(t3)

    # Slicing a tuple
    print(t3[3:])
    print(t3[:3])

if __name__ == "__main__":
    main()