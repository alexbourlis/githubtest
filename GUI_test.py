#https://docs.python.org/fr/3/library/tkinter.html#tkinter.Tk
from tkinter import * #it imports everything
from tkinter import ttk
root = Tk(className="mon application")                                      #fait apparaître une interface vide avec comme titre "mon application"

root.geometry('800x500')

root.title('mon GUI')

frm = ttk.Frame(root, padding=10)                                           #creating a frame where we'll insert a label and a button
frm.grid()
ttk.Label(frm, text="Hello World!", font=('Arial',18)).grid(column=0, row=0)
ttk.Button(frm, text="Quit", cursor='watch', command=root.destroy).grid(column=1, row=0)
Text(frm, height=3, width=10, font=('Arial',16)).grid(column=2,row=0)
root.mainloop()

#get information about a widget
#btn = ttk.Button(frm)
#print(btn.configure().keys())

#compare information
#rint(set(btn.configure().keys()) - set(frm.configure().keys()))

#widget methods
#print(dir(btn))
#print(set(dir(btn)) - set(dir(frm)))