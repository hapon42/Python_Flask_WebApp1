from flask import Flask, render_template, url_for
import random
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'dafgdjdjrtrtru'

posts = [
  {
  'title':'First Blog Post',
  'content': 'This is the content of the First Blog',
  'author': 'John Doe',
  'datePosted': 'June 16, 2020'
  }, 
  {
  'title':'Second Blog Post',
  'content': 'This is the content of the Second Blog',
  'author': 'Jane Doe',
  'DatePosted': 'June 17, 2020'
  }
  ]


@app.route('/')
@app.route('/home')#you can add multiple routes this other routes are decorators
def Home():
    return render_template('/home.html',posts=posts)

@app.route('/about')
def About():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
  form = RegistrationForm()
  return render_template('register.html', title='Register', form=form)
@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)

print('a')
print(__name__)
if __name__ == 'flask_blog':  # Makes sure this is the main process
  print('b')
  app.run( # Starts the site
    debug = True, # this enables to reflect changes in the app without restarting the application
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)