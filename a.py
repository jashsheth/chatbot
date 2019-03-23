from flask import Flask,request,jsonify
import json
import requests
url="http://numbersapi.com/"
app=Flask(__name__)


@app.route('/',methods=['GET'])
def home():
	return "asdfghj"

@app.route('/',methods=['POST'])
def post():
	req=request.get_json(silent = True, force = True)
	intent = req.get('queryResult').get('intent').get('displayName')
	print(req)
	if intent=='Default Welcome Intent':
		return jsonify({"fulfillmentText":"bhag"})
	elif intent=='numbers':
		t=req.get('queryResult').get('parameters').get('type')
		n=int(req.get('queryResult').get('parameters').get('number'))
		u= url+str(n)+"/"+t+"?json"
		print(u)
		res= requests.get(u)
		txt = res.json()["text"]

		return jsonify({"fulfillmentText":txt})	
	
		
		
        
	#return req

if(__name__=="__main__"):
	app.run()
