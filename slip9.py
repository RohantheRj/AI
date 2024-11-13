Write python program to solve 8 puzzle problem using A* algorithm [



import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def heuristic(self):
        # Manhattan distance heuristic
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    h += abs(i - goal_i) + abs(j - goal_j)
        return h

    def get_possible_moves(self):
        moves = []
        i, j = next((i, j) for i, row in enumerate(self.state) for j, value in enumerate(row) if value == 0)
        for move_i, move_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + move_i, j + move_j
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row.copy() for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                moves.append(PuzzleNode(new_state, self, (i, j)))
        return moves

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    if initial_node.heuristic() == 0:
        return [initial_node.state]

    visited = set()
    priority_queue = [initial_node]

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        visited.add(current_node)

        for neighbor in current_node.get_possible_moves():
            if neighbor not in visited:
                if neighbor.heuristic() == 0:
                    # Found the solution
                    path = [neighbor.state]
                    while neighbor.parent:
                        path.append(neighbor.parent.state)
                        neighbor = neighbor.parent
                    path.reverse()
                    return path
                heapq.heappush(priority_queue, neighbor)

    return None

def print_solution(solution):
    for step, state in enumerate(solution):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print("\n")

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    solution = a_star(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")








Q2) Write a Python program to solve water jug problem. 2 jugs with capacity 5 gallon and 7 gallon are given with unlimited water supply respectively. The target to achieve is 4 gallon of water in second jug.



def water_jug_problem(jug1, jug2, target):
    def pour(jug1, jug2):
        # Pour water from jug1 to jug2
        if jug1[0] > 0 and jug2[1] < jug2[2]:
            amount = min(jug1[0], jug2[2] - jug2[1])
            jug1[0] -= amount
            jug2[1] += amount
            yield jug1, jug2

        # Pour water from jug2 to jug1
        if jug2[1] > 0 and jug1[0] < jug1[1]:
            amount = min(jug2[1], jug1[1] - jug1[0])
            jug2[1] -= amount
            jug1[0] += amount
            yield jug1, jug2

    def dfs(current_state, visited):
        if current_state[0][0] == target or current_state[1][0] == target:
            return [current_state[0][0], current_state[1][0]]

        visited.add((current_state[0][0], current_state[1][0]))

        for next_state in pour(*current_state):
            if (next_state[0][0], next_state[1][0]) not in visited:
                result = dfs(next_state, visited)
                if result:
                    return [current_state[0][0], current_state[1][0]] + result

        return None

    initial_state = [[0, 5], [0, 7]]
    final_state = dfs(initial_state, set())

    if final_state:
        print(f"Solution found: {final_state[0]} gallons in the 5-gallon jug and {final_state[1]} gallons in the 7-gallon jug.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    water_jug_problem(5, 7, 4)











