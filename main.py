import random
import time
import tkinter as tk
from multiprocessing import Process, Queue

icon = None

def worker(q):
    while True:
        q.put("spawn")
        time.sleep(0.1)

def message_box(root):
    ms_w, ms_h = 350, 100


    rand_x = random.randint(0, root.winfo_screenwidth() - ms_w)
    rand_y = random.randint(0, root.winfo_screenheight() - ms_h)

    win = tk.Toplevel(root)
    win.title("System Hacked")
    win.geometry(f"{ms_w}x{ms_h}+{rand_x}+{rand_y}")
    win.resizable(False, False)

    frame = tk.Frame(win)
    frame.pack(expand=True, fill="both", padx=25, pady=10)

    global icon

    if icon is None:
        icon = tk.PhotoImage(file="assets/error.png")
        icon = icon.subsample(6, 6)

    icon_label = tk.Label(frame, image=icon)
    icon_label.image = icon
    icon_label.pack(side="left")

    text_label = tk.Label(frame, text="Haha bitch, \nI hacked your computer", anchor="w", justify="left")
    text_label.pack(expand=True)

    root.update_idletasks()

def poll_queue(root, q):
    while not q.empty():
        q.get()
        message_box(root)

    root.after(50, poll_queue, root, q)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    q = Queue()

    p = Process(target=worker, args=(q,))
    p.start()

    poll_queue(root, q)
    root.mainloop()
