def User():
    firstname = ""
    lastname = ""
    email = ""
    password = ""
    flag = 0
    schedule = ""
    course = []
    

def getFirst(User):
    return User.firstname
    
def getLast(User):
    return User.lastname

def getEmail(User):
    return User.email

def getPass(User):
    return User.password
    
def getFlag(User):
    return User.flag
    
def getSchedule(User):
    return User.schedule
    
def setFirst(first):
    User.firstname = first
    
def setLast(last):
    User.lastname = last
    
def setEmail(mail):
    User.email = mail

def setPass(word):
    User.password = word
    
def setFlag(num):
    User.flag = num
    
def setSchedule(times):
    user.schedule = times