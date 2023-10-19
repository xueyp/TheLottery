import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
dbdir= os.path.join(basedir,'../..')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(dbdir,'dball.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Dball(db.Model):
    __tablename__ = 'dball'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    r1 = db.Column(db.Integer)
    r2 = db.Column(db.Integer)
    r3 = db.Column(db.Integer)
    r4 = db.Column(db.Integer)
    r5 = db.Column(db.Integer)
    r6 = db.Column(db.Integer)
    b = db.Column(db.Integer)

    def __repr__(self):
        return f"<Dball(id,r1,r2,r3,r4,r5,r6,b)>"


@app.route('/')
def index():
    balls = Dball.query.all()
    return render_template('index.html', balls=balls)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
