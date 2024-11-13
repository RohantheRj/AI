Q.1)Write a program to implement Hangman game using python. [10 Marks] Description: Hangman is a classic word-guessing game. The user should guess the word correctly by entering alphabets of the user choice. The Program will get input as single alphabet from the user and it will matchmaking with the alphabets in the original 



import random

def hangman():
    secret_word = random.choice(["python", "hangman", "programming", "computer", "science", "algorithm"])
    guessed_letters, attempts = set(), 6
    
    while attempts > 0 and set(secret_word) > guessed_letters:
        print("Current word:", ''.join(letter if letter in guessed_letters else '_' for letter in secret_word))
        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)
        attempts -= guess not in secret_word

    print(f"{'Congratulations!' if set(secret_word) <= guessed_letters else 'Sorry, you ran out of attempts. The word was: ' + secret_word}")

if __name__ == "__main__":
    hangman()








2))Write a Python program to implement Breadth First Search algorithm. Refer the following graph as an Input for the program.[Initial node=1,Goal node=8] 

BFS:

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]

    while queue:
        current_node, path = queue.pop(0)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [],
    6: [],
    7: [],
    8: []
}

# Specify the initial and goal nodes
initial_node = 1
goal_node = 8

# Run BFS and print the result
result = bfs(graph, initial_node, goal_node)

if result:
    print(f"BFS path from {initial_node} to {goal_node}: {result}")
else:
    print(f"No path found from {initial_node} to {goal_node}")