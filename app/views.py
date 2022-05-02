from flask import render_template
from app import app

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    title = 'The E-news'
    return render_template('index.html',title = title)

@app.route('/articles/<articles_id>')
def  articles(articles_id):
    """
    view function that displays details of the articles from a particular source
    """
    return render_template('articles.html',id = articles_id)
    