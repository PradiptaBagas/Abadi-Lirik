import json
import tkinter as tk
import time

def print_lirik(interval):
    lirik = [
        'biarpun kita hilang',
        'tak lagi bersama',
        'tak lagi bercinta',
        'berdua'
    ]
    for baris in lirik:
        listbox.insert(tk.END, baris)
        root.update()
        time.sleep(interval)
        
root = tk.Tk()
root.title("A B A D I")
root.geometry("320x340")

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    interval = 4
    print_lirik(interval)
    root.mainloop()