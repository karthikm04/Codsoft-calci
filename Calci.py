import tkinter as tk
from tkinter import messagebox

# Create the main window
class Calci:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")  # Set the window size

        # Set background color of the entire window
        self.root.config(bg="lightgray")

        # Create a frame for the calculator with a black background to center the buttons and give contrast
        self.frame = tk.Frame(self.root, bg="black", padx=10, pady=10)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

        # Add decorative lines and a label with "ARITHMETIC CALCI"
        self.top_line = tk.Frame(self.frame, bg="Violet", height=3, width=300)
        self.top_line.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 2))  # Decorative top line

        # Add the text label between the lines
        self.label = tk.Label(self.frame, text="ARITHMETIC CALCI", font=("Helvetica", 16, "bold"), bg="Red", fg="Light blue")
        self.label.grid(row=1, column=0, columnspan=4, pady=(2, 2))

        # Add a bottom line below the label
        self.bottom_line = tk.Frame(self.frame, bg="darkblue", height=3, width=300)
        self.bottom_line.grid(row=2, column=0, columnspan=4, padx=10, pady=(2, 10))  # Decorative bottom line

        # Create the entry widget with fancy display settings
        self.entry = tk.Entry(self.frame, width=24, borderwidth=10, justify="right", font=("Helvetica", 18, "bold italic"), bg="lightyellow", relief="groove")
        self.entry.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    # Create the buttons
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '%'
        ]

        button_bg = "lavender"  # Set button background color
        button_style = {"width": 10, "height": 3, "bg": button_bg, "relief": "raised", "borderwidth": 5}  # Button style

        row_val = 4  # Start the row after the display and header
        col_val = 0

        # Add buttons in a grid layout with updated style
        for button in buttons:
            tk.Button(self.frame, text=button, **button_style, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Adjust the modulus button position
        tk.Button(self.frame, text="%", **button_style, command=lambda: self.click_button('%')).grid(row=row_val, column=0, padx=5, pady=5)

        # Create the expanded clear button spanning across columns 2-3
        tk.Button(self.frame, text="Clear", height=3, bg="orange", borderwidth=5, relief="raised", command=self.clear_entry).grid(row=row_val, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    # Handle button clicks
    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    # Clear the entry field
    def clear_entry(self):
        self.entry.delete(0, tk.END)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calci(root)
    root.mainloop()
