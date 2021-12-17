
from enum import unique
from flask import Flask, render_template, request, flash,url_for,redirect
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.secret_key='abc'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:ashwini@localhost/flask-table'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def __repr__(self)->str:
        return f"{self.id}-{self.name}-{self.email}"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET','POST'])
def register():
    error=""
    if(request.method=='POST'):
        name=request.form['name']
        email=request.form['email']
        data=User(name=name, email=email)
        try:
          db.session.add(data)
          db.session.commit()
          flash("successfully registered")
          return redirect(url_for('index'))
        except IntegrityError:
            error="Email id already exists"
            db.session.rollback()
    return render_template('register.html',error=error)

@app.route("/attendees")
def attendees():
    allData=User.query.all()
    return render_template('attendees.html',allData=allData)

if __name__=="__main__":
    app.run(debug=True)