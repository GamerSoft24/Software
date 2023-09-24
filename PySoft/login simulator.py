import tkinter as tk
from tkinter import messagebox

# Fake user credentials
fake_username = "fakeuser"
fake_password = "fakepassword1234"

# Function to check login credentials
def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == fake_username and entered_password == fake_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to fit the window to the screen
def fit_to_screen():
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Create the main window
root = tk.Tk()
root.title("Fake Login Platform")

# Fit the window to the screen initially
fit_to_screen()

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Mask the password
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

# Start the GUI main loop
root.mainloop()
