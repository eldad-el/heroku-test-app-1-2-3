from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(username=test)



if __name__ == '__main__':
    app.run(threaded=True, port=5000)