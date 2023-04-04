#https://docs.python.org/fr/3/library/tkinter.html#tkinter.Tk
# from tkinter import * #it imports everything
from tkinter import ttk
root = Tk(className="mon application")                                      #fait apparaître une interface vide avec comme titre "mon application"
frm = ttk.Frame(root, padding=10)                                           #creating a frame where we'll insert a label and a button
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#get information about a widget
#btn = ttk.Button(frm)
#print(btn.configure().keys())

#compare information
#rint(set(btn.configure().keys()) - set(frm.configure().keys()))

#widget methods
#print(dir(btn))
#print(set(dir(btn)) - set(dir(frm)))