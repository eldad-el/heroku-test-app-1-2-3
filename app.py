from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hi</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)