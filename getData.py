import urllib
from bs4 import BeautifulSoup as soup

def getAmazonData(URL):
	amazonURL = URL

	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]	# used to spoof Amazon
	response = opener.open(amazonURL)
	pageHTML = response.read()

	pageSoup = soup(pageHTML, "html.parser")
	productInfo = pageSoup.findAll("div", {"class":"s-item-container"})[0]

	costDollars = productInfo.find("span", {"class":"sx-price-whole"}).text
	costCents = productInfo.find("sup", {"class":"sx-price-fractional"}).text

	return str(costDollars) + "." + str(costCents)