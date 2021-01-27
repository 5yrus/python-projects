import tkinter as tk

HEIGHT = 100
WIDTH = 100

root = tk.Tk()

canvas1 = tk.Canvas(root, width=200, height=200)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(100, 100, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(100, 150, window=entry2)

def selected(event):
    myLabel = tk.Label(root, text=clicked.get()).pack()


myButton = tk.Button(root, text="Select Service", command=selected)
myButton.pack()

options = (
    "Outlook",
    "Gmail",
)

clicked = tk.StringVar()
clicked.set(options[0])

button = tk.Button(root, text="Login", bg='gray', fg='red', width=4, height=1)
button.pack()

root.mainloop()
