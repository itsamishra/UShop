from tkinter import *

def getUPCInfo():
	print("hello")
	None

def makeGUI():
	root = Tk()

	upcLabel = Label(root, text="Product UPC")
	upcEntry = Entry(root)
	upcButton = Button(root, text="Go", command=getUPCInfo)

	upcLabel.grid(row=0, column=0)
	upcEntry.grid(row=0, column=1)
	upcButton.grid(row=0, column=2)

	root.mainloop()


if __name__ == '__main__':
	makeGUI()