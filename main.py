from incomeTracker import *
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=1, width=20, font=("Arial", 16))
textbox.pack()

my_entry = tk.Entry(root)
my_entry.pack(pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="Add Income")
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="Remove Income")
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="Edit Income")
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

buttonframe.pack()

button = tk.Button(root, text="Save & Exit", font=("Arial", 12))
button.pack()

root.mainloop()
