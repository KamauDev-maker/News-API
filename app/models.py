class Articles:
    """
     class to define news article objects
    """
    
    def __init__(self,author,description,imageurl,time,title):
        self.author = author
        self.description = description
        self.imageurl = imageurl
        self.time = time
        self.title = title
        
class Breaking:
    """
    class to define news articles object
    """
    def __init__(self,title,imageurl):
       self.title = title
       self.imageurl = imageurl
       
class Keyword:
    """
    class to define news articles object
    """  
    def __init__(self,author,title,imageurl,time):
        self.author = author
        self.title = title
        self.imageurl = imageurl
        self.time = time

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