from decemberblog import app,db
from flask import render_template,request, redirect, url_for
from decemberblog.forms import SignupForm,LoginForm

# From Werkzeug for Security Import
from werkzeug.security import check_password_hash

# Import for Flask-Login
from flask_login import login_user, current_user

# User Model Import
from decemberblog.models import User

#Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Sign Up Route
@app.route("/signup",methods=["GET","POST"])
def signup():
    signupForm = SignupForm()
    if request.method == "POST":
        username = signupForm.username.data
        email = signupForm.email.data
        password = signupForm.password.data
        print(username,email,password)

        # Add Form Data to User Model Class(AKA DATABASE)
        # First - Import User Model(Above)
        # Second - Open a database Session, then add our data
        # Last - Commit data and close the session for the database

        user = User(username,email,password)
        db.session.add(user) # Start communication with Database
        db.session.commit() # Save Data to Database and Close Session


    return render_template("signup.html",signupform = signupForm)

# Login Route
@app.route("/login", methods=["GET","POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        # Find out who the logged in user currently is
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    else:
        print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)