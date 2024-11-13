Q.1) Write a python program to implement Lemmatization using NLTK



import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text

if __name__ == "__main__":
    input_text = input("Enter a sentence for lemmatization: ")

    lemmatized_result = lemmatize_text(input_text)

    print("\nOriginal Text:", input_text)
    print("Lemmatized Text:", lemmatized_result)








Q.2) Write a Python program to implement Breadth First Search algorithm. Refer the following graph as an Input for the program.[Initial node=1,Goal node=8]



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

