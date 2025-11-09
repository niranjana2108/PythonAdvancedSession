import tkinter as tk
from tkinter import messagebox


class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.create_menu()
        self.create_display()
        self.create_buttons()

    # ---------------- MENU BAR -----------------
    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    # ---------------- DISPLAY -------------------
    def create_display(self):
        self.display_var = tk.StringVar()
        display_frame = tk.Frame(self.root)

        display = tk.Entry(display_frame,
                           textvariable=self.display_var,
                           font=("Verdana", 16),
                           bd=8,
                           relief="sunken",
                           justify="right")
        display.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

        display_frame.pack()

    # ---------------- BUTTONS -------------------
    def create_buttons(self):
        btns_frame = tk.Frame(self.root)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            for btn_text in row:
                button = tk.Button(row_frame,
                                   text=btn_text,
                                   width=5, height=2,
                                   font=("Verdana", 14),
                                   command=lambda t=btn_text: self.on_button_click(t))
                button.pack(side="left", padx=5, pady=5)
            row_frame.pack()

        btns_frame.pack()

    # ---------------- EVENT HANDLING ------------
    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def show_about(self):
        messagebox.showinfo("About", "Simple Calculator App\nBuilt using Tkinter")


# ---------------- MAIN APP -----------------
if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()
