def User():
    firstname = ""
    lastname = ""
    email = ""
    password = ""

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
    