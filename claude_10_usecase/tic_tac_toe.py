import random
import math
from typing import List, Callable

# Constants
BOARD_SIZE = 9
EMPTY_CELL = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def create_board() -> List[str]:
    """
    Create an empty Tic-Tac-Toe board.

    Returns:
    List[str]: A list of 9 empty strings representing the Tic-Tac-Toe board.
    """
    return [EMPTY_CELL for _ in range(BOARD_SIZE)]

def visualize_board(board: List[str]) -> None:
    """
    Visualize the current state of the Tic-Tac-Toe board.
    
    This function takes the current board state and prints it in a 3x3 grid format,
    with each cell separated by vertical bars and horizontal lines.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    """
    print('-------------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |')
        print('-------------')

def is_board_full(board: List[str]) -> bool:
    """
    Check if the Tic-Tac-Toe board is completely filled.
    
    This function checks if there are any empty spaces left on the board.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    
    Returns:
    bool: True if the board is full, False otherwise.
    """
    return EMPTY_CELL not in board

def check_win(board: List[str], player: str) -> bool:
    """
    Check if a player has won the game.
    
    This function checks all possible winning combinations (rows, columns, and diagonals)
    to determine if the specified player has won.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    player (str): The player to check for a win ('X' or 'O').
    
    Returns:
    bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def player_move(board: List[str]) -> int:
    """
    Get the player's move.
    
    This function prompts the player to enter their move, validates the input,
    and ensures the chosen position is available on the board.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    
    Returns:
    int: The index (0-8) of the player's chosen move on the board.
    """
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= BOARD_SIZE:
                print(f"Invalid move. Please enter a number between 1 and {BOARD_SIZE}.")
            elif board[move] != EMPTY_CELL:
                print("That space is already occupied. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def easy_ai_move(board: List[str]) -> int:
    """
    Generate a move for the AI in easy difficulty.
    
    This function randomly selects an empty space on the board for the AI's move.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    
    Returns:
    int: The index (0-8) of the AI's chosen move on the board.
    """
    empty_spaces = [i for i, cell in enumerate(board) if cell == EMPTY_CELL]
    return random.choice(empty_spaces)

def medium_ai_move(board: List[str]) -> int:
    """
    Generate a move for the AI in medium difficulty.
    
    This function implements a basic strategy for the AI:
    1. Check if AI can win in the next move
    2. Check if player can win in the next move and block them
    3. If no immediate threat, choose a random move
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    
    Returns:
    int: The index (0-8) of the AI's chosen move on the board.
    """
    # First, check if AI can win in the next move
    for i in range(BOARD_SIZE):
        if board[i] == EMPTY_CELL:
            board[i] = PLAYER_O
            if check_win(board, PLAYER_O):
                board[i] = EMPTY_CELL
                return i
            board[i] = EMPTY_CELL
    
    # Then, check if player can win in the next move and block them
    for i in range(BOARD_SIZE):
        if board[i] == EMPTY_CELL:
            board[i] = PLAYER_X
            if check_win(board, PLAYER_X):
                board[i] = EMPTY_CELL
                return i
            board[i] = EMPTY_CELL
    
    # If no immediate threat, choose a random move
    return easy_ai_move(board)

def hard_ai_move(board: List[str]) -> int:
    """
    Generate a move for the AI in hard difficulty using the minimax algorithm.
    
    This function implements the minimax algorithm to find the optimal move for the AI.
    It evaluates all possible moves and their outcomes to choose the best one.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    
    Returns:
    int: The index (0-8) of the AI's chosen move on the board.
    """
    best_score = -math.inf
    best_move = None
    for i in range(BOARD_SIZE):
        if board[i] == EMPTY_CELL:
            board[i] = PLAYER_O
            score = minimax(board, 0, False)
            board[i] = EMPTY_CELL
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def minimax(board: List[str], depth: int, is_maximizing: bool) -> int:
    """
    Implement the minimax algorithm for the AI's decision making.
    
    This recursive function evaluates all possible game states to determine the best move.
    It alternates between maximizing the AI's score and minimizing the player's score.
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    depth (int): The current depth in the game tree.
    is_maximizing (bool): True if it's the AI's turn (maximizing), False if it's the player's turn (minimizing).
    
    Returns:
    int: The best score for the current game state.
    """
    if check_win(board, PLAYER_O):
        return 1
    if check_win(board, PLAYER_X):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(BOARD_SIZE):
            if board[i] == EMPTY_CELL:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY_CELL
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(BOARD_SIZE):
            if board[i] == EMPTY_CELL:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY_CELL
                best_score = min(score, best_score)
        return best_score

def play_game(board: List[str]) -> None:
    """
    Main game loop for Tic-Tac-Toe.
    
    This function manages the entire game flow, including:
    - Allowing the player to choose the AI difficulty
    - Alternating between player and AI moves
    - Checking for win/tie conditions
    - Handling game restart
    
    Args:
    board (List[str]): A list of 9 elements representing the Tic-Tac-Toe board.
    """
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
    
    ai_move: Callable[[List[str]], int] = {
        1: easy_ai_move,
        2: medium_ai_move,
        3: hard_ai_move
    }[difficulty]
    
    print(f"\nYou are '{PLAYER_X}', and the AI is '{PLAYER_O}'. Let's begin!")
    visualize_board(board)
    
    while True:
        # Player's turn
        player_pos = player_move(board)
        board[player_pos] = PLAYER_X
        visualize_board(board)
        
        if check_win(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        
        # AI's turn
        print("AI is making a move...")
        ai_pos = ai_move(board)
        board[ai_pos] = PLAYER_O
        visualize_board(board)
        
        if check_win(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing!")

def main() -> None:
    """
    Initialize and start the Tic-Tac-Toe game.
    """
    board = create_board()
    play_game(board)

# Start the game if this script is run directly
if __name__ == "__main__":
    main()