from wordsearch import *

class WordsearchSolver:
    def __init__(self, wordsearch):
        self.wordsearch = wordsearch
        
    def solve(self):
        if not self.wordsearch.isValid():
            raise ValueError("Wordsearch must return True for isValid() to be able to solve")
        return