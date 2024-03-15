import tkinter as tk
import random

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon","car","chair","table","computer","dog","cat","football"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.word = random.choice(word_list)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        
        self.word_label = tk.Label(root, text="_ " * len(self.word), font=("Arial", 24))
        self.word_label.pack()
        
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack()
        
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if guess in self.guesses:
            self.result_label.config(text="You already guessed that letter.")
        elif guess in self.word:
            self.guesses.append(guess)
            self.update_word_display()
            if "_" not in self.word_label["text"]:
                self.result_label.config(text="Congratulations! You won!")
                self.guess_button.config(state=tk.DISABLED)
        else:
            self.guesses.append(guess)
            self.attempts += 1
            self.update_hangman_display()
            if self.attempts >= self.max_attempts:
                self.result_label.config(text=f"You lost! The word was {self.word}.")
                self.guess_button.config(state=tk.DISABLED)
        
    def update_word_display(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_label.config(text=displayed_word)
        
    def update_hangman_display(self):
        hangman_display = f"Attempts left: {self.max_attempts - self.attempts}"
        self.result_label.config(text=hangman_display)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
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
