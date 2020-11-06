from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('home/')
def homepage():
    return "<h1>homepage2</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)