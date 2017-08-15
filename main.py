import getData

def main():
	amazonPrice = getData.getAmazonData("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=037000509783&rh=i%3Aaps%2Ck%3A037000509783")
	print(amazonPrice)

if __name__ == '__main__':
	main()