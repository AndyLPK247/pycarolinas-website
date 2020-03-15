# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


# --------------------------------------------------------------------------------
# Create the Flask App
# --------------------------------------------------------------------------------

app = Flask(__name__)
bootstrap = Bootstrap(app)


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/code-of-conduct')
def code_of_conduct():
  return render_template('code-of-conduct.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/covid19')
def covid19():
  return render_template('covid19.html')


@app.route('/diversity')
def diversity():
  return render_template('diversity.html')


@app.route('/speaking')
def speaking():
  return render_template('speaking.html')


@app.route('/sponsors')
def sponsors():
  return render_template('sponsors.html')


@app.route('/venue')
def venue():
  return render_template('venue.html')
