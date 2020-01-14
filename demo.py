from flask import Flask, render_template

app = Flask("demo")

@app.route("/")
def home():
    return render_template("index.html")

app.run(port = "8080")