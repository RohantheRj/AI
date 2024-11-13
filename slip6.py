1)Write a python program to remove stop words for a given passage from a text file using NLTK?.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")

    try:
        passage = read_text_from_file(file_path)
        cleaned_passage = remove_stop_words(passage)

        print("\nOriginal Passage:")
        print(passage)

        print("\nPassage after Removing Stop Words:")
        print(cleaned_passage)
    except FileNotFoundError:
        print("File not found. Please check the file path.")








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






