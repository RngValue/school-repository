from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html", title = "haha")

if __name__ == "__main__":
    app.run()