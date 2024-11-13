1)Write a python program to generate Calendar for the given month and year?



import calendar

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"Calendar for {month_name} {year}:")
    print(" Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2} ", end=" ")

        print()

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    generate_calendar(year, month)












Q.2)Write a Python program to simulate 4-Queens problem



def is_safe(board, row, col):
    # Check if there is a queen in the same row
    if any(board[row][c] == 1 for c in range(col)):
        return False

    # Check upper diagonal on the left side
    if any(board[r][c] == 1 for r, c in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check lower diagonal on the left side
    if any(board[r][c] == 1 for r, c in zip(range(row, len(board)), range(col, -1, -1))):
        return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[row][col] = 0

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if solve_n_queens_util(board, 0):
        print("Solution found:")
        for row in board:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_n_queens(4)
