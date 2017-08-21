import getData

def main():
	UPC = input()

	# Gets Amazon price for product
	try:
		amazonPrice = getData.getAmazonData(UPC)
	except:
		amazonPrice = getData.getAmazonData(UPC)
	print("Amazon: $" + amazonPrice)


	try:
		walmartPrice = getData.getWalmartData(UPC)
	except:
		walmartPrice = getData.getWalmartData(UPC)
	print("Walmart: $" + walmartPrice)


	try:
		eBayPrice = getData.geteBayData(UPC)
	except:
		eBayPrice = getData.geteBayData(UPC)
	print("eBay: $" + eBayPrice)

if __name__ == '__main__':
	main()