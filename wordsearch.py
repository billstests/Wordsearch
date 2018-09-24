

class Wordsearch:
    def __init__(self, fileLocation):
        self.results = dict()
        
    def loadData(self, keywords=[], grid=[]):
        self.keywords = keywords
        self.grid = grid
        
    def isValid(self):
        #There must be keywords to search for to be valid
        if len(self.keywords) == 0:
            return False
        
        return True