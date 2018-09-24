

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
        
        #Grid must not be an empty list
        if len(self.grid) == 0:
            return False
        
        #All grid rows must be equal length
        rowLength = len(self.grid[0])
        for row in self.grid:
            if len(row) != rowLength:
                return False
        
        #Make sure keywords consist entirely of chars in [A-Z]
        keywordsAreAllCaps = self.__CheckKeywordsConsistOfAllCaps()
        if (not keywordsAreAllCaps):
            return False
        
        #Make sure keywords are at least two chars long
        for kword in self.keywords:
            if len(kword) < 2:
                return False
        
        return True
    
    #Validation tests helper functions:
    def __CheckKeywordsConsistOfAllCaps(self):
        for kword in self.keywords:
            for c in kword:
                if not c.isupper():
                    return False
        return True