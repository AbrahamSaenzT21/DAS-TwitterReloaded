from flask import Flask, render_template, request, redirect, url_for
from models import db
from controllers import TweetController, ThreadController, UserController, EventController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter.db'
db.init_app(app)

tweet_controller = TweetController()
thread_controller = ThreadController()
user_controller = UserController()
event_controller = EventController()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_controller.get_user_by_username(username)
        if user and user.verify_password(password):
            return redirect(url_for('dashboard', username=username))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/dashboard/<string:username>')
def dashboard(username):
    user = user_controller.get_user_by_username(username)
    if not user:
        return 'User not found'
    tweets = tweet_controller.get_latest_tweets(10)
    return render_template('dashboard.html', user=user, tweets=tweets)


@app.route('/tweet', methods=['POST'])
def create_tweet():
    content = request.form['content']
    user_id = request.form['user_id']
    tweet_controller.create_tweet(content, user_id)
    return redirect(url_for('dashboard', username=user_controller.get_user(user_id).username))


@app.route('/thread', methods=['POST'])
def create_thread():
    content = request.form['content']
    user_id = request.form['user_id']
    tweet_id = request.form['tweet_id']
    thread_controller.create_thread(content, user_id, tweet_id)
    return redirect(url_for('dashboard', username=user_controller.get_user(user_id).username))


@app.route('/reply', methods=['POST'])
def reply():
    content = request.form['content']
    user_id = request.form['user_id']
    thread_id = request.form['thread_id']
    thread_controller.reply(content, user_id, thread_id)
    return redirect(url_for('dashboard', username=user_controller.get_user(user_id).username))


if __name__ == '__main__':
    app.run(debug=True)
