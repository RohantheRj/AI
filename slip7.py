Q.1)Write a python program implement tic-tac-toe using alpha beeta pruning[

import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player, alpha, beta):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != ' ':
            print("Invalid move. Cell already occupied. Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)

        # Check if player wins
        if is_winner(board, 'O'):
            print("Congratulations! You win!")
            break

        # Check if the board is full
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI is making a move...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'X'
        print_board(board)

        # Check if AI wins
        if is_winner(board, 'X'):
            print("AI wins! Better luck next time.")
            break

        # Check if the board is full
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()





Q2)))Write a Python program to implement Simple Chatbot.



import random

def simple_chatbot():
    print("Hello! I'm a Simple Chatbot. You can type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you!")
        elif 'your name' in user_input:
            print("Chatbot: I'm just a simple chatbot.")
        elif 'joke' in user_input:
            jokes = [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What did one wall say to the other wall? I'll meet you at the corner.",
                "Why don't scientists trust atoms? Because they make up everything!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()










