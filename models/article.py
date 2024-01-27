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
        for article_data in feed_articles:
            # Extract relevant data from feed_articles and create an Article instance
            title = article_data.get('title', '???')
            body = article_data.get('summary', '???')
            link = article_data.get('link', '???')
            guid = article_data.get('id', '???')
            #date_published = datetime.utcnow()
            date_published = article_data.get('date_published', None)

            # Check if the article with the same guid already exists for the source
            existing_article = cls.query.filter_by(source_id=source_id, guid=guid).first()
            if existing_article:
                # If it exists, update the existing article (e.g., update unread status)
                existing_article.unread = True  # Update as needed
            else:
                # If it doesn't exist, create a new article and add it to the session
                new_article = cls(
                    title=title,
                    body=body,
                    link=link,
                    guid=guid,
                    source_id=source_id,
                    date_published=date_published,
                )
                db.session.add(new_article)

        # Commit changes to the database
        db.session.commit()