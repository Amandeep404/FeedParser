from flask import Flask , redirect, request, abort, render_template
from app import app
from models.article import Article
from models.source import Source
from db import db
import feed

@app.route('/', methods=['GET'])
def index_get():
    query = Article.query.filter(Article.unread == True).order_by(
        Article.date_added.desc()
        )
    articles = query.all()
    #return str([article.title for article in articles])
    return render_template('index.html', articles=articles)

@app.route('/read/<int:article_id>', methods=['GET'])
def read_article_get(article_id):
    article = Article.query.get(article_id)
    article.unread = False  
    db.session.commit()
    return redirect(article.link)

@app.route('/sources', methods=['GET'])
def sources_get():
    query = Source.query.order_by(Source.title)
    sources = query.all()
    #return str([source.title for source in sources])
    return render_template('sources.html', sources=sources)

@app.route('/sources', methods=['POST'])
def sources_post():
    feed_url = request.form['feed_url']
    parsed = feed.parse(feed_url)
    feed_source = feed.get_source(parsed)
    source = Source.insert_from_feed(feed_url, feed_source)
    feed_articles = feed.get_articles(parsed)
    Article.insert_from_feed(source.id, feed_articles)
    return redirect('/sources')