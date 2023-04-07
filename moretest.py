import numpy as np

#f = open('workfile','w',encoding="utf-8")

import tkinter as tk
from tkinter import messagebox

class Gui:
    """Gui class"""
    def __init__(self):
        self.root = tk.Tk()

        self.new_window = tk.Button(master=self.root, text="Open new window", width=20, pady=4, command=self.new_window)
        self.new_window.pack()

        self.root.mainloop()

    def new_window(self):
        """Create a new top level window"""
        new_window = tk.Toplevel()
        futest(new_window)
        #tk.Label(master=new_window, text="This is a new window").pack()
        new_window.bind("<Destroy>",self.on_closing)
    def on_closing(self,event):
        #if messagebox.askyesno(title="Quit?", message ="Do you really want to quit?"):
         #   self.root.destroy()
        print('hi')

def futest(window:tk.Toplevel):
	tk.Label(master=window, text="This is a new window").pack()


if __name__ == '__main__':
    Gui()








