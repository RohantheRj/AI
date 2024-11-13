Write a python program to remove stop words for a given passage from a text file using NLTK?. [

Install NLTK if you haven't already:

((bash
Copy code
pip install nltk
Create a text file with the passage.

Use the following Python program:))


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        passage = file.read()

    stop_words = set(stopwords.words('english'))
    words = word_tokenize(passage)

    filtered_words = [word for word in words if word.lower() not in stop_words]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(" ".join(filtered_words))

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with the path to your input text file
    output_file = "output.txt"  # Replace with the desired output file path

    remove_stop_words(input_file, output_file)





 2))Implement a system that performs arrangement of some set of objects in a room. Assume that you have only 5 rectangular, 4 square-shaped objects. Use A* approach for the placement of the objects in room for efficient space utilisation. Assume suitable heuristic, and dimensions of objects and rooms. (Informed Search)





import heapq

class State:
    def __init__(self, room, remaining_rectangular, remaining_square, cost, heuristic):
        self.room = room
        self.remaining_rectangular = remaining_rectangular
        self.remaining_square = remaining_square
        self.cost = cost
        self.heuristic = heuristic

def is_valid_move(room, obj_type, row, col):
    rows, cols = len(room), len(room[0])

    if obj_type == 'rectangular':
        return row + 1 < rows and col + 2 < cols and all(room[row + i][col + j] == 0 for i in range(2) for j in range(3))
    elif obj_type == 'square':
        return row + 1 < rows and col + 1 < cols and all(room[row + i][col + j] == 0 for i in range(2) for j in range(2))

def apply_move(room, obj_type, row, col):
    if obj_type == 'rectangular':
        for i in range(2):
            for j in range(3):
                room[row + i][col + j] = 1
    elif obj_type == 'square':
        for i in range(2):
            for j in range(2):
                room[row + i][col + j] = 1

def heuristic(room, remaining_rectangular, remaining_square):
    return remaining_rectangular * 6 + remaining_square * 4  # Heuristic based on the number of empty cells

def a_star_search():
    rows, cols = 6, 6
    initial_room = [[0] * cols for _ in range(rows)]

    initial_state = State(initial_room, 5, 4, 0, heuristic(initial_room, 5, 4))
    heap = [(initial_state.cost + initial_state.heuristic, initial_state)]
    visited = set()

    while heap:
        _, current_state = heapq.heappop(heap)

        if current_state.remaining_rectangular == 0 and current_state.remaining_square == 0:
            return current_state.room

        if tuple(map(tuple, current_state.room)) in visited:
            continue

        visited.add(tuple(map(tuple, current_state.room)))

        for i in range(rows):
            for j in range(cols):
                for obj_type in ['rectangular', 'square']:
                    if is_valid_move(current_state.room, obj_type, i, j):
                        new_room = [row[:] for row in current_state.room]
                        apply_move(new_room, obj_type, i, j)
                        new_remaining_rectangular = current_state.remaining_rectangular - (1 if obj_type == 'rectangular' else 0)
                        new_remaining_square = current_state.remaining_square - (1 if obj_type == 'square' else 0)
                        new_cost = current_state.cost + 1
                        new_heuristic = heuristic(new_room, new_remaining_rectangular, new_remaining_square)
                        new_state = State(new_room, new_remaining_rectangular, new_remaining_square, new_cost, new_heuristic)
                        heapq.heappush(heap, (new_state.cost + new_state.heuristic, new_state))

    return None

def print_room(room):
    for row in room:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    final_room = a_star_search()

    if final_room:
        print("Optimal arrangement:")
        print_room(final_room)
    else:
        print("No solution found.")

