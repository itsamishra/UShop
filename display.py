from tkinter import *
import getData

# Updates prices obtained from getPrices() method
def updatePrices(amazonPrice, walmartPrice, eBayPrice):
	amazonPriceLabel.config(text=amazonPrice)
	walmartPriceLabel.config(text=walmartPrice)
	eBayPriceLabel.config(text=eBayPrice)


# Gets prices for specified product
def getPrices():
	UPC = UPCEntry.get()

	# Gets Amazon price for product
	try:
		amazonPrice = getData.getAmazonData(UPC)
	except IndexError:
		amazonPrice = "----"
	except:
		amazonPrice = getData.getAmazonData(UPC)
	
	#print("Amazon:\t\t$" + amazonPrice)


	try:
		walmartPrice = getData.getWalmartData(UPC)
	except IndexError:
		walmartPrice = "----"
	except:
		walmartPrice = getData.getWalmartData(UPC)

	#print("Walmart:\t$" + walmartPrice)


	try:
		eBayPrice = getData.geteBayData(UPC)
	except IndexError:
		eBayPrice = "----"
	except:
		eBayPrice = getData.geteBayData(UPC)

	#print("eBay:\t\t$" + eBayPrice)

	updatePrices(amazonPrice, walmartPrice, eBayPrice)

def buildGUI():
	# Allows variables to be read/manipulated in other methods
	global UPCEntry, amazonPriceLabel, walmartPriceLabel, eBayPriceLabel

	root = Tk()

	# UPC stuff
	UPCLabel = Label(root, text="Product UPC")
	UPCEntry = Entry(root)
	UPCButton = Button(root, text="Enter", command=getPrices)

	UPCLabel.grid(row=0, column=0, sticky=E)
	UPCEntry.grid(row=0, column=1)
	UPCButton.grid(row=0, column=2)


	# Price stuff
	amazonDisplayLabel = Label(root, text = "Amazon Price")
	amazonPriceLabel = Label(root, text="")
	walmartDisplayLabel = Label(root, text = "Walmart Price")
	walmartPriceLabel = Label(root, text="")
	eBayDisplayLabel = Label(root, text = "eBay Price")
	eBayPriceLabel = Label(root, text="")

	amazonDisplayLabel.grid(row=2, column=0, sticky=E)
	amazonPriceLabel.grid(row=2, column=1, sticky=E)
	walmartDisplayLabel.grid(row=3, column=0, sticky=E)
	walmartPriceLabel.grid(row=3, column=1, sticky=E)
	eBayDisplayLabel.grid(row=4, column=0, sticky=E)
	eBayPriceLabel.grid(row=4, column=1, sticky=E)


	root.mainloop()


if __name__ == '__main__':
	buildGUI()