from __init__ import *

@blah.route("/blah")
def index():
    return render_template("main.html", css = url_for("static", filename="stylesblah.css"), sample_text = "Hehe")