from flask import Flask
from src.hello import hello,string_test
app = Flask(__name__)

@app.route("/<number>")
def hello_world(number):
    print(number, type(number))
    value = int(number)
    print(value, type(value))
    return string_test()+hello(value)