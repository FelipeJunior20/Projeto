from main import app
from flask import render_template, request, redirect, url_for, flash

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

@app.route("/newPassword", methods=["POST", "GET"])
def newpasswordpage():
    if request.method == "POST":
        return redirect(url_for("loginpage"))
    return render_template("newPasswordPage.html")