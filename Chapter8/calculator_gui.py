import tkinter as tk

root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root, width=20)
e.grid(row=0, column=0, columnspan=4)

# Function
def click(value):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + str(value))

def clear():
    e.delete(0, tk.END)

def equal():
    result = eval(e.get())
    e.delete(0, tk.END)
    e.insert(0, result)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:

    if button == "C":
        cmd = clear

    elif button == "=":
        cmd = equal

    else:
        cmd = lambda x=button: click(x)

    tk.Button(root, text=button, width=5, height=2,
              command=cmd).grid(row=row, column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

root.mainloop()