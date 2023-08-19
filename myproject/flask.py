from flask import Flask
from hello import src/hello
app = Flask(__name__)

@app.route("/")
def hello_world():
    hello()
    return "<p>Hello, World!</p>"