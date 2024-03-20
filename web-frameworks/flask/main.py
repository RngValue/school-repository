from flask import *
from password import *
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
            if len(request.form["password"]) >= 8:
                if check_similarity(request.form["password"]):
                    return "bruw: {}<br/>Your password is this safe: {}/5<br/>your password matches with another one (not saved)".format(request.form["password"], check_safety(request.form["password"]))
                else:
                    return "bruw: {}<br/>Your password is this safe: {}/5<br/>your password matches with neither of your passwords (saved)".format(request.form["password"], check_safety(request.form["password"]))
            return "bruw: {}<br/>Your password is this safe: {}/5<br/>Password length must be atleast 8 characters long.".format(request.form["password"], check_safety(request.form["password"]))

if __name__ == "__main__":
    app.run()