from bottle import route, run, template, post, request, get

#class Inf:
#	def __init__(self, s,m):
#		self.sender = s
#		self.message = m


msgs = []

@route('/chat', method=['GET', 'POST'])
def chat():

	sender = request.forms.username
	msg = request.forms.msg

	msgs.append({'sender': sender, 'msg': msg})
	
	inf = {
		'data': msgs
	}
	
	return template('index.tpl', inf)

run(host='localhost', port=8080, debug=True)
