1)Write Python program to implement crypt arithmetic problem TWO+TWO=FOUR



from itertools import permutations

def is_valid_assignment(assignment):
    t, w, o, f, u, r = assignment
    return 2 * (100 * t + 10 * w + o) == 1000 * f + 100 * o + 10 * u + r

def solve_cryptarithmetic():
    for perm in permutations(range(10), 6):
        assignment = {'T': perm[0], 'W': perm[1], 'O': perm[2], 'F': perm[3], 'U': perm[4], 'R': perm[5]}
        if assignment['T'] == 0 or assignment['F'] == 0:
            continue

        if is_valid_assignment(assignment):
            print("Solution found:")
            print(f"  T W O\n+ T W O\n-------\n  F O U R")
            print(f"  {assignment['T']} {assignment['W']} {assignment['O']}")
            print(f"+ {assignment['T']} {assignment['W']} {assignment['O']}")
            print("-------")
            print(f"  {assignment['F']} {assignment['O']} {assignment['U']} {assignment['R']}")
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()







Q2)Write a Python program to implement Simple Chatbot.




import random

def simple_chatbot():
    print("Hello! I'm a Simple Chatbot. You can type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you!")
        elif 'your name' in user_input:
            print("Chatbot: I'm just a simple chatbot.")
        elif 'joke' in user_input:
            jokes = [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What did one wall say to the other wall? I'll meet you at the corner.",
                "Why don't scientists trust atoms? Because they make up everything!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()

