from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("https://www.youtube.com/watch?v=7le4AGwtH94")
app.run()
