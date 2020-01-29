"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic


# Your code goes here
exit_condition_not_reached = True

while exit_condition_not_reached == True :
    entry = input("> ")
    tokens = entry.split(" ")
    if tokens[0] == 'q':
        exit_condition_not_reached = False

    if tokens[0] == '+':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.add(tokens1, tokens2))

    if tokens[0] == '-':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.subtract(tokens1, tokens2))

    if tokens[0] == '*':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.multiply(tokens1, tokens2))

    if tokens[0] == '/':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.divide(tokens1, tokens2))

    if tokens[0] == 'square':
        tokens1 = float(tokens[1])
        print(arithmetic.square(tokens1))

    if tokens[0] == 'cube':
        tokens1 = float(tokens[1])
        print(arithmetic.cube(tokens1))    

    if tokens[0] == 'pow':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.power(tokens1, tokens2))

    if tokens[0] == 'mod':
        tokens1 = float(tokens[1])
        tokens2 = float(tokens[2])
        print(arithmetic.mod(tokens1, tokens2))   