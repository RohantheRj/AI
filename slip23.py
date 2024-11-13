1)Write a Program to Implement Tower of Hanoi using Python



def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg using target peg
        tower_of_hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary peg to target peg using source peg
        tower_of_hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))

    tower_of_hanoi(num_disks, 'A', 'C', 'B')









2)  Write a Python program for the following Cryptarithmetic problems SEND + MORE = MONEY 

from itertools import permutations

def is_valid_assignment(assignment):
    s, e, n, d, m, o, r, y = assignment['S'], assignment['E'], assignment['N'], assignment['D'], assignment['M'], assignment['O'], assignment['R'], assignment['Y']
    return s != 0 and m != 0 and (s * 1000 + e * 100 + n * 10 + d + m * 1000 + o * 100 + r * 10 + e == m * 10000 + o * 1000 + n * 100 + e * 10 + y)

def solve_cryptarithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    digits = range(10)
    valid_assignments = []

    for perm in permutations(digits, len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            valid_assignments.append(assignment)

    return valid_assignments

def print_solutions(solutions):
    for solution in solutions:
        print("  {}{}{}{} + {}{}{} = {}{}{}{}{}".format(
            solution['S'], solution['E'], solution['N'], solution['D'],
            solution['M'], solution['O'], solution['R'],
            solution['M'], solution['O'], solution['N'], solution['E'], solution['Y']
        ))

if __name__ == "__main__":
    print("Solving Cryptarithmetic Problem: SEND + MORE = MONEY")
    
    solutions = solve_cryptarithmetic()

    if solutions:
        print("Valid solutions found:")
        print_solutions(solutions)
    else:
        print("No solution found.")
