from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	print (request.method, request.path, request.form)
	return "hello napier"
