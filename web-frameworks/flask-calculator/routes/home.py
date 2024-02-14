from __init__ import *

@home.route("/")
def index():
    return render_template("main.html", css = url_for("static", filename="styles.css"), sample_text = "LOL")