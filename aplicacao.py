from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def principal():
    return render_template("brasileira.html")
@app.route("/norte")
def nordestina():
    return render_template("nordestina.html")
@app.route("/sul")
def sulista():
    return render_template("/html/sulista.html")

app.run(debug=True)


