from flask import Flask
from models import db
from controllers import UserController, TweetController, ThreadController, EventController

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter.db'
    db.init_app(app)

    tweet_controller = TweetController()
    thread_controller = ThreadController()
    user_controller = UserController()
    event_controller = EventController()

    return app