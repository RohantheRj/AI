1) Write a python program using mean end analysis algorithmproblem of transforming a string of lowercase letters into another string.



def mean_end_analysis(start, goal):
    current_state = list(start)
    goal_state = list(goal)
    steps = []

    while current_state != goal_state:
        for i in range(len(current_state)):
            if current_state[i] != goal_state[i]:
                current_state[i] = chr((ord(current_state[i]) - 97 + 1) % 26 + 97)
                steps.append(''.join(current_state))
        
        if current_state == goal_state:
            break

        steps.append(''.join(current_state))

    return steps

if __name__ == "__main__":
    start_string = "abcde"
    goal_string = "vwxyz"

    result = mean_end_analysis(start_string, goal_string)

    if result:
        print(f"Transformation steps from '{start_string}' to '{goal_string}':")
        for step in result:
            print(step)
    else:
        print(f"No transformation needed. The strings are already the same.")







Q.2) Write a Python program to solve water jug problem. Two jugs with capacity 4 gallon and 3 gallon are given with unlimited water supply respectively. The target is to achieve 2 gallon of water in second jug.



def water_jug_problem(capacity_jug1, capacity_jug2, target):
    def pour(jug1, jug2):
        # Pour water from jug1 to jug2
        if jug1 > 0 and jug2 < capacity_jug2:
            amount = min(jug1, capacity_jug2 - jug2)
            jug1 -= amount
            jug2 += amount
            yield jug1, jug2

        # Pour water from jug2 to jug1
        if jug2 > 0 and jug1 < capacity_jug1:
            amount = min(jug2, capacity_jug1 - jug1)
            jug2 -= amount
            jug1 += amount
            yield jug1, jug2

    def dfs(current_state, visited):
        if current_state[1] == target:
            return [current_state[0], current_state[1]]

        visited.add(current_state)

        for next_state in pour(*current_state):
            if next_state not in visited:
                result = dfs(next_state, visited)
                if result:
                    return [current_state[0], current_state[1]] + result

        return None

    initial_state = [0, 0]
    final_state = dfs(initial_state, set())

    if final_state:
        print(f"Solution found: {final_state[0]} gallons in the 4-gallon jug and {final_state[1]} gallons in the 3-gallon jug.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    water_jug_problem(4, 3, 2)