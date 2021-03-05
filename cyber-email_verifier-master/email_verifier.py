#verify if email exists
import requests

def email_verify():
	headers = {
    		'Authorization': 'bearer YOUR CODE',
		}
	email = input('Enter Email: ')
	params = {
    		'email':email,
	}
	res = requests.get('https://isitarealemail.com/api/email/validate', headers=headers, params=params)

	if 'invalid' in res.text:
		return 0
	return 1
