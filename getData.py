import urllib
from bs4 import BeautifulSoup as soup

# Gets price of amazon item with associated URL (sometimes throws error as connection isn't thred-safe)
def getAmazonData(UPC):
	amazonURL = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(UPC)

	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]	# used to spoof Amazon
	response = opener.open(amazonURL)
	pageHTML = response.read()

	pageSoup = soup(pageHTML, "html.parser")
	productInfo = pageSoup.findAll("div", {"class":"s-item-container"})[0]

	costDollars = productInfo.find("span", {"class":"sx-price-whole"}).text
	costCents = productInfo.find("sup", {"class":"sx-price-fractional"}).text

	return str(costDollars) + "." + str(costCents)

def getWalmartData(UPC):
	walmartURL = "https://www.walmart.com/search/?query=" + str(UPC)

	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	response = opener.open(walmartURL)
	pageHTML = response.read()

	pageSoup = soup(pageHTML, "html.parser")
	productInfo = pageSoup.findAll("div", {"class":"search-result-listview-item clearfix"})[0]

	costDollars = productInfo.find("span", {"class":"Price-characteristic"}).text
	costCents = productInfo.find("span", {"class":"Price-mantissa"}).text

	return str(costDollars) + "." + str(costCents)

def geteBayData(UPC):
	eBayURL = "https://www.ebay.com/sch/" + str(UPC)

	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	response = opener.open(eBayURL)
	pageHTML = response.read()

	pageSoup = soup(pageHTML, "html.parser")
	productInfo = pageSoup.findAll("li", {"class":"sresult lvresult clearfix li shic"})[0]

	cost = productInfo.find("span", {"class":"bold"}).text
	
	# Formatting cost to be number
	cost = cost.strip()
	cost = cost[1:]

	return str(cost)