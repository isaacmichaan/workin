# insert text to blog in metasploitable without needing to do it manually
import requests

url='http://10.0.0.9/mutillidae/index.php?page=add-to-your-blog.php'

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Cookie': 'PHPSESSID=2c8a6cfa83869a2c232cfffcc59c3fe2'
}

data = {
'csrf-token': 'SecurityIsDisabled',
'blog_entry': 'bla bla',
'add-to-your-blog-php-submit-button': 'Save+Blog+Entry'
}

requests.post(url, data=data, headers=headers)
