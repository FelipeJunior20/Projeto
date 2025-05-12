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
        senha = request.form["password"]
        confirmar = request.form["confirmPassword"]
        if senha != confirmar:
            flash("❌ As senhas não coincidem. Tente novamente.", "error")
            return redirect(url_for("newpasswordpage"))
        else:
            flash("✅ Senha alterada com sucesso!", "success")
        return redirect(url_for("newpasswordpage"))
    return render_template("newPasswordPage.html")