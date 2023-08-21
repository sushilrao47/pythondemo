from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/1')
@app.route('/next')
def hello_world():
   return "hello"


@app.route('/first')
def first():
   return "first"


@app.route('/sec')
def sec():
   return "sec"


if __name__ == "__main__":
   app.run()