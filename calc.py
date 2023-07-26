import tkinter as tk
def on_click(event):
    current_text = display_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(current_text + button_text)

# Main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.config(bg="#f2f2f2")

# Variable to store the input and result
display_var = tk.StringVar()

# Create the display widget
display = tk.Entry(root, textvar=display_var, font=("Helvetica", 32), bd=5, relief=tk.SOLID, justify=tk.RIGHT, bg="#fff", fg="#333")
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Create the button frame
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH)

# Buttons with custom colors
buttons = [
    ("7", "8", "9", "/", "#f2a154"),
    ("4", "5", "6", "*", "#f2a154"),
    ("1", "2", "3", "-", "#f2a154"),
    ("C", "0", "=", "+", "#f26b6b")
]

# Add the buttons to the frame
for row_idx, row in enumerate(buttons):
    for col_idx, (text, bg_color) in enumerate(zip(row[:-1], [row[-1]]*len(row))):
        button = tk.Button(button_frame, text=text, font=("Helvetica", 20, "bold"), bd=5, relief=tk.GROOVE, bg=bg_color, fg="#fff")
        button.grid(row=row_idx, column=col_idx, padx=10, pady=10, sticky="nsew")
        button.bind("<Button-1>", on_click)

# To make the buttons expandable
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)

root.mainloop()
