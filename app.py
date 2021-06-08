import os
from flask import Flask,render_template
from jinja2 import environment

app = Flask(__name__)

@app.get('/hello')
def hello():
    return 'hello world!!!'

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/env/<envname>')
def getEnv(envname):
    return os.environ.get(envname)

# if __name__ == "__main__":
#     app.run(debug=True)
