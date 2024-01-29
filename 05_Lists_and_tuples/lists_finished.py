"""

Example files for lists

"""

def main():
    # Creating a list
    l1 = [1, 2, 3]
    l2 = [1, "Mon", 2, "Tues"]
    l3 = []
    l4 = list()

    print(l1, l2, l3, l4)

    # Accesing elements from a list
    print(l1[0], l2[2])

    # Creating and accesing multi-dimensional list
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(matrix[2][1])

    # Negative indexing
    print(l1[-1], l1[-3])

    # Getting the size of a list
    print(len(l1))

    # Adding elements to a list
    l3.append(10)
    l3.append(20)

    print(l3)

    # Adding elements to a list using an iterator
    for i in range(5):
        l4.append(i)
    print(l4)

    # Adding a tuple to a list
    l4.append((1, 2, 3))

    print(l4)

    # Adding a list to a list
    l4.append(l2)

    print(l4)

    # Inserting elements in a list
    l4.insert(1, (1, 2))

    print(l4)

    # Adding elements to a list using extend method
    l3.extend([2, "Hi", [5, 6, 7]])

    print(l3)

    # Reversing a list using reverse method
    l3.reverse()

    print(l3)

    # Reversing a list using reversed method
    reversed_l4 = list(reversed(l4))

    print(reversed_l4)

    # Removing element from a list with remove method
    l4.remove(0)
    l4.remove(l2)

    print(l4)

    # Removing element from a list with pop method
    l4.pop()
    print(l4)

    l4.pop(0)
    print(l4)

    # Slicing a list
    print(f"Elements from beginning to a range: {l3[:3]}")
    print(f"Elements from specific index: {l3[3:]}")

    # List comprenhension
    even_number = [i for i in range(15) if i % 2 == 0]
    print(even_number)

    even_number = []
    for i in range(15):
        if i % 2 == 0:
            even_number.append(i)
    
    print(even_number)

if __name__ == "__main__":
    main()