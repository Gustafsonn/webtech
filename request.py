from flask import Flask, request
app = Flask(__name__)


@app.route("/account/", methods=['GET', 'POST'])
def account():
	if request.method == 'POST':
		print (request.form)
		name = request.form['name']
		return "Hello %s" % name
	else:
		page = '''
		<html><body>
			<form action="" method="post" name="form">
				<labelfor="name">Name:</label>
				<input type="text" name="name" id="name"/>
				<input type="submit" name="submit" id="submit"/>
			</form>
		</body><html>'''

		return page


@app.route("/hello/<name>")
def hello(name):
	return "hello %s" % name


@app.route("/add/<int:first>/<int:second>")
def add(first, second):
	return str(first+second)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
