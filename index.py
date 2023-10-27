from flask import Flask

app = Flask(__name__)
@app.route("/")
def homepage():
    return "https://goosadasdgle.com.br/"
app.run(debug=True)

