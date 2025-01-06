import tkinter as tk
from tkinter import messagebox

def click(event):
    try:
        text = event.widget.cget("text")
        if text == "=":
            if entry_value.get().strip() == "":
                return
            result = eval(entry_value.get())
            entry_value.set(result)
        elif text == "C":
            entry_value.set("")
        else:
            entry_value.set(entry_value.get() + text)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Creating main window
root = tk.Tk()
root.title("Beautiful Calculator")
root.geometry("300x400")
root.configure(bg="lightblue")

entry_value = tk.StringVar()
entry = tk.Entry(root, textvar=entry_value, font=("Arial", 20), justify='right', relief=tk.SUNKEN, bd=8)
entry.pack(fill=tk.X, padx=10, pady=15)

# Button layout and text
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Adding buttons to the interface
for row in buttons:
    frame = tk.Frame(root, bg="lightblue")
    frame.pack(expand=True, fill=tk.BOTH)
    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Arial", 15), width=5, relief=tk.RAISED, bg="white")
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        button.bind("<Button-1>", click)

# Run the main loop
root.mainloop()
