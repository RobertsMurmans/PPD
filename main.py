from flask import Flask, render_template, request, session, redirect, jsonify, json
from data import *
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask('app')
app.secret_key = os.getenv('Key')


@app.route('/')
def Index_page():
    if 'login' not in session or session['login'] == False:
        session['login'] = False
        return redirect('/login')
    return redirect('/homepage')


@app.route('/login', methods=('GET', 'POST'))
def Login_page():
    if request.method == 'POST':
        username = request.form['user_ID']
        password = request.form['password']
        if confirmPass(username, password):
            session['username'] = username
            session['id'] = getID(username)
            session['login'] = True
            return redirect('/homepage')
        return render_template('login.html', fail = True, login = True)
    return render_template('login.html', fail = False, login=True)


@app.route('/homepage', methods=('GET', 'POST'))
def Homepage():
    if 'login' not in session or session['login'] == False:
        session['login'] = False
        return redirect('/login')
    return render_template('home.html')


app.run(host='0.0.0.0', port=81)