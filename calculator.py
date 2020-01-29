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
