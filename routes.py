from main import app
from flask import render_template

#rotas 

@app.route("/")
def homepage():
    return render_template("homePage.html")

@app.route("/login")
def loginpage():
    return render_template("loginPage.html")

@app.route("/register")
def registerpage():
    return render_template("registerPage.html")

@app.route("/forgot")
def forgotpage():
    return render_template("forgotPage.html")