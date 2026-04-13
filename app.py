from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return f"<h1>Hello World!</h1><p>Running on Python {sys.version}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)