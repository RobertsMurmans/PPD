from flask import Flask, render_template, request, session, redirect, jsonify, json
from data import *
import os


app = Flask('app')
app.secret_key = "poop"


@app.route('/')
def Index_page():
    if 'login' not in session or session['login'] == False:
        session['login'] = False
        return redirect('/login')
    return render_template('home.html')


@app.route('/login', methods=('GET', 'POST'))
def Login_page():
    if request.method == 'POST':
        userID = request.form['user_ID']
        password = request.form['password']
        print(userID, " and ", password)
        if checkIfOnServer(userID, password):
            session['userID'] = userID
            session['password'] = password
            session['login'] = True
            return redirect('/')
    return render_template('login.html')


app.run(host='0.0.0.0', port=81)