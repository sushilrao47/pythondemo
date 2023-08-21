from flask import Flask
app = Flask(__name__)


def hello_world():
   return "hello"

@app.route('/hello1/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/product/<float:price>')
def price(price):
   return 'Price Value %f' % price


app.add_url_rule("/hello", "hello1", hello_world)
app.add_url_rule("/", "hello", hello_world)

if __name__ == "__main__":
   app.run()