import getData

def main():
	UPC = input()

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

if __name__ == '__main__':
	main()