import socket
import googlesearch
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from time import time, sleep

startTime = time()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

for search in googlesearch.search(query="Vasant Kurvari", tld="com", pause=1, user_agent=headers['User-Agent']):

	print(search)
	my_url = search
	# ipAd =  socket.getaddrinfo('localhost', 8080)
	print(ipAd)
	break
	"""
	req = Request(url=my_url, headers=headers) 
	uClient = urlopen(req)
	html_parse = uClient.read()
	uClient.close()

	html_soup = soup(html_parse, "lxml")

	# web_pages = html_soup.findAll("h3", {"class":"LC20lb"})
	# link_pages = html_soup.findAll("cite", attrs={"class": "iUh30"})

	# for page in range(len(web_pages)):
		# linkName = link_pages[page].text
	"""



endTime = time()

print(endTime-startTime)