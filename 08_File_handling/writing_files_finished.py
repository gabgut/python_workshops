"""

Example file for writing files

"""

def main():
    file_name = 'writing_file_example.txt'

    # Writing to a file using write() method
    file = open(file_name, 'w')
    file.write("I'm writing to a file\n")
    file.write("If the file doesn't exits, the write() method creates it")
    file.close()

    # Writing to file using with statement
    with open(file_name, 'w') as file:
        file.write("Writing a file using with statement\n")
    file.close()

    # Working on append mode
    file = open(file_name, 'a')
    file.write("Adding text on append mode")
    file.close()

if __name__ == "__main__":
    main()