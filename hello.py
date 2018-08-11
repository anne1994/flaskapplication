from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/you')
def johnboy():
    return render_template("form.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/friend')
def annez():
    return 'Hi, I am your friend '


@app.route('/yourDetails' , methods = ["POST"])
def details():
	firstName = request.form["firstname"]
	lastName = request.form["lastname"]
	print("The name is " + firstName + " " + lastName)
	return '{} {}'.format(firstName, lastName)
    


if __name__ == '__main__':
	app.run()