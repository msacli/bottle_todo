from bottle import run,template, route

@route('/')
def index():
	return template('index.tpl')

run(host='localhost', port=8080, debug='True', reloader='True')