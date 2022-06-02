
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return '<h1>You are logged in</h1>'
    
if __name__ == '__main__':
    app.run()
