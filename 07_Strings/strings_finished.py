"""

Example file for strings

"""

def main():
    # Creating a string with single quotes
    str1 = 'This is a string created with single quotes'

    # Creating a string with double quotes
    str2 = 'This is a string created with double quotes'

    # Creating a string with triple quotes
    str3 = """
           This is a 
           string created 
           with triple quotes
           """
    
    str_list = [str1, str2, str3]
    for i in str_list:
        print(i)

    # Accessing characters from a string
    short_str = "Banana"
    print(f"short_str character 0: {short_str[0]}")
    print(f"short_str character 0: {short_str[2]}")
    print(f"short_str character -1: {short_str[-1]}")

    for i in short_str:
        print(f"{i}", end=' ')
    print()

    j = -1
    while (j >= -1*len(short_str)):
        print(f"{short_str[j]}", end=' ')
        j -= 1
    print()

    # String slicing
    print(f"Slicing short_str characters from 1-3: {short_str[1:3]}")

    # Reversing a string
    print(f"Reversing string with string slicing: {short_str[::-1]}")
    reversed_short_str = "".join(reversed(short_str))
    print(f"Reversing string using join and reversed methods: {reversed_short_str}")

    # Updating an entire string
    str1 = "Hello"
    print(str1)

    # Updating a character from a string
    list1 = list(str1)
    list1[0] = 'J'
    str1 = ''.join(list1)
    print(str1)

    str1 = 'H' + str1[1:]
    print(str1)

    # Formatting a string by default order
    form_str = "{} {}".format('This is', 'a string')
    print(form_str)

    # Formatting a string by positional formatting
    form_str = "{1} {0}".format('This is', 'a string')
    print(form_str)

    # Formatting a string by keyword arguement
    form_str = "{key1} {key2}".format(key1='This is', key2='a string')
    print(form_str)

    # String concatenation
    conc_str = str1 + ' ' + str2
    print(conc_str)

    # String multiplication
    rep_str = str1 * 2
    print(rep_str)

    # Getting string length
    print(f"rep_str length: {len(rep_str)}")

if __name__ == "__main__":
    main()