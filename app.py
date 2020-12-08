from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	return redirect("/create")

@app.route("/create", methods=["GET", "POST"])
def create():
	return render_template("create.html")
	#return render_template("index.html", test="Hello World")


