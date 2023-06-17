import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('GUI2')

label = tk.Label(root, text="Hello world!", font=("Arial",18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=50)
#button with parent root
button  = tk.Button(root, text="click me!", font=('Arial',18))
button.place(x=350, y=350, height=100, width=100)
#making a frame for another button
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

b1  = tk.Button(buttonframe, text="1", font=('Arial',18))
b1.grid(row=0,column=0, sticky=tk.W+tk.E)
b2  = tk.Button(buttonframe, text="2", font=('Arial',18))
b2.grid(row=0,column=1, sticky=tk.W+tk.E)
b3  = tk.Button(buttonframe, text="3", font=('Arial',18))
b3.grid(row=0,column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

myentry = tk.Entry(root)
myentry.pack()
Nwindow = tk.Toplevel()

root.mainloop()