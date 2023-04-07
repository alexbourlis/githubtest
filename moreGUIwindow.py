import tkinter as tk

class opWindowparam:
    def __init__(self,window: tk.Toplevel):
        self.window = window
        self.texte1 = []
        self.texte2 = []
        self.texte3 = []

        self.label = tk.Label(self.window, text="New point Coordinates", font=('Arial', 10))
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.window, font=('Arial', 16), height=3, width=10)
        self.textbox.pack(padx=10, pady=10)
        self.button = tk.Button(self.window, text="create point", font=('Arial', 10), command=self.btnfunc)
        self.button.pack(padx=10, pady=10)

    def btnfunc(self):
        self.texte1 = self.textbox.get('1.0', '1.10')
        self.texte2 = self.textbox.get('2.0', '2.10')
        self.texte3 = self.textbox.get('3.0', '3.10')
        self.window.destroy()



#W=opWindow()
#W.create()