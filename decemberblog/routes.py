from decemberblog import app
from flask import render_template
from decemberblog.forms import SignupForm

#Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Sign Up Route
@app.route("/signup",methods=["GET","POST"])
def signup():
    signupForm = SignupForm()
    
    username = signupForm.username.data
    email = signupForm.email.data
    password = signupForm.password.data
    print(username,email,password)

    return render_template("signup.html",signupform = signupForm)
