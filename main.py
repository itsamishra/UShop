import getData

def main():
	UPC = input()

	# Gets Amazon price for product
	try:
		amazonPrice = getData.getAmazonData(UPC)
	except:
		amazonPrice = getData.getAmazonData(UPC)

	print(amazonPrice)

if __name__ == '__main__':
	main()