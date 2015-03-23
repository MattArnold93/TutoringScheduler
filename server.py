from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb, utils, os

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

@app.route('/index')
def index():
  print "hi"
  return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():
  # db = utils.db_connect()
  # cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  # # if request.method == 'POST':
  #   print "yay"
  #   email = request.form['email']
  #   password = request.form['password']
  #   query = "SELECT * FROM users WHERE email = '%s' AND password = '%s'" % (email, password) 
  #   cur.execute(query)
  #   db.commit()
  #   print "committed"
      
  #   if cur.fetchone():
  #     session['logged_in'] = email
  #     print "redirect"
  #     return redirect(url_for('index'))
  return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
  # db = utils.db_connect()
  # cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  # if request.method == 'POST':
  #   firstname=request.form['firstname']
  #   lastname=request.form['lastname']
  #   email=request.form['email']
  #   password=request.form['password']
  #   print firstname + " " + lastname + " " + email + " " + password
  #   query = "INSERT INTO users (firstname,lastname,email,password,accountStatus) VALUES('%s','%s','%s','%s',1);" % (firstname,lastname,email,password)
  #   print query
  #   cur.execute(query)
  #   db.commit()
  #   return redirect(url_for('login'))
  return render_template('register.html')

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
 app.run(host='0.0.0.0', port=8080)