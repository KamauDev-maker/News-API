import urllib.request,json
from .models import Sources,Articles,Keyword,Breaking

api_Key= None
base_url= None
top_articles_url= None
keyword_url= None
breaking_news_url= None


def configure_request(app):
    global api_Key, base_url, top_articles_url, keyword_url, breaking_news_url
    api_Key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    top_articles_url = app.config["NEWS_API_TOP_ARTICLES_BASE_URL"]
    keyword_url = app.config["NEWS_API_SEARCH_KEYWORD_BASE_URL"]
    breaking_news_url = app.config["NEWS_API_BREAKING_NEWS_BASE_URL"]

def get_sources():
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format('3d022a8956c34986b22de4568f411a54')
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_results = None
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results 

def process_sources(sources_list):
    '''
    function that process the sources result and transforms them into a list of objects
    Args:
        sources_list: A list of dictionaries that contains sources details
    Returns:
           sources_results: A list of sources object   
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description =sources_item.get('description')
        url =sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        
        sources_object = Sources(id,name,description,url,category,language)  
        sources_results.append(sources_object)
    return sources_results  

def get_top_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = top_articles_url.format(id, '3d022a8956c34986b22de4568f411a54')

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(articles_list):
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        imageurl = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        url = articles_item.get('url')

        if imageurl:
            articles_object = Articles(author,title,imageurl,publishedAt,url)
            articles_results.append(articles_object)
    return articles_results

def get_keyword(keyword_name):
    search_keyword_url = keyword_url.format(keyword_name, '3d022a8956c34986b22de4568f411a54')
    with urllib.request.urlopen(search_keyword_url) as url:
        search_keyword_data = url.read()
        search_keyword_response = json.loads(search_keyword_data)

        keyword_results = None

        if search_keyword_response['articles']:
            search_keyword_list = search_keyword_response['articles']
            keyword_results = process_keyword(search_keyword_list)

    return keyword_results

def process_keyword(keyword_list):
    keyword_results = []
    for keyword in keyword_list:
        author = keyword.get('author')
        title = keyword.get('title')
        imageurl = keyword.get('urlToImage')
        publishedAt = keyword.get('publishedAt')
        url = keyword.get('url')

        if imageurl:
            keyword_object = Keyword(author,title,imageurl,publishedAt,url)
            keyword_results.append(keyword_object)

    return keyword_results

def get_breaking_news():
    get_breaking_news_url = breaking_news_url.format('3d022a8956c34986b22de4568f411a54')

    with urllib.request.urlopen(get_breaking_news_url) as url:
        get_breaking_data = url.read()
        get_breaking_response = json.loads(get_breaking_data)

        breaking_results = None

        if get_breaking_response['articles']:
            breaking_results_list = get_breaking_response['articles']
            breaking_results = process_breaking_news(breaking_results_list)

        return breaking_results

def process_breaking_news(breaking_news_list):
    breaking_results = []
    for breaking_item in breaking_news_list:
        title = breaking_item.get('title')
        imageurl = breaking_item.get('urlToImage')
        url = breaking_item.get('url')

        breaking_object = Breaking(title,imageurl, url)
        breaking_results.append(breaking_object)

    return breaking_results
