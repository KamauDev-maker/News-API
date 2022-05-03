from app import app
import urllib.request,json
from .models import Sources

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources():
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
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
        url =sources_list.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        
        sources_object = Sources(id,name,description,url,category,language)  
        sources_results.append(sources_object)
    return sources_results   
            