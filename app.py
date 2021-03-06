from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10000), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return '<Task %r>' % self.id
    
    
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)