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
		#flash("Bad info!")
		pass #I had to comment it out becaus it was showing up when the user first gets redirected
       # if password != "abc123": #auth(username,password,userpass)==0:
	#	flash("Bad password!")
	if (table_helper.verify_user(username, password)):
              session["username"] = username
	      return redirect("/homepage")

      	if "submit" in request.args and request.args["submit"] == "Logout":
		session["username"] = ""
		flash("You logged out")

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
            flash('Success! Redirecting to the home page! Please log in to your new account!')
            return redirect("/loggit")
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
	stories = table_helper.get_all_stories()
	storylist = []
	return render_template('listofstories.html', stories=stories)
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
@app.route('/readstory/<story>')
def readstory(story):
	stories = table_helper.get_all_stories()
	use = ""
	for possible in stories:
		if possible['title'] == story:
			use = possible
	#return use.content
	lcpre = use['contributors'] #table_helper.string_to_dict(use['contributors'])
	lc = table_helper.string_to_dict(str(lcpre))
	#eturn lc
	#use['updates2'] = '{"test1":"test1s contribution to society","test2":"im out of clever ideas"}'
	updates = []
	for contr in lc:
		update = {}
		update['user'] = contr
		update['text'] = table_helper.string_to_dict(use['updates'])[contr]
		updates.append(update)
	#return update['user']
	return render_template('read.html',title=story, updates=updates)

#This is the function for validating the new user


#IF user chooses to read stories:
#@app.route("/listofstories")
#def read():
#        return render_template('listofstories.html', stories=[1,2,3,4,5,6,7,8,9])

@app.route('/createstory',methods=["GET", "POST"])
def createstory():
	if request.method == "POST":
		wikiname = request.form["title"]
		content = request.form["text"]
		user = ""
		if "username" in session:
			user = session["username"]
		else:
			user = "user"
		if table_helper.add_story(wikiname, content, user):
			return render_template('success.html',whathappened="created")
		else:
			return render_template('success.html',whathappened="failed to create")
	return render_template("newstory.html")

@app.route('/updatestory')
def updatestory():
        stories = table_helper.get_all_stories()
        return render_template("update_stories.html", stories = stories) 
        
@app.route('/updatestory/<storyname>')
def updatestory_story(storyname):
	stories = table_helper.get_all_stories()
	use = None
	for possible in stories:
		if possible['title'] == storyname:
			use = possible
	contributors = table_helper.string_to_dict(use['contributors'])
	updates = table_helper.string_to_dict(use['updates'])
	lastc = contributors[len(contributors)-1]
	#return lastc
	last = updates[lastc]
	return render_template("update.html", writer=lastc, text=last, title=storyname)

@app.route('/updatestory_redirect', methods=["POST"])
def updatestory_redirect():
	title = request.form['title']
	update = request.form['update']
	user = ""
	if "username" in session:
		user = session["username"]
	else:
		user = "user"
	if table_helper.update_story(title, user, update):
		return render_template("success.html", whathappened="update")
	else:
		return render_template("success.html", whathappened="failed to update")

if __name__ == "__main__":
    app.debug = True
app.run()
