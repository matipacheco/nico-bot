# Nico-bot
The Slackbot that was supossed to give motivational frases but got fucked up in the way

### Dependencias
virtualenv nico-bot
source nico-bot/bin/activate

### Heroku
Para clonar el repositorio de Heroku
heroku git:remote -a slack-nico-bot

Para deployar, simplemente:
git push heroku master

### Levantar aplicación
export FLASK_APP=app.py
flask run