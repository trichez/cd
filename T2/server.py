from bottle import route, run, template, post, request, get
import time
import threading
import requests
import json
import sys
#class Inf:
#	def __init__(self, s,m):
#		self.sender = s
#		self.message = m

porta = str(sys.argv[1])
msgs = []
servers = []#quem via usar ? la no tpl se usa 
@route('/chat', method=['GET', 'POST'])
def chat():

	sender = request.forms.username
	msg = request.forms.msg

	msgs.append({'sender': sender, 'msg': msg})
	
	inf = {
		'data': msgs
	}
	
	return template('index.tpl', inf)

@route('/msg', method =['GET']) #msg
def msg():# transforma msgs[] em json
	msg_j = []
	for i in msgs:
		msg_j.append(json.loads(msgs))
	
	return msg_j
	
@route('/peers/<url>', method = ['GET']) #lista de peers
def peers(url): #faz o append dos servers
	if not url in servers:
		servers.append(url)
	
	return servers
@route('client', method=['GET'])	
def client():# qnd invocado requisita os servers
	
	srvs = requests.get("http://localhost:8080/peers/porta") 
	return servers
		
		

t = threading.Thread(target=client,args=())
t.start()


run(host='localhost', port=porta, debug=True)
