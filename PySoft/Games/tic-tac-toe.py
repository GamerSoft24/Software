import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(root, text='', width=10, height=3, command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

        for pattern in win_patterns:
            a, b, c = pattern
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False

    def reset_board(self):
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

except FileExistsError:
    exit()
except FileNotFoundError:
    exit()
except OSError:
    exit()
except ValueError:
    exit()
except KeyboardInterrupt:
    exit()
except EOFError:
    exit()
except BaseException:
    exit()
except IOError:
    exit()
except:
    exit()
