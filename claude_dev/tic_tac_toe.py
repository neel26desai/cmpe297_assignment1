import random
import math

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3+1], '|', board[i*3+2], '|')
        print('-------------')

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function for player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That space is already occupied. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function for easy AI move (random)
def easy_ai_move(board):
    empty_spaces = [i for i, x in enumerate(board) if x == ' ']
    return random.choice(empty_spaces)

# Function for medium AI move (basic strategy)
def medium_ai_move(board):
    # First, check if AI can win in the next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win(board, 'O'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # Then, check if player can win in the next move and block them
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win(board, 'X'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # If no immediate threat, choose a random move
    return easy_ai_move(board)

# Function for hard AI move (minimax algorithm)
def hard_ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    global board
    board = [' ' for _ in range(9)]
    
    print("Welcome to Tic-Tac-Toe!")
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        try:
            difficulty = int(input("Enter the number of your chosen difficulty (1-3): "))
            if difficulty < 1 or difficulty > 3:
                print("Invalid choice. Please enter a number between 1 and 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    ai_move = {
        1: easy_ai_move,
        2: medium_ai_move,
        3: hard_ai_move
    }[difficulty]
    
    print("\nYou are 'X', and the AI is 'O'. Let's begin!")
    print_board(board)
    
    while True:
        # Player's turn
        player_pos = player_move(board)
        board[player_pos] = 'X'
        print_board(board)
        
        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        
        # AI's turn
        print("AI is making a move...")
        ai_pos = ai_move(board)
        board[ai_pos] = 'O'
        print_board(board)
        
        if check_win(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    play_game()