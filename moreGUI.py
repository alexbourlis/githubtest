import tkinter as tk
from moreGUIwindow import *
from tkinter import messagebox


class Cartesian:
	def __init__(self):

		#self.optionW = opWindow()
		self.id1 = []
		self.root = tk.Tk()
		self.root.geometry('500x500')
		self.root.title('cartesian')

		self.menubar = tk.Menu(self.root)
		self.actionmenu = tk.Menu(self.menubar, tearoff=0)
		self.actionmenu.add_command(label="Add point", command=self.add_point)
		self.actionmenu.add_command(label="delete point", command=self.delete_point)
		self.actionmenu.add_command(label="Create point", command=self.newWindow)
		#self.actionmenu.add_command(label="Show point", command=self.rtndV)

		self.menubar.add_cascade(menu=self.actionmenu, label="Action")
		self.root.config(menu=self.menubar)

		self.can = tk.Canvas(self.root,bg='white')
		self.can.place(x=0,y=0,heigh=500,width=500)

		self.xaxis = self.can.create_line((0,250,500,250), fill = 'grey')
		self.zaxis = self.can.create_line((250,0,250,500), fill = 'grey')
		self.yaxis = self.can.create_line((0,500,500,0), fill='grey')

		self.origin = self.can.create_oval((247,247,253,253))

		self.root.mainloop()

	def shortcut(self,event):
		print(event)

	def point(self,a,b):
	    pnt = (247+a,247+b,253+a,253+b)
	    return pnt

	def add_point(self,x=100,y=-50):
	    self.id1.append(self.can.create_oval(self.point(x,y)))
	    print("add")

	def delete_point(self):
		if len(self.id1)==0:
			print("nothing to remove")
		else:
		    self.can.delete(self.id1[-1])
		    self.id1 = self.id1[:-1]
		    print("delete")

	def newWindow(self):
		self.opWinState = True
		optionW = tk.Toplevel()
		self.opWinParam = opWindowparam(optionW)
		optionW.bind("<Destroy>", self.pointConf)

	def pointConf(self,event):
		if self.opWinState == True:
			print(event)
			try:
				#print(int(self.opWinParam.texte1))
				x,y,z = int(self.opWinParam.texte1),int(self.opWinParam.texte2),int(self.opWinParam.texte3)
				#i should verify that the numbers make sense
				self.add_point(x+y,-z-y)
			except ValueError:
				print("Not a valid entry, enter 3 numbers in 3 different lines")
			except TypeError:
				print("No entries")
			self.opWinState = False

cart = Cartesian()
