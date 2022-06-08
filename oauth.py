#oauth.py --> home.html --> welcome.html
import os
from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
#app.secret_key = 'mysecret'
#app.config['SECRET_KEY'] = 'mysecret'

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")

#blueprint = make_google_blueprint(client_id='479217618451-s9v5792onqdeuolnbuto1vh14vv02b6b.apps.googleusercontent.com',
#                client_secret='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',scope=['profile','email'])

#app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    #return internal server error if not logged in
    #resp = google.get('/oauth2/v2/userinfo')
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok,resp.text
    email = resp.json()['email']
    return render_template('welcome.html',email=email)

@app.route('/login')
def login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    #resp = google.get('/oauth2/v2/userinfo')
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    #return "You are {email} on Google".format(email=resp.json()["email"])    
    email = resp.json()['email']
    #print("Here's the content of my response: " + resp.content)
    
    #resp = example_blueprint.session.get("/user")
    #assert resp.ok
    #print("Here's the content of my response: " + resp.content)
    return render_template('welcome.html',email=email)
