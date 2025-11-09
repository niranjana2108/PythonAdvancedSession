import tkinter as tk
from tkinter import messagebox


def login_action():
    username = username_var.get()
    password = password_var.get()

    if username == "" or password == "":
        messagebox.showwarning("Validation Error", "Username and Password cannot be empty")
        return

    if username == "admin" and password == "1234": #hard coding
        messagebox.showinfo("Login Success", "Welcome Admin!")
        username_var.set("")
        password_var.set("")
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")


# Main application window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x180")
root.resizable(False, False)

# Variables
username_var = tk.StringVar()
password_var = tk.StringVar()

# Widgets
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=username_var).grid(row=0, column=1, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=password_var, show="*").grid(row=1, column=1, pady=10)

tk.Button(root, text="Login", command=login_action).grid(row=2, column=1, pady=15)

# Run event loop
root.mainloop()
