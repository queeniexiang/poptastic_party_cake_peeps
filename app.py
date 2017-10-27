from flask import Flask, session, url_for, redirect, render_template, request
from util.table_helper import *
import sqlite3
import os

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def landing():
	print session;
	if "username" in session:
		return redirect("/homepage")
	return render_template("index.html")


#Where all the fun login stuff happens
@app.route("/loggit")
def logged(user = ""):
        #This part checks if your user+pw is correct.
        if user == "":
		username = request.args["user"].lower()
		password = request.args["password"]
		print "BOUTTA CHECK THAT USERNAME \n\n"
		if username == "test": #in the database:
			print "THE USERNAME HAS BEEN VALIDATED \n\n"
			if password == "abc123":  #in the database:
			        print "THE PASSWORD HAS BEEN VALIDATED \n\n"
				session["username"] = user_username
				print "Does we makes it?\n\n"
				return redirect("/homepage")
			else:
			        flash("Incorrect password, please try again.")
		else:
			flash("Incorrect username, please try again.")

	#If you already have a username, it brings you here
	#WHAT DOES THIS DO
        else:
		return redirect("/listofstories")

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

@app.route('/readstory')
def readstory(updates=None):
    if updates == None:
		updates = [{'user':"Caligula", 'text': 'idk roman emperors are cool'}, {'user':'alexander', 'text':'he was kind of great'}]
    return render_template('read.html',title="this is a title", updates=updates)

#This is the function for validating the new user
@app.route('/register_redirect', methods=["GET", "POST"])
def register_redirect():
    user = request.form["user"]
    email = request.form["email"]
    passo = request.form["passo"]
    rpasso = request.form["repeatpasso"]
	#Still needs work
    if add_user(user, passo, 'first_name', 'last_name', email):
		return redirect("/register")
    else:
		return 'something went wrong'
    return user + ", " + email + ", " + passo + ", " + rpasso

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method=="POST":
		return request.form['user']
	return render_template('register.html')
        #If form has been submited:
        #blah

        #If registering has been successful:
        #Return /listofstories

        #Else:
        #return render_template("register.html")

#'''@app.route("/wrong")
#def u_messed_up():
#    return render_template("errorpage.html", bad = request.args.get("err"))'''

@app.route("/homepage")
def homepage():
	pass
        #return render_template('homepage.html')


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

if __name__ == "__main__":
    app.debug = True
app.run()
