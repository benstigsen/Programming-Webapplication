from flask import Flask, redirect, render_template, request, url_for
from language import Language

app = Flask(__name__)

languages = []
language_current = 0

@app.route("/", methods=["GET", "POST"])
def index():
	return redirect("/create")

@app.route("/create", methods=["GET", "POST"])
def create():
	if request.method == "POST":
		languages.append(Language(request.form))
		return redirect("../overview")
	
	return render_template("create.html")
	#return render_template("index.html", test="Hello World")

@app.route("/overview")
def overview():
	return render_template("overview.html", languages=languages)

@app.route("/interpreter/<language>")
def interpreter(language):
	for lang in languages:
		if lang.name == language:
			return render_template("interpreter.html", language=lang)

	return redirect("../../overview")
