from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    number = 0
    if request.args.get("erst_nummer") != None and request.args.get("zweit_nummer") != None and request.args.get("operation"):
        match(request.args.get("operation")):
            case "sub":
                number = float(request.args.get("erst_nummer")) - float(request.args.get("zweit_nummer"))
            case "mul":
                number = float(request.args.get("erst_nummer")) * float(request.args.get("zweit_nummer"))
            case "div":
                number = float(request.args.get("erst_nummer")) / float(request.args.get("zweit_nummer"))
            case _:
                number = float(request.args.get("erst_nummer")) + float(request.args.get("zweit_nummer"))
    return render_template("main.html", css = url_for("static", filename="styles.css"), result = number)

@app.route("/bruw", methods=["GET", "POST"])
def bruw():
    match(request.method):
        case "GET":
            return "Bruh"
        case "POST":
            return "Bruw: {}".format(request.form["bruh"])

if __name__ == "__main__":
    app.run()