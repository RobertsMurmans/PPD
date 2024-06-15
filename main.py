from flask import Flask, render_template, request, session, redirect, jsonify, json
from data import *
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask('app')
app.secret_key = os.getenv('Key')
app.config['FILE_UPLOAD'] = 'C:/Users/Fark/Documents/GitHub/PPD/filers'


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
    if request.method == 'POST':
        return redirect("/")
    return render_template('home.html', swap="Upload", swapLink="/upload")


@app.route('/upload', methods=('GET', 'POST'))
def UploadPage():
    if 'login' not in session or session['login'] == False:
        session['login'] = False
        return redirect('/login')
    
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file.filename == '':
                print("Invalid filename")
                return redirect(request.url)
            basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(basedir, app.config['FILE_UPLOAD'], file.filename))
            upload(os.path.join(basedir, app.config['FILE_UPLOAD'], file.filename), file.name, session['id'], file.filename)
        except TypeError:
            print(TypeError)
            return redirect("/")
        else:
            return redirect("/homepage")

    return render_template('upload.html', swap="Home", swapLink="/homepage")


@app.route('/logout', methods=('GET', 'POST'))
def LogOut():
    session['login'] = False
    return redirect('/')


app.run(host='0.0.0.0', port=81)
