import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from hashlib import *
from hashlib import sha1 #hashing passwords

def setup():
    f="bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()

######################
#user dict builder
def dict_user_pass():
    f="util/bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM users"
    foo = c.execute(q)
    users = {}
    for bar in foo:
        user = bar[0]
        password = bar[1]
        users[user] = password;
    return users

#story dict builder
def dict_story():
    f="bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM stories"
    foo = c.execute(q)
    stories = {}
    for bar in foo:
        wiki_name = bar[0]
        content = bar[1]
        stories[wiki_name] = {}
        stories[wiki_name]['content'] = content
        stories[wiki_name]['working_version'] = bar[2]
        stories[wiki_name]['last_update'] = bar[3]
        stories[wiki_name]['contributors'] = bar[4]
    return stories
##################

##adding user
def add_user(username, password1, password2,  first_name, last_name, email):
    f="util/bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    userpass = dict_user_pass()
    passw = sha1(password1).hexdigest()
    if (username in userpass or email in userpass or  password1 != password2):
        return False
    command = "INSERT INTO users VALUES('"+ username + "','" + passw + "','" + first_name + "', '" + last_name + "','" + email + "', 'none')"
    c.execute(command)
    db.commit()
    db.close()
    return True

##adding story
def add_story(wikiname, content, contributor):
    f="bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    storydict = dict_story()
    if (wikiname in storydict):
        return False
    command = "INSERT INTO stories VALUES('"+ wikiname + "','" + content + "','" + content + "', '" + content  + "','" + contributor + "')"
    c.execute(command)
    db.commit()
    db.close()
    return True
####################
def verify_user(username, password):
    userpass = dict_user_pass()
    if not(username in userpass):
        return False
    ##verifying pass w database
    if(userpass[username] == sha1(password).hexdigest()):
        return True
    return False



'''
nice = dict_story()
add_story("My life", "My life is amazing", "dasha")
nice = dict_story()
for wow in nice:
    print wow'''

    


#==========================================================
#db.commit() #save changes
#db.close()  #close database'''
