from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html", css = url_for("static", filename="styles.css"), sample_text = "Hehe")

@app.route("/blah", methods=['POST', 'GET'])
def ah():
    if request.method == "GET":
        print("aaa")
        return render_template("main.html", css = url_for("static", filename="stylesblah.css"), sample_text = "Lmao")
    if request.method == "POST":
        print("doing stuff with \"" + request.json['sheesh'] + "\"")
        return request.json['sheesh'] + " :3"

if __name__ == "__main__":
    app.run()