# This example is to show the interaction between the Flask APIs which act as the LOGIC Layer and the template folder (HTML) which act as the PRESENTATION Layer
Remember to change the Procfile to reflect the python file to load eg "web: gunicorn abc: app". In this example abc is referring to abc.py

# 1) Example on your first Flask application (firstFlask.py)
# 2) Example on your Flask and HTML interaction (app.py --> post.html --> index.html)
# 3) Example on creating simple login page (login.py --> login.html)
# 4) Example on Google OAuth (oauth.py --> home.html --> welcome.html)
Flask-Dance Example App: Google Edition
This repository provides an example of how to use Flask-Dance to connect to Google as an OAuth client. The example code is in google.py -- all the other files in this repository are secondary. You can run this example code locally, or deploy it to Heroku for free to see how it runs in a production-style environment.

Heroku Installation
Heroku is a great way to get up and running fast, and you don't even need to open the terminal!

Step 1: Deploy to Heroku
It's easy, and it's free! Just click on this button:

Deploy to Heroku

You can leave all the fields at their default values: we'll fill them in later. The only thing that matters right now is the app name, and Heroku will autogenerate a name for you if you leave that field blank. Using an autogenerated name is perfectly fine, just take note of what it is.

Note that your app isn't functional yet, and if you try to visit it right now, you'll end up at a Google 404 page. That's OK, we're not done yet!

Step 2: Get OAuth credentials from Google
Visit the Google Developers Console at https://console.developers.google.com and create a new project. In the "APIs & auth" section, click on "Credentials", and then click the "Create a new Client ID" button. Select "Web Application" for the application type, and click the "Configure consent screen" button. Put in your application information, and click Save. Once you’ve done that, you’ll see two new fields: "Authorized JavaScript origins" and "Authorized redirect URIs". You need to set the correct authorized redirect URI for the OAuth system to work correctly.

To set the correct authorized redirect URI, you'll need that app name from Heroku. The correct authorized redirect URI is https://APPNAME.herokuapp.com/login/google/authorized. For example, if Heroku assigned you an app name of peaceful-lake, your authorization callback URL must be https://peaceful-lake.herokuapp.com/login/google/authorized. Once you've put that in, click "Create Client ID". Google will give you a client ID and client secret, which we'll use in the next step.

Step 3: Give OAuth credentials to your app on Heroku
Go to Heroku and visit the settings page for your app. (You can get there from your Heroku dashboard, or by clicking on the "Manage App" button after the deploy step is finished.) On that page, there should be a section called "Config Variables" where you can manage the config vars for your application. You'll need click the "Reveal Config Vars" button to see which variables are available, and then the "Edit" button to allow you to change these variables.

Take the client ID you got from Google, and paste it into the "VALUE" field next to the GOOGLE_OAUTH_CLIENT_ID field, replacing the dummy value that was there before. Similarly, take the client secret you got from Google, and paste it into the "VALUE" field next to the GOOGLE_OAUTH_CLIENT_SECRET field, replacing the dummy value that was there before. Click the "Save" button when you're done.

Step 4: Visit your app and login with Google!
Your app name from Heroku will determine the URL that your app is running on: the URL will be https://APPNAME.herokuapp.com. For example, if Heroku assigned you an app name of peaceful-lake, your app will be available at https://peaceful-lake.herokuapp.com. Visit that URL, and you should immediately be redirected to login with Google!
