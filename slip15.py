1)Write a Program to Implement Monkey Banana Problem using Python



import random

class MonkeyBananaProblem:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.monkey_position = (rows - 1, 0)
        self.banana_position = (0, cols - 1)
        self.bananas_collected = 0

    def move(self, direction):
        if direction == 'up' and self.monkey_position[0] > 0:
            self.monkey_position = (self.monkey_position[0] - 1, self.monkey_position[1])
        elif direction == 'down' and self.monkey_position[0] < self.rows - 1:
            self.monkey_position = (self.monkey_position[0] + 1, self.monkey_position[1])
        elif direction == 'left' and self.monkey_position[1] > 0:
            self.monkey_position = (self.monkey_position[0], self.monkey_position[1] - 1)
        elif direction == 'right' and self.monkey_position[1] < self.cols - 1:
            self.monkey_position = (self.monkey_position[0], self.monkey_position[1] + 1)

        if self.monkey_position == self.banana_position:
            self.bananas_collected += 1
            self.place_banana()

    def place_banana(self):
        self.banana_position = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))

    def print_state(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == self.monkey_position:
                    print('M', end=' ')
                elif (i, j) == self.banana_position:
                    print('B', end=' ')
                else:
                    print('.', end=' ')
            print()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows in the room: "))
    cols = int(input("Enter the number of columns in the room: "))

    monkey_banana_problem = MonkeyBananaProblem(rows, cols)

    while True:
        monkey_banana_problem.print_state()
        print(f"Bananas collected: {monkey_banana_problem.bananas_collected}")

        if monkey_banana_problem.monkey_position == monkey_banana_problem.banana_position:
            print("Congratulations! Monkey reached the banana.")
            break

        direction = input("Enter the direction to move (up/down/left/right): ")
        monkey_banana_problem.move(direction.lower())



Q2)Write a program to implement Iterative Deepening DFS algorithm.

def iterative_deepening_dfs(root, goal_state, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_dfs(root, goal_state, depth)
        if result is not None:
            return result
    return None

def depth_limited_dfs(node, goal_state, depth):
    if depth == 0 and node == goal_state:
        return node
    elif depth > 0:
        for child_state in generate_children(node):
            result = depth_limited_dfs(child_state, goal_state, depth - 1)
            if result is not None:
                return result
    return None

def generate_children(state):
    # Modify this function based on your specific problem to generate children
    # For demonstration purposes, let's consider a simple problem of generating children for integers
    return [state + 1, state - 1]

def iterative_deepening_dfs_without_class(initial_state, goal_state, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_dfs(initial_state, goal_state, depth)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    initial_state = 0
    goal_state = 5
    max_depth = 10

    result = iterative_deepening_dfs_without_class(initial_state, goal_state, max_depth)

    if result is not None:
        print("Goal state found:", result)
    else:
        print("Goal state not found within the maximum depth.")
