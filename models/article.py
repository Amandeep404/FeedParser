from db import db
from datetime import datetime
import time

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    guid = db.Column(db.String(255), nullable=False)
    unread = db.Column(db.Boolean, default=True, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    source = db.relationship('Source', backref=db.backref('articles', lazy=True))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_published = db.Column(db.DateTime)
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )

    @classmethod
    def insert_from_feed(cls, source_id, feed_articles):
        conn = db.engine.connect()

        stmt = Article.__table__.insert().prefix_with('OR IGNORE')  # Updated this line
        articles = []
        
        for article in feed_articles:
            if article['published'] is None:
                continue
            articles.append({
                'title': article['title'],
                'body': article['summary'],
                'link': article['link'],
                'guid': article['id'],
                'source_id': source_id,
                'date_published': datetime.utcfromtimestamp(time.mktime(article['published'])),
            })
        conn.execute(stmt, articles)
        conn.close()
