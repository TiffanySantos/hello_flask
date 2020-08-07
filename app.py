from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

