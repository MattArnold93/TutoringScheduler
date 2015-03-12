from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict
import utils, MySQLdb
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return "Login"

@app.route('/register')
def register():
	return "Register"

@app.route('/AdminDash')
def AdminDash():
	return "AdminDash"

@app.route('/TutorDash')
def TutorDash():
	return "TutorDash"

@app.route('/Schedule')
def Schedule():
	return "Schedule"


if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0', port=6782)