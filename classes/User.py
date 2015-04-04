def User():
    firstname = ""
    lastname = ""
    email = ""
    password = ""
    accountStatus = 0
    schedule = ""
    classes = []
    

def getFirst(User):
    return User.firstname
    
def getLast(User):
    return User.lastname

def getEmail(User):
    return User.email

def getPass(User):
    return User.password
    
def getAccountStatus(User):
    return User.accountStatus
    
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
    
def setAccountStatus(num):
    User.accountStatus = num
    
def setSchedule(times):
    User.schedule = times