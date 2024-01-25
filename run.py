from app import app
from db import db
from models.source import Source
from models import article
from threading import Thread
import time
import feed
import routes

with app.app_context():
    db.create_all()

# update loop in the background
def update_loop():
    while True:
        with app.app_context():
            query = Source.query
            print(query.all())
            for source in query.all():
                try:
                    update_source(source)
                except Exception as e:
                    print(f"Error updating source:-> {source.link}: {e}")
                    continue  # If there's an error, continue to the next source
        time.sleep(105)

def update_source(source):
    print('this is the source link: ' + source.link)
    parsed = feed.parse(source.feed)
    feed_articles = feed.get_articles(parsed)
    # Use the SQLAlchemy model method to insert articles
    
    article.Article.insert_from_feed(source.id, feed_articles)
    print('This is the source id: ' + str(source.id))

# Start the background thread
thread = Thread(target=update_loop)
thread.start()

# Run the Flask app
app.run(port=5000, debug=True)
