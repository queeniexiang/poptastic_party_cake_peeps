import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from hashlib import shai1 #hashing passwords
f="/data/bestsite.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
######################
#dict builder
def dict_user_pass():
    q = "SELECT * FROM users"
    foo = c.execute(q)
    users = {}
    for bar in foo:
        user = bar[0]
        password = bar[1]
        users[user] = password;       
return users
##################
def add_user(username, password, first_name, last_name, email):
    userpass = dict_user_pass()
    passw = sha1(password).hexdigest()
    if (username in userpass):
        return False
    command = "INSERT INTO users VALUES('"+ username + "','" + passw + "','" + first_name + "', '" + last_name + "','" + email + "', none)"
    c.execute(command)
    return True
####################
def verify_user(username, password):
    userpass = dict_user_pass()
    if !(username in userpass):
        return False
    if(userpass[username] == password):
        return True
    return False 


#==========================================================
db.commit() #save changes
db.close()  #close database'''

    
    
    
