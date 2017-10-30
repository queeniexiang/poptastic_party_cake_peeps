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
        users[user] = {}
        users[user]['password'] = password
        users[user]['First_Name'] = bar[2]
        users[user]['Last_Name'] = bar[3]
        users[user]['contributions'] = bar[5]
    return users

#story dict builder
def dict_story():
    f="util/bestsite.db"
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
    if (username in userpass or  password1 != password2):
        return False
    command = "INSERT INTO users VALUES('"+ username + "','" + passw + "','" + first_name + "', '" + last_name + "','" + email + "', 'none')"
    c.execute(command)
    db.commit()
    db.close()
    return True

##FXN FOR CREATING NEW STORIES
## returns true if story successfully added to database
def add_story(wikiname, content, contributor):
    f="bestsite.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    storydict = dict_story()
    ##If already exists, u cant make it
    if (wikiname in storydict):
        return False
    command = "INSERT INTO stories VALUES('"+ wikiname + "','" + content + "','" + content + "', '" + content  + "','" + contributor + "')"
    c.execute(command)
    db.commit()
    db.close()
    return True

###########################
#Story Helper fxns
############################
#returns content of story

def content(story):
    wow = dict_story()
    return wow[story]['content']

#shows working version of story

def workingversion(story):
    wow = dict_story()
    return wow[story]['working_version']


#returns contributors of story

def contributors(story):
    wow = dict_story()
    return wow[story]['contributors']

#returns last edit in story

def lastupdate(story):
    wow = dict_story()
    return wow[story]['last_update']

################################
#USER HELPER FXNS
################################

#verifying user and pass for login

def verify_user(username, password):
    userpass = dict_user_pass()
    if not(username in userpass):
        return False
    ##verifying pass w database
    if(userpass[username]['password'] == sha1(password).hexdigest()):
        return True
    return False

#return user contributions

def contributions(user):
        userpass = dict_user_pass()
        return userpass[user]['contributions']

#testing zone
'''
print(workingversion("My life"))
print(contributors("My life"))
print(lastupdate("My life"))
print(content("My life"))
print(contributions('dasha'))
'''


#==========================================================
#db.commit() #save changes
#db.close()  #close database'''
