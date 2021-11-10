from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def funct():
    return "Welcome..."

@app.route("/temprunning")
def tempRunning():
    return render_template("index.html")

app.run(debug=True)