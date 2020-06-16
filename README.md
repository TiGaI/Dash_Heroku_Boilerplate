# How to run the dash
pip3 install -r requirements.txt
flask run


# Deploying your Dash app online

1. Setup account on Heroku and download Heroku CLI utility
2. Navigate to this folder
3. Commit this folder to Git

4. 'heroku login' and type in your credentials
5. 'heroku create -n [YOUR-APP-NAME]' where YOUR-APP-NAME refers to the title of your Dash app
6. 'heroku git:remote -a [YOUR-APP-GIT-URL]' where YOUR-APP-GIT-URL refers to the Git link returned by 5.
7. 'git push heroku master' will deploy your app to Heroku
8. 'heroku ps:scale web=1' will create a Dyno and make your app live
