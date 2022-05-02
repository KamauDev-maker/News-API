class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?{}apiKey={}'

class ProdConfig (Config):
    """
    production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass 

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config :The parent configuration class with General configuration settings
    """
    
    DEBUG = True