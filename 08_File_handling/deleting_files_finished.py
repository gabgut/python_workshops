"""

Example file for deleting files

"""

import os

def main():
    f_name_1 = 'writing_file_example.txt'

    # Deleting file using using remove method
    os.remove(f_name_1)

if __name__ == "__main__":
    main()