Q.1) Write a python program to remove punctuations from the given string? .[ 10 marks ] 

import string

def remove_punctuation(input_string):
    # Get the set of punctuation characters
    punctuations = set(string.punctuation)

    # Remove punctuations from the input string
    result_string = ''.join(char for char in input_string if char not in punctuations)

    return result_string

if __name__ == "__main__":
    input_string = input("Enter a string with punctuations: ")

    result = remove_punctuation(input_string)

    print("String without punctuations:", result)








2)Write a Python program for the following Cryptarithmetic problems. 

GO + TO = OUT

from itertools import permutations

def is_valid_assignment(assignment):
    g, o, t, u = assignment['G'], assignment['O'], assignment['T'], assignment['U']
    return g != 0 and t != 0 and (g * 10 + o + t * 10 + o == u * 100 + t * 10 + o)

def solve_cryptarithmetic():
    letters = ['G', 'O', 'T', 'U']
    digits = range(10)
    valid_assignments = []

    for perm in permutations(digits, len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            valid_assignments.append(assignment)

    return valid_assignments

def print_solutions(solutions):
    for solution in solutions:
        print("  {}{} + {}{} = {}{}".format(
            solution['G'], solution['O'],
            solution['T'], solution['O'],
            solution['O'], solution['U']
        ))

if __name__ == "__main__":
    print("Solving Cryptarithmetic Problem: GO + TO = OUT")
    
    solutions = solve_cryptarithmetic()

    if solutions:
        print("Valid solutions found:")
        print_solutions(solutions)
    else:
        print("No solution found.")
