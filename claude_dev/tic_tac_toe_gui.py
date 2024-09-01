import tkinter as tk
from tkinter import messagebox
import random
import math

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.game_over = False
        self.ai_difficulty = None

        self.create_board()
        self.create_difficulty_buttons()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=' ', font=('normal', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def create_difficulty_buttons(self):
        difficulty_frame = tk.Frame(self.master)
        difficulty_frame.grid(row=3, column=0, columnspan=3)

        difficulties = ['Easy', 'Medium', 'Hard']
        for i, diff in enumerate(difficulties):
            btn = tk.Button(difficulty_frame, text=diff, command=lambda d=i+1: self.set_difficulty(d))
            btn.pack(side=tk.LEFT, padx=5, pady=5)

    def set_difficulty(self, difficulty):
        self.ai_difficulty = difficulty
        for btn in self.master.winfo_children():
            if isinstance(btn, tk.Button):
                btn.config(state=tk.NORMAL)

    def on_button_click(self, row, col):
        if not self.game_over and self.ai_difficulty:
            index = 3 * row + col
            if self.board[index] == ' ':
                self.board[index] = self.current_player
                self.buttons[index].config(text=self.current_player)
                
                if self.check_win(self.board, self.current_player):
                    self.game_over = True
                    messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                elif self.is_board_full():
                    self.game_over = True
                    messagebox.showinfo("Game Over", "It's a tie!")
                else:
                    self.current_player = 'O'
                    self.ai_move()

    def ai_move(self):
        if self.ai_difficulty == 1:
            move = self.easy_ai_move()
        elif self.ai_difficulty == 2:
            move = self.medium_ai_move()
        else:
            move = self.hard_ai_move()

        self.board[move] = 'O'
        self.buttons[move].config(text='O')

        if self.check_win(self.board, 'O'):
            self.game_over = True
            messagebox.showinfo("Game Over", "AI wins!")
        elif self.is_board_full():
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            self.current_player = 'X'

    def easy_ai_move(self):
        empty_spaces = [i for i, x in enumerate(self.board) if x == ' ']
        return random.choice(empty_spaces)

    def medium_ai_move(self):
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.check_win(self.board, 'O'):
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                if self.check_win(self.board, 'X'):
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '

        return self.easy_ai_move()

    def hard_ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_win(board, 'O'):
            return 1
        if self.check_win(board, 'X'):
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    @staticmethod
    def check_win(board, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(board[i] == player for i in condition) for condition in win_conditions)

    def is_board_full(self):
        return ' ' not in self.board

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()