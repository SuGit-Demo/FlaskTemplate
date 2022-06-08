#oauth.py --> home.html --> welcome.html
from flask import Flask, redirect, url_for, render_template, session
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
blueprint = make_google_blueprint(
    client_id="479217618451-s9v5792onqdeuolnbuto1vh14vv02b6b.apps.googleusercontent.com",
    client_secret="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",
    # reprompt_consent=True,
    #offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)


if __name__ == "__main__":
    app.debug = True
    app.run()
