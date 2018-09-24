

class Wordsearch:
    def __init__(self, fileLocation):
        self.results = dict()
        
    def loadData(self, keywords=[]):
        self.keywords = keywords