from flask import Flask, session, url_for, redirect, render_template, request

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
		if username == "test" #in the database: 
			print "THE USERNAME HAS BEEN VALIDATED \n\n"
			if password == "abc123":  #in the database: 
			        print "THE PASSWORD HAS BEEN VALIDATED \n\n"
				session["username"] = #user_username
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

@app.route('/shainatesting')
def testing():
	testmode = "list"
	if testmode == "read":
		return render_template('read.html',title="this is a title", updates=[{'user':"Caligula", 'text': 'idk roman emperors are cool'}, {'user':'alexander', 'text':'he was kind of great'}])
	if testmode == "success":
		return render_template('success.html', whathappened="updated")
	if testmode == "list":
		return render_template('listofstories.html', stories=[1,2,3,4,5,6,7,8,9])
	return "nope"

@app.route("/register")
def register():
        #If form has been submited:
        #blah

        #If registering has been successful:
        #Return /listofstories

        #Else:
        #return render_template("register.html")

'''@app.route("/wrong")
def u_messed_up():
    return render_template("errorpage.html", bad = request.args.get("err"))'''

app.route("/homepage")
def homepage():
        #return render_template('homepage.html')


#IF user chooses to read stories:         
app.route("/listofstories") 
def read():
        return render_template('listofstoriess.html', stories=[1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
    app.debug = True
app.run()
