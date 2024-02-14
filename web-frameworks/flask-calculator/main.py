from flask import Flask
from routes.home import home
from routes.blah import blah
app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(blah)

if __name__ == "__main__":
    app.run()