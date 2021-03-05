# find out which urls website has, foe example does yad2/robots.txt exists?
import requests

domain = input("Enter Domain: ")
urls = ['itzik.txt', 'beker.txt', 'robots.txt']

for link in urls:
	res = requests.get(domain + '/' + link)
	if res.status_code == 200:
		print(f"Found: {link}")
	else:
		print(f"Error: {link}, Status code: {res.status_code}")


