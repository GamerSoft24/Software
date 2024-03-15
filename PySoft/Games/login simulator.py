import tkinter as tk
from tkinter import messagebox

# Fake user credentials
fake_username = "fakeuser"
fake_password = "fakepassword1234"

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == fake_username and entered_password == fake_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def fit_to_screen():
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

root = tk.Tk()
root.title("Fake Login Platform")

fit_to_screen()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Mask the password
password_entry.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

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
