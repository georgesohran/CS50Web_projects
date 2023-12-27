from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

from werkzeug.security import check_password_hash, generate_password_hash

import os.path
import sqlite3

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return render_template(f"{session["user_type"]}/index.html")


@app.route("/register", methods=["POST","GET"])
def register():
    session.clear()

    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()
    if request.method == "POST":
        password = request.form.get("password")
        password2 = request.form.get("password2")
        name = request.form.get("name")
        type = request.form.get("type")
        if type == "teacher":
            subject = request.form.get("subject")

        if not password or not password2 or not name or not type:
            return render_template("register.html", messege="missing password or name or type")
        if type not in ["teacher", "student"]:
            return render_template("register.html", messege="invalid type")
        if password != password2:
            return render_template("register.html", messege="invalid repeat password")

        if type == "teacher":
            subject_id = db.execute("SELECT id FROM subjects WHERE name == ?", (subject,)).fetchall()
            subject_id = subject_id[0]
            subject_id = [i for i in subject_id][0]

            if (subject,) not in db.execute("SELECT name FROM subjects").fetchall():
                return render_template("register.html",messege="invalid subject")

            cur.execute("INSERT INTO teachers (name,password_hash,subject_id) VALUES(?,?,?)",(name, generate_password_hash(password), subject_id))
            db.commit()

        elif type == "student":
            cur.execute("INSERT INTO students (name,password_hash) VALUES(?,?)", (name, generate_password_hash(password)))
            db.commit()

        session["user_id"] = cur.execute(f"SELECT id FROM {type}s WHERE name == ?", (name,)).fetchall()

        session["user_type"] = type

        db.close()

        return redirect("/")

    else:
        db.close()

        return render_template("register.html", messege="OK")



@app.route("/login", methods=["POST","GET"])
def login():
    session.clear()

    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        type = request.form.get("type")
        password =request.form.get("password")

        if type not in ["teacher", "students"]:
            return render_template("login.html", messege="invalid type")

        all_names = 


    else:
        db.close()
        return render_template("login.html", messege="OK")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")



