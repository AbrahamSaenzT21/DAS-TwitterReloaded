from app import app, db
from models import User, Tweet, Thread, Event

# create an application context
with app.app_context():

    db.drop_all()

    # create database tables
    db.create_all()

    # add some data to the database
    user1 = User(username='Alice', password='Alice2020')
    user2 = User(username='Bob', password='Bob444')
    user3 = User(username='Charlie', password='12345Charlie')
    user4 = User(username='admin', password='1234')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.commit()

    tweet1 = Tweet(user_id=user1.id, content='Hello World!')
    tweet2 = Tweet(user_id=user2.id, content='This is a test.')
    tweet3 = Tweet(user_id=user3.id, content='Flask is awesome!')

    db.session.add(tweet1)
    db.session.add(tweet2)
    db.session.add(tweet3)
    db.session.commit()

    event1 = Event(user_id=user1.id, type='create_tweet')
    event2 = Event(user_id=user2.id, type='create_tweet')
    event3 = Event(user_id=user1.id, type='create_thread')
    event4 = Event(user_id=user3.id, type='create_tweet')

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.commit()

    thread1 = Thread(user_id=1, tweet_id=1, content="This is a thread!")
    thread2 = Thread(user_id=2, tweet_id=2, content="This is a thread!")
    thread3 = Thread(user_id=3, tweet_id=3, content="This is a thread!")

    db.session.add(thread1)
    db.session.add(thread2)
    db.session.add(thread3)
    db.session.commit()

