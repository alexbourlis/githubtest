import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

            self.root = tk.Tk()

            self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
            self.label.pack(padx=10, pady=10)

            self.textbox = tk.Text(self.root, font=('Arial',16), height = 5)
            self.textbox.bind("<KeyPress>", self.shortcut)
            self.textbox.pack(padx=10, pady=10)

            self.check_state = tk.IntVar() #state of the checkbox
            self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
            self.check.pack(padx=10, pady=10)

            self.button = tk.Button(self.root, text= "Show Mesage", font=('Arial', 18), command = self.show_message)
            self.button.pack(padx=10, pady=10)

            self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))  #1.0 is the begining, tk.END is the end
        else:
            messagebox.showinfo(title="Message", message= self.textbox.get('1.0', tk.END))

    def shortcut(self,event):
        #print(event) to see what's going on
        if event.keysym == "Return" and event.state == 12:
            self.show_message()
MyGUI()