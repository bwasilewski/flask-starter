from flask import Flask, render_template, flash, redirect, request, session, abort
from flask_pymongo import PyMongo, ObjectId
import os

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def index():
    users = mongo.db.users.find()
    if not session.get('logged_in'):
        return render_template('login.html', title="Please log in")
    else:
        return render_template('index.html', title="Welcome", users=users)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['field-password'] == 'password' and request.form['field-email'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()


@app.route('/logout', methods=['POST'])
def logout():
    session['logged_in'] = False
    return index()


@app.route('/register')
def register():
    return render_template('register.html', title="Please fill out the form")


@app.route('/createuser')
def createuser():
    return register()


@app.route('/newuser', methods=['POST'])
def newuser():
    if request.form['field-password'] != '' and request.form['field-email'] != '':
        mongo.db.users.insert_one({
            'email': request.form['field-email'],
            'password': request.form['field-password'],
            'namefirst': request.form['field-fname'],
            'namelast': request.form['field-lname'],
            'age': request.form['field-age']
        })

    return index()


@app.route('/edituser/<userid>')
def edituser(userid=None):
    user = mongo.db.users.find_one({'_id': ObjectId(userid)})
    return render_template('edituser.html', title="Please modify the user", user=user)


@app.route('/useredited', methods=['POST'])
def useredited():
    mongo.db.users.update_one({'_id': ObjectId(request.form['field-id'])}, {
        '$set': {
            'email': request.form['field-email'],
            'password': request.form['field-password'],
            'namefirst': request.form['field-fname'],
            'namelast': request.form['field-lname'],
            'age': request.form['field-age']
        }
    }, upsert=False)

    return index()


@app.route('/removeuser', methods=['POST'])
def removeuser():
    mongo.db.users.delete_one({'_id': ObjectId(request.form['radio-delete'])})
    return index()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
