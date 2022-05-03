from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    sources = get_sources()
    breaking_news = get_breaking_news()
    title = 'The E-news'
    return render_template('index.html',title = title,sources=sources,breaking_news=breaking_news)

@app.route('/articles/<articles_id>')
def  articles(articles_id):
    """
    view function that displays details of the articles from a particular source
    """
    return render_template('articles.html',id = articles_id)
    