from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html", css = url_for("static", filename="styles.css"), sample_text = "Hehe")

@app.route("/blah")
def ah():
    return render_template("main.html", css = url_for("static", filename="stylesblah.css"), sample_text = "Hehe")

if __name__ == "__main__":
    app.run()