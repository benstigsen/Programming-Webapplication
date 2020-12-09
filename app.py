from flask import Flask, redirect, render_template, request, url_for
from language import Language
from interpret import interpret

app = Flask(__name__)

languages = []

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

@app.route("/interpreter/<language>", methods=["GET", "POST"])
def interpreter(language):
	if request.method == "POST":
		for lang in languages:
			if lang.name == language:
				code = request.form["codearea"]
				output = interpret(lang, request.form["codearea"])
				return render_template("interpreter.html", language=lang, code=code, output=output)

	for lang in languages:
		if lang.name == language:
			code = lang.generateExample()
			return render_template("interpreter.html", language=lang, code=code, output=[])

	return redirect("../../overview")
