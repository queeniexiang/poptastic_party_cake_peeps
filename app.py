from flask import Flask, flash, session, url_for, redirect, render_template, request
from util import table_helper
import sqlite3
import os

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

###############################################
#INITIAL PAGES
###############################################
@app.route("/")
def landing():
	print session;
	if "username" in session:
		return redirect("/homepage")
	return render_template("index.html")

@app.route("/homepage")
def homepage():
        return render_template('homepage.html')

        
###############################################
#LOGGING IN
###############################################
@app.route("/loggit")
def logged():
        
        #This part checks if your user+pw is correct.
        if "username" in request.args and session["username"] == "test":
                return redirect("/homepage")

        username = ""
        password = ""

        if "user" in request.args and "passo" in request.args:
		username = request.args["user"].lower()
		password = request.args["passo"]
	if not table_helper.verify_user(username, password): #auth(username,password,userpass)==-1:
		flash("Bad info!")			
       # if password != "abc123": #auth(username,password,userpass)==0:
	#	flash("Bad password!")
	if (table_helper.verify_user(username, password)):
              session["username"] = username
	      return redirect("/homepage")

        return render_template("index.html")
	#return render_template("loggedin.html")

###############################################
#REGISTRATION ROUTES
###############################################

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method=="POST":
		return request.form['user']
	return render_template('register.html')


@app.route('/register_redirect', methods=["GET", "POST"])
def register_redirect():
    user = request.form["user"]
    email = request.form["email"]
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    passo = request.form["passo"]
    rpasso = request.form["repeatpasso"]
	#Still needs work
    if table_helper.add_user(user, passo, rpasso, first_name, last_name , email):
            flash('Success! Redirecting to the home page') 
            return redirect("/homepage")
    else:
            flash('Error, please try again. Redirecting to the register page') 
	    return render_template('register.html') 
    return user + ", " + email + ", " + passo + ", " + rpasso              


###############################################
#TESTING LAND
###############################################

#IF user chooses to read stories:
@app.route("/listofstories")
def read():
        return render_template('listofstories.html', stories=[1,2,3,4,5,6,7,8,9])
###############################################
#UNFINISHED LAND
###############################################
'''
@app.route('/shainatesting') #Phasing this out for actual routes
def testing():
	testmode = "list"
	if testmode == "read":
		return render_template('read.html',title="this is a title", updates=[{'user':"Caligula", 'text': 'idk roman emperors are cool'}, {'user':'alexander', 'text':'he was kind of great'}])
	if testmode == "success":
		return render_template('success.html', whathappened="updated")
	if testmode == "list":
		return render_template('listofstories.html', stories=[1,2,3,4,5,6,7,8,9])
	return "nope"
'''
@app.route('/readstory')
def readstory(updates=None):
    if updates == None:
		updates = [{'user':"Caligula", 'text': 'idk roman emperors are cool'}, {'user':'alexander', 'text':'he was kind of great'}]
    return render_template('read.html',title="this is a title", updates=updates)

#This is the function for validating the new user

'''
#IF user chooses to read stories:
@app.route("/listofstories")
def read():
        return render_template('listofstories.html', stories=[1,2,3,4,5,6,7,8,9])

@app.route('/createstory',methods=["GET", "POST"])
def createstory():
	if request.method == "POST":
		return render_template('success.html',whathappened="created")
	return render_template("newstory.html")

@app.route('/updatestory', methods=["GET", "POST"]) #I didn't copy create, I just rewrote it
def updatestory():
	samplestory = {
		'title':'once upon a time',
		'text':'Ipsum tempor elit culpa cupidatat quis et laborum tempor nostrud voluptate nisi cupidatat. Ad fugiat sit laborum in consectetur ullamco ut esse. Ut eiusmod aliquip minim commodo id deserunt officia magna anim ut veniam ipsum laborum. Lorem duis ea elit ullamco sint est laborum enim sint.'
	}
	if request.method == "POST":
		return render_template('success.html', whathappened="updated")
        return render_template("update.html",story=samplestory)
'''

if __name__ == "__main__":
    app.debug = True
app.run()
