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
  return render_template('index.html', row=row)

@app.route('/logout')
def logout():
  session.pop('username', None)
  session.pop('password', None)
  session.pop('Status', None)
  return redirect(url_for('login'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

  if request.method == 'POST':
    #password = session['password']
    oldP = request.form['oldpassword']
    newPass = request.form['password']
    email = session['username']
    level = session['Status']
  
    #if oldP is password:
      #if level is not "admin":
    
    #query = "UPDATE users SET password = '" + newPass + "' WHERE email = '" + email + "';"
    #cur.execute(query)
    #db.commit()
    
    #else:
    
      #firstname = request.form['firstName']
      #lastname = request.form['lastName']
    
    #query = "UPDATE users SET firstname = '" + firstname + "', lastname = '" + lastname + "', email = '" + email + "', password = '" + newPass + "' WHERE email = '" + email + "';"
    #cur.execute(query)
    #db.commit()
    
  return render_template('edit.html')

@app.route('/createTutor', methods=['GET', 'POST'])
def createTutor():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  created = " "
  if request.method == 'POST':
      row = []
      first = request.form['firstName']
      last = request.form['lastName']
      email = request.form['email']
      course = request.form['course']
      password = request.form['password']
      query2 = "SELECT * FROM users WHERE email = '%s';" % (email)
      cur.execute(query2)
      test = cur.fetchone()
      if test:
        print test
        if test['accountStatus'] == 1:
          created = "admin"
          print "Admin"
        elif test['accountStatus'] == 2:
          created = "no"
          print "Tutor"
        elif test['accountStatus'] == 3:
          print "Student"
          created = "updated"
          #if the query here does not activate, take out classes + and leave it '%s'
          query3 = "UPDATE users SET accountStatus = 2, classes = classes + '%s' WHERE email = '%s';" % (course, email)
          cur.execute(query3)
      else:
        print "Not Created"
        created = "yes"
        query = "INSERT INTO users (firstname,lastname,email,password,accountStatus,classes) VALUES('%s','%s','%s','%s',2, '%s');" % (first,last,email,password, course)
        cur.execute(query)
        db.commit()
  return render_template('createTutor.html', created=created)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  exist = " "
  if request.method == 'POST':
    firstname = request.form['firstName']
    lastname = request.form['lastName']
    email = request.form['email']
    reason = request.form['reason']
    query = "SELECT * FROM users WHERE firstname = '%s' AND lastname = '%s' AND email = '%s';" % (firstname, lastname, email)
    cur.execute(query)
    account = cur.fetchone()
    print session['username']
    print email
    if email == session['username']:
      exist = "admin"
    elif account:
      exist = "yes"
      query2 = "DELETE FROM users WHERE firstname = '%s' AND lastname = '%s' AND email = '%s';" % (firstname, lastname, email)
      cur.execute(query2)
      db.commit();
    else:
      exist = "no"
  return render_template('delete.html', exists=exist)

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
        session['logged_in'] = "yes"
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
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
  stuff = []
  query = "SELECT * FROM users WHERE level LIKE 'ADMIN'"
  cur.execute(query)
  
  results = cur.fetchall()
  #for result in results:

  return "AdminDash"

@app.route('/Schedule')
def Schedule():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

  query = "SELECT DISTINCT subject FROM classes"
  cur.execute(query)
  db.commit()

  results=cur.fetchall()

  return render_template('schedule.html', subjects=results)

@app.route('/appoint2', methods=['GET', 'POST'])
def appointment2():
  subject = request.form['subject']
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

  query = "SELECT class FROM classes WHERE subject=\'" + subject + "\'"
  cur.execute(query)
  db.commit()

  classes = cur.fetchall()

  return render_template('schedule2.html', classes=classes)

@app.route('/appoint3', methods=['GET', 'POST'])
def appointment3():
  selClass = request.form['class']
  selType = request.form['schedule']
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  fullDict = []
  #query = "SELECT numId, classes FROM users;"
  #cur.execute(query)
  #db.commit() 
  #users = cur.fetchall()
  #length = len(users)
  #for y in range(0,length):
   # dict1 = users[y]
    #classes = dict1['classes']
    #if classes == None:
     # continue
    #if selClass in classes:
     # print "found 1"
    #else:
     # continue


  

  if selType == "Tutor":
   # query = "SELECT numId, classes FROM users WHERE INNER JOIN times ON users.numId=times.studentId"
   print "stuff"
  else:
    query = "SELECT studentId, classes, dayofweek, hourof FROM times"
    cur.execute(query)
    db.commit()
    usrTimes = cur.fetchall()
    print usrTimes
    length = len(usrTimes)
    for y in range(0, length):
      dict1 = usrTimes[y]
      classes = dict1['classes']
      if classes == None:
        continue
      if selClass in classes:
        fullDict.append(dict1)
      else:
        continue
    results = fullDict
    for item in results:
      if item['dayofweek'] == "Monday":
        print "fun"
      elif item['dayofweek'] == "Tuesday":
        print "not fun"
      elif item['dayofweek'] == "Wednesday":
        print "bafds"
      else:
        print "sdgsdddddss"
  return render_template('schedule3.html', results=results)

#@app.route('/appoint4', methods=['GET', 'POST'])
#def appointment4():



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

