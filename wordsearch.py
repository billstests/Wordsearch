

class Wordsearch:
    def __init__(self, fileLocation):
        self.results = dict()
        
    def loadData(self, keywords=[], grid=[]):
        self.keywords = keywords
        self.grid = grid