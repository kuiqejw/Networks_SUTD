from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #determines entry point, / means root of the website
#so just http://127.0.0.1:5000
@app.route('/index')
def index():#name we give to the route
	user = {'username': 'Laura Ong'}
	posts = [
	{
		'author':{'username': 'John'},
		'body': 'Beautiful day in Berkeley'
	},
	{
		'author': {'username': 'Serena'},
		'body':'The Civil War movie read more...'
	}
	]
	return render_template('index.html',title = 'Home', user= user, posts = posts)#content of the web page

#added a template, found in /templates
@app.route('/cakes')
def cakes():
	return 'Yummy cakes!'
@app.route('/hello/<name>')#create a new route on website so that when you go to http://127.0.0.1/hello/name
#it will say 'hello name and replace 'name' with whatever you put ther so /hello/Paul/ will display Hello Paul!
#<name> part means it passes the name into the hello function as a variable called name
def hello(name):
	#function that determines what content is shown -- this time it takes the given name as a parameter
	return render_template('page.html', name=name)
	#It tells the template to render the variable name which was passed in the route function hello
	#here we look up the template page .html and pass in the variable name from the url so the template can use it
# @app.route('/hello')
# def hello():
# 	return 'You have yet to present an appropriate name'
if __name__=='__main__':
	app.run(debug=True, host = '0.0.0.0')