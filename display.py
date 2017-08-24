from tkinter import *
import getData

def printEntry():
	UPC = UPCEntry.get()

	# Gets Amazon price for product
	try:
		amazonPrice = getData.getAmazonData(UPC)
	except IndexError:
		amazonPrice = "----"
	except:
		amazonPrice = getData.getAmazonData(UPC)
	
	print("Amazon:\t\t$" + amazonPrice)


	try:
		walmartPrice = getData.getWalmartData(UPC)
	except IndexError:
		walmartPrice = "----"
	except:
		walmartPrice = getData.getWalmartData(UPC)

	print("Walmart:\t$" + walmartPrice)


	try:
		eBayPrice = getData.geteBayData(UPC)
	except IndexError:
		eBayPrice = "----"
	except:
		eBayPrice = getData.geteBayData(UPC)

	print("eBay:\t\t$" + eBayPrice)

def buildGUI():
	# Allows variables to be read/manipulated in other methods
	global UPCEntry

	root = Tk()

	# UPC stuff
	UPCLabel = Label(root, text="Product UPC")
	UPCEntry = Entry(root)
	UPCButton = Button(root, text="Enter", command=printEntry)

	UPCLabel.grid(row=0, column=0, sticky=E)
	UPCEntry.grid(row=0, column=1)
	UPCButton.grid(row=0, column=2)


	# Price stuff
	amazonDisplayLabel = Label(root, text = "Amazon Price")
	amazonPriceLabel = Label(root, text="fetching...")
	walmartDisplayLabel = Label(root, text = "Walmart Price")
	walmartPriceLabel = Label(root, text="fetching...")
	eBayDisplayLabel = Label(root, text = "eBay Price")
	eBayPriceLabel = Label(root, text="fetching...")

	amazonDisplayLabel.grid(row=2, column=0, sticky=E)
	amazonPriceLabel.grid(row=2, column=1, sticky=E)
	walmartDisplayLabel.grid(row=3, column=0, sticky=E)
	walmartPriceLabel.grid(row=3, column=1, sticky=E)
	eBayDisplayLabel.grid(row=4, column=0, sticky=E)
	eBayPriceLabel.grid(row=4, column=1, sticky=E)


	root.mainloop()


if __name__ == '__main__':
	buildGUI()