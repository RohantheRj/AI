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




Q2) Write a Python program to implement Depth First Search algorithm. Refer the following graph as an Input for the program.[Initial node=2,Goal node=7] 



import sys
def dfs(graph, start,goal,visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print("Visited node:", start)
    if start==goal:
        sys.exit()
        
    for neighbor in graph[start]:
        
        
        if neighbor not in visited:
            dfs(graph, neighbor,goal,visited)
        

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}

# Specify the initial node
start_node = 1
goal_node =8
print("Depth First Search starting from node", start_node)
dfs(graph,start_node,goal_node)