def User():
    firstname = ""
    lastname = ""
    email = ""
    password = ""
    flag = 0

def getFirst(User):
    return User.firstname
    
def getLast(User):
    return User.lastname

def getEmail(User):
    return User.email

def getPass(User):
    return User.password
    
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

def getFlag(User):
    return User.flag
    