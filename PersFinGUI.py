# File which builds the GUI using tkinter.

import tkinter as tk


def init_GUI():
    window = tk.Tk()

    title = tk.Label(
        text="This is a Personal Finance Tracker",
    )
    title.pack()
    window.mainloop()
    return


if __name__ == "__main__":
    init_GUI()
