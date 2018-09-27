from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask import jsonify, request, render_template, send_file, send_from_directory, make_response, redirect, url_for
from flask import session, flash, make_response
app = Flask(__name__)
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
@app.route('/cakes')
def cakes():
  return 'Yummy cakes!' 
@app.route('/login')
def student():
   return render_template('login.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

 
@app.route("/hello/<string:name>/")
def hello(name):
	#return name
    # return render_template('test.html', name)
    quotes = [ "Build a man a fire, and he'll be warm for a day. Set a man on fire, and he'll be warm for the rest of his life.",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "Coming back to where you started is not the same as never leaving.",
               "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "Real stupidity beats artificial intelligence every time."  ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
 
    return render_template(
        'test.html',**locals())

if __name__ == "__main__":
    app.run()