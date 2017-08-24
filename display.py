from tkinter import *

def buildGUI():
	root = Tk()

	# UPC stuff
	UPCLabel = Label(root, text="Product UPC")
	UPCEntry = Entry(root)
	UPCButton = Button(root, text="Enter")
	UPCLabel.grid(row=0, column=0, sticky=E)
	UPCEntry.grid(row=0, column=1)
	UPCButton.grid(row=0, column=2)

	# Price stuff
	amazonDisplayLabel = Label(root, text = "Amazon Price")
	amazonPriceLabel = Label(root, text="#TODO")
	walmartDisplayLabel = Label(root, text = "Walmart Price")
	walmartPriceLabel = Label(root, text="#TODO")
	eBayDisplayLabel = Label(root, text = "eBay Price")
	eBayPriceLabel = Label(root, text="#TODO")

	amazonDisplayLabel.grid(row=2, column=0, sticky=E)
	amazonPriceLabel.grid(row=2, column=1, sticky=E)
	walmartDisplayLabel.grid(row=3, column=0, sticky=E)
	walmartPriceLabel.grid(row=3, column=1, sticky=E)
	eBayDisplayLabel.grid(row=4, column=0, sticky=E)
	eBayPriceLabel.grid(row=4, column=1, sticky=E)

	root.mainloop()


if __name__ == '__main__':
	buildGUI()