"""

Example file for dictionaries

"""

def main():
    #Creating a dictionary
    d1 = {1: 'Val1', 2: 'Val2'}
    d2 = dict({'Key1': 1, 'Key2': 2})
    d3 = dict([(1, 'Val1'), (2, 'Val2')])
    d4 = {1: 'Val1', 2: [1, 2, 3]}
    List = [d1, d2, d3, d4]

    for idx, i in enumerate(List, 1):
        print(f"This is dictionary d{idx}")
        for key, value in i.items():
            print(f'{key}: {value}', end=' ')
        print()            

    # Accessing values of a dictionary
    print(f"Accessing element using d1 key: {d1[1]}")
    print(f"Accessing element using d2 key: {d2['Key1']}")

    # Accessing values of a dictionary using get method
    print(f"Accessing element using get method (d1): {d1.get(1)}")
    print(f"Accessing element using get method (d2): {d2.get('Key1')}")

    # Nested dicitonaries
    d5 = {1: 'Val1', 2: {'A': 1, 'B': 2}}
    d6 = {'d1': d1, 'd2': d2}
    print(d5)
    print(d6)

    # Accesing values of a nested dicitonary
    print(f"Accessing element d5 key: {d5[2]['A']}")

    for idx, i in enumerate(d6, 1):
        print(f"This key d{idx}")
        for ext_key, ext_value in d6[i].items():
            print(f'{ext_key}: {ext_value}', end=' ')
        print()

    # Adding elements to a dictionary 
    Dict = {}
    for i in range(3):
        Dict[i] = i

    Dict['CCG'] = "Client Computing Group"

    print(Dict)

    # Clear a dictionary
    print(f"d1 before clearing it: {d1}")
    d1.clear()
    print(f"d1 after clearing it: {d1}")

    # Copy a dictionary
    d1 = d2.copy()
    print(f"d1: {d1}, d2: {d2}")

    # Remove a element with the specific key
    print(f"d1 before removing element with 'Key1' key: {d1}")
    d1.pop('Key1')
    print(f"d1 after removing element with 'Key1' key: {d1}")

    # Remove the last inserted element
    print(f"Dict before removing last inserted element: {Dict}")
    Dict.popitem()
    print(f"Dict after removing last inserted element: {Dict}")

    # Get a list containing a tuple for each key-value pair
    print(d3.items())

    # Get a list of the keys
    print(f"d3 keys: {d3.keys()}")

    # Get a list of the values
    print(f"d3 values: {d3.values()}")

if __name__ == "__main__":
    main()