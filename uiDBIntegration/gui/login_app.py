# gui/login_app.py
import tkinter as tk
from tkinter import messagebox

from uiDBIntegration.database.db_manager import DBManager


# from gui.db_manager import DBManager

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Register System")
        self.root.geometry("400x400")
        self.db = DBManager()

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(pady=50)

        tk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Entry(frame, textvariable=self.username_var).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.password_var, show="*").grid(row=1, column=1)

        tk.Button(frame, text="Login", command=self.login_user).grid(row=2, column=0, pady=20)
        tk.Button(frame, text="Register", command=self.create_register_frame).grid(row=2, column=1, pady=20)

    def create_register_frame(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(pady=30)

        tk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(frame, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(frame, text="Phone:").grid(row=3, column=0, padx=10, pady=5)

        self.reg_username = tk.StringVar()
        self.reg_password = tk.StringVar()
        self.reg_email = tk.StringVar()
        self.reg_phone = tk.StringVar()

        tk.Entry(frame, textvariable=self.reg_username).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.reg_password, show="*").grid(row=1, column=1)
        tk.Entry(frame, textvariable=self.reg_email).grid(row=2, column=1)
        tk.Entry(frame, textvariable=self.reg_phone).grid(row=3, column=1)

        tk.Button(frame, text="Register", command=self.register_user).grid(row=4, column=0, columnspan=2, pady=15)
        tk.Button(frame, text="Back to Login", command=self.create_login_frame).grid(row=5, column=0, columnspan=2)

    def login_user(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if self.db.validate_login(username, password):
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register_user(self):
        username = self.reg_username.get()
        password = self.reg_password.get()
        email = self.reg_email.get()
        phone = self.reg_phone.get()

        if not (username and password):
            messagebox.showwarning("Warning", "Username and Password are required!")
            return

        if self.db.register_user(username, password, email, phone):
            messagebox.showinfo("Success", "User registered successfully!")
            self.create_login_frame()
        else:
            messagebox.showerror("Error", "Username already exists!")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
