
# First Flask app to demo on route and decorator

from flask import Flask

app = Flask(__name__)

#default decorator
#web page for default page https://xxxxx.com/
@app.route('/')
def index():
    return 'Hello from Flask me!'

#web page for https://xxxxx.com/information
@app.route('/information')
def info():
    return '<h1>Puppies are cute</h1>'
  
if __name__ == '__main__':
    app.run
