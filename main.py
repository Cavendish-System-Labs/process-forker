import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def show_notification():
    win = tk.Toplevel()
    win.title("System Breach")

    ms_w = 250
    ms_h = 100

    rand_x = random.randint(0, root.winfo_screenwidth() - ms_w)
    rand_y = random.randint(0, root.winfo_screenheight() - ms_h)

    win.geometry(f"{ms_w}x{ms_h}+{rand_x}+{rand_y}")

    label = tk.Label(win, text="Un-Authorization", fg="red")
    label.pack(expand=True)

    root.after(200, show_notification)

if __name__ == '__main__':
    show_notification()
    root.mainloop()
