from models import Tweet, Thread, User, Event, db


class TweetController:
    def create_tweet(self, content, user_id):
        user = User.query.get(user_id)
        tweet = Tweet(content=content, user=user)
        db.session.add(tweet)
        db.session.commit()

    def get_latest_tweets(self, limit):
        return Tweet.query.order_by(Tweet.timestamp.desc()).limit(limit)


class ThreadController:
    def create_thread(self, content, user_id, tweet_id):
        user = User.query.get(user_id)
        tweet = Tweet.query.get(tweet_id)
        thread = Thread(content=content, user=user, tweet=tweet)
        db.session.add(thread)
        db.session.commit()

    def reply(self, content, user_id, thread_id):
        user = User.query.get(user_id)
        thread = Thread.query.get(thread_id)
        reply = Thread(content=content, user=user, parent=thread)
        db.session.add(reply)
        db.session.commit()

    def get_latest_threads(self, limit):
        return Thread.query.order_by(Thread.timestamp.desc()).limit(limit)

    def get_most_commented_tweet(self):
        most_commented_tweet_id = db.session.query(Thread.tweet_id, db.func.count(Thread.id)).group_by(
            Thread.tweet_id).order_by(db.func.count(Thread.id).desc()).first()

        if not most_commented_tweet_id:
            return None

        return Tweet.query.filter_by(id=most_commented_tweet_id[0]).first()


class UserController:
    def create_user(self, username, password):
        user = self.get_user_by_username(username)
        if user:
            return False
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

    def get_user(self, id):
        return User.query.get(id)

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()


class EventController:
    def create_event(self, type, user_id):
        user = User.query.get(user_id)
        event = Event(type=type, user=user)
        db.session.add(event)
        db.session.commit()

    def get_event_counts(self):
        return {
            'create_tweet': db.session.query(Event).filter(Event.type == 'create_tweet').count(),
            'reply_tweet': db.session.query(Event).filter(Event.type == 'reply_tweet').count(),
            'open_app': db.session.query(Event).filter(Event.type == 'open_app').count()
        }

    def get_most_events_user(self):
        return db.session.query(Event.user_id, db.func.count(Event.id)).group_by(Event.user_id).order_by(
            db.func.count(Event.id).desc()).first()[0]

    def get_num_app_opens(self):
        return db.session.query(Event).filter(Event.type == 'open_app').count()
