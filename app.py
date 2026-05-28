from flask import Flask, render_template, url_for, session, request,redirect
USERNAME = ""
PASSWORD = ""
app = Flask(__name__)
app.secret_key = 'sarthi123'

@app.route("/register",methods = ["GET", "POST"])
def register():
    global USERNAME, PASSWORD
    if request.method == "POST":
        USERNAME = request.form["USERNAME"]
        PASSWORD = request.form["PASSWORD"]

        return redirect(url_for("login"))
    return render_template("register.html")
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else: 
            return render_template("login.html", error = "Invalid credentials")
    return render_template("login.html")


@app.route("/dashboard",methods = ["GET", "POST"])
def dashboard():
    if "user" not in session:
        return render_template("login.html", error = "User not in logged in")
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = weight/height ** 2

        return render_template("dashboard.html",bmi = bmi)
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)




