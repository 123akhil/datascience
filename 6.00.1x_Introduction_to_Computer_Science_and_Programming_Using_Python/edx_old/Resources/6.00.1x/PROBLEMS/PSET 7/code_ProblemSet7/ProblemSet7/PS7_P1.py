class NewsStory (object):
    
    def __init__(self,guid, titulo, tema, resumen, link):
        
        self.guid = guid
        self.titulo = titulo
        self.tema = tema
        self.resumen = resumen
        self.link = link
    
    def getGuid(self):
        return self.guid
        
    def getTitle(self):
        return self.titulo
    
    def getSubject(self):
        return self.tema
        
    def getSummary(self):
        return self.resumen
        
    def getLink(self):
        return self.link

