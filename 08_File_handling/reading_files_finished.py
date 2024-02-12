"""

Example file for reading files

"""

def main():
    file_name = 'read_file_example.txt'

    # Reading a file using open() method
    file = open(file_name, 'r')

    for line in file:
        print(line)

    # Extracting a string with read() method
    file = open(file_name, 'r')        
    print(file.read())

    # Reading a file using with statement
    with open(file_name) as file:
        data = file.read()

    print(data)

    # Reading mode characters wise
    file = open(file_name, 'r')
    print(file.read(7))

    # Splitting lines with split() method
    with open(file_name, 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            print(word)

if __name__ == "__main__":
    main()