import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def show_notification():

    ms_w = 300
    ms_h = 100

    rand_x = random.randint(0, root.winfo_screenwidth() - ms_w)
    rand_y = random.randint(0, root.winfo_screenheight() - ms_h)

    win = tk.Toplevel()
    win.withdraw()
    win.title("Hacked")
    win.update_idletasks()
    win.geometry(f"{ms_w}x{ms_h}+{rand_x}+{rand_y}")
    win.deiconify()
    win.resizable(False, False)

    frame = tk.Frame(win)
    frame.pack(expand=True, fill="both", padx=25, pady=10)

    icon = tk.PhotoImage(file="assets/error.png")
    icon = icon.subsample(6, 6)

    icon_label = tk.Label(frame, image=icon)
    icon_label.image = icon
    icon_label.pack(side="left")

    text_label = tk.Label(frame, text="Haha bitch, your pc has been hacked", anchor="w", justify="left")
    text_label.pack(expand=True)

    root.after(1, show_notification)

if __name__ == '__main__':
    show_notification()
    root.mainloop()
