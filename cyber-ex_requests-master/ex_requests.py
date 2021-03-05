# doing a google research of all the urls in a page
import requests
from bs4 import BeautifulSoup
from header_parser import headers_parser

class Google:
	def __init__(self):
		self.headers = headers_parser(headers)
		self.url = "https://www.google.com/search"
		self.links = []

	def search(self):
		text = input("Enter Keyword: ")
		pages = input("How many pages?")
		start = 0
		for i in range(int(pages)):
			print(f"Page number {i+1}")
			print(self.google_search(text,str(start)))
			start = int(start) + 10

	def extract_links(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.select('.r a:not([class])'):
			self.links.append(link['href'])
			print(f"{link.text} - {link['href']}")

	def google_search(self, text, start='0'):
		newparams = {
			'q': text,
			'oq': text,
			'start': start
		}
		response = requests.get(self.url, params=newparams, headers=headers_parser(headers))
		self.extract_links(response.text)


headers = '''Host: www.google.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.google.com/
Cookie: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg; NID=197=E-4YOt-eDGaujR68iLrzNVD1PhmVWpjLEQF7jUMq4f-XkxhQq540A2k8JR-lORc_IVQQGEpJiIvoPrg5cDKcrQ4XGZLrmxsPe5dIq6LkigJqPkUvXWR-q2luBeVB3gX7aKlSQcIYrtr8JlnqJj_H4IiYLnLJTFgGUHMV_oZIqaA; ANID=AHWqTUlx_lJuRxCqdtNQws3AEXdPCW3QEF6Heh7OGFQhXfO88oUFQuum55RBafDw; 1P_JAR=2020-2-4-16; DV=E5CYlWO5nbYt0Huu17E4kLAIxKcPAZfVOJqCboh3ywEAAAA
Connection: keep-alive'''

search = Google()
#search.google_search('itzik')
search.search()
