from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb, utils, os

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

@app.route('/index')
def index():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  queryStat = "SELECT accountStatus FROM users WHERE email = '" + session['username'] + "' AND password = '" + session['password'] + "';"
  print queryStat
  cur.execute(queryStat)
  print "executed"
  row = cur.fetchone()
  print row['accountStatus']
  if row['accountStatus'] == 1:
    session['Status'] = "admin"
  elif row['accountStatus'] == 2:
    session['Status'] = "tutor"
  elif row['accountStatus'] == 3:
    session['Status'] = "student"
  return render_template('index.html', row=row, )

@app.route('/logout')
def logout():
  session.pop('username', None)
  session.pop('password', None)
  session.pop('Status', None)
  return redirect(url_for('login'))

@app.route('/createTutor')
def createTutor():
  return render_template('createTutor.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
      print "yay"
      row = []
      email = request.form['email']
      password = request.form['password']
      query = "SELECT * FROM users WHERE email = '%s' AND password = '%s'" % (email, password) 
      print query
      cur.execute(query)
      login = cur.fetchall()
      db.commit()
      print "committed"
      if login:
        session['username'] = email
        session['password'] = password
        print "redirect"
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  if request.method == 'POST':
    firstname=request.form['firstname']
    lastname=request.form['lastname']
    email=request.form['email']
    password=request.form['password']
    print firstname + " " + lastname + " " + email + " " + password
    if "umw.edu" in email:
      query = "INSERT INTO users (firstname,lastname,email,password,accountStatus) VALUES('%s','%s','%s','%s',3);" % (firstname,lastname,email,password)
      print query
      cur.execute(query)
      db.commit()
      return redirect(url_for('login'))
    else:
      return redirect(url_for('register'))
  return render_template('register.html')

@app.route('/AdminDash')
def AdminDash():
  #db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
  stuff = []
  query = "SELECT * FROM users WHERE level LIKE 'ADMIN'"
  cur.execute(query)
  
  results = cur.fetchall()
  #for result in results:
    
  
  
  return "AdminDash"

@app.route('/TutorDash')
def TutorDash():
	return "TutorDash"

@app.route('/Schedule')
def Schedule():
	return "Schedule"

@app.route('/search')
def search():
  return render_template('search.html', selectedMenu='search')

@app.route('/search2')
def search2():
  if (searchbyname != False):
    stuff = {'firstname': request.form['firstname'],
          'lastname': request.form['lastname']}
  
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
    query = "SELECT firstname, lastname, courses FROM tutors WHERE firstname LIKE " + stuff[0] + " OR lastname LIKE " + stuff[1] + ";"
    cur.execute(query)
    db.commit()
    results = cur.fetchall()
    print results
  else: #Search by course
    stuff = {'Subject': request.form['Subject'],
              'CourseNum': request.form['CourseNum']}
    
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    query = "SELECT firstname, lastname FROM classes WHERE Subject LIKE " + stuff[0] + " OR CourseNum LIKE " + stuff[1] + ";"
    cur.execute(query)
    db.commit()
    results = cur.fetchall()
    print results
    
    
  
  
  return render_template('search2.html', stuff = stuff)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=True)