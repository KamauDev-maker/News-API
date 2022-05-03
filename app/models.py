class Articles:
    """
     class to define news article objects
    """
    
    def __init__(self,author,title,imageurl,publishedAt,url):
        self.author = author
        self.url = url
        self.imageurl = imageurl
        self.publishedAt = publishedAt
        self.title = title
        
class Breaking:
    """
    class to define news articles object
    """
    def __init__(self,title,imageurl,url):
       self.title = title
       self.imageurl = imageurl
       self.url = url
class Keyword:
    """
    class to define news articles object
    """  
    def __init__(self,author,title,imageurl,publishedAt,url):
        self.author = author
        self.title = title
        self.imageurl = imageurl
        self.publishedAt = publishedAt
        self.url = url

class Sources:
    """
    class to define news articles object
    """
    def __init__(self,id,name,description,url,category,language):
        self.id = id
        self.name = name
        self.description =description
        self.url = url
        self.category =category
        self.language = language               