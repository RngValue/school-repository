from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    number = 0
    # if request.method == "GET":
    #     number = request.form["erst_nummer"] + request.form["zweit_nummer"]
    return render_template("main.html", css = url_for("static", filename="styles.css"), result = number)

if __name__ == "__main__":
    app.run()