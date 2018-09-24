

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
        
        #Make sure keywords consist entirely of chars in [A-Z]
        keywordsAreAllCaps = self.__CheckKeywordsConsistOfAllCaps()
        if (not keywordsAreAllCaps):
            return False
        
        return True
    
    #Validation tests helper functions:
    def __CheckKeywordsConsistOfAllCaps(self):
        for kword in self.keywords:
            for c in kword:
                if not c.isupper():
                    return False
        return True