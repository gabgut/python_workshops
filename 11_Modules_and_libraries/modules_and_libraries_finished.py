"""

Example file for using modules

"""

# Math module

import math

# Math constants
print(f"Pi from math module: {math.pi}")
print(f"Euler's number from math module: {math.e}")
print(f"Tau constant from math module: {math.tau}")
print(f"Infinite representation from math module: {math.inf}")
print(f"Nan (not a number) from math module: {math.nan}")

# Common math functions
print(f"sin(pi): {math.sin(math.pi)}")
print(f"cos(pi): {math.cos(math.pi)}")
print(f"ln(e): {math.log(math.e)}")
print(f"log10(5): {math.log10(5)}")
print(f"log3(27): {math.log(27, 3)}")
print(f"Square root of 2: {math.sqrt(2)}")
print(f"3!: {math.factorial(3)}")
print(f"|-3|: {math.fabs(-3)}")
print(f"Euler's exponential of 3: {math.exp(3)}")
print(f"2 to the power of 3: {math.pow(2, 3)}")

# Random module

import random

# Gettign a random element from a list
list = [1, 2, 3, 4]
print(f"Random list element: {random.choice(list)}")

# Getting a random integer given an interval
print(f"Random int between 2 and 7: {random.randint(2, 7)}")

# Gettind a random float given an interval
print(f"Random float between 0 and 1: {random.random()}")

# Shuffling a list
random.shuffle(list)
print(f"Shuffled list: {list}")

# CSV mode

import csv

file_name = "/workspaces/python_workshops/11_Modules_and_libraries/example.csv"

# Writing to a csv file

fields = ['Instrument', 'Branch', 'Model', 'Price']
rows = [['Guitar', 'LTD', 'Arrow 200', '$925'],
        ['Guitar', 'G&L', 'Tribute Legacy', '$800']]

with open(file_name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# Reading a csv file
with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)