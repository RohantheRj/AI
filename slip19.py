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







2)Write a Python program to implement A* algorithm. Refer the following graph as an Input for the program.

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def astar(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current_node, path) = heapq.heappop(heap)

        if current_node in visited:
            continue

        path = path + [current_node]

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor, neighbor_cost in graph.graph[current_node].items():
            heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))

    return None

if __name__ == "__main__":
    # Example graph structure
    example_graph = Graph()
    example_graph.add_edge("A", {"B": 5, "C": 3})
    example_graph.add_edge("B", {"D": 2})
    example_graph.add_edge("C", {"D": 1})
    example_graph.add_edge("D", {"E": 4})

    start_node = "A"
    goal_node = "E"

    result = astar(example_graph, start_node, goal_node)

    if result:
        print(f"Optimal path from {start_node} to {goal_node}: {result}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")










