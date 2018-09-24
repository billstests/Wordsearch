import unittest
from wordsearch import *

class WordsearchInputTests(unittest.TestCase):

    #results should be an empty dictionary that will later be filled with the solutions. 
    #The solutions to the word puzzle consists of the words as keys and lists of ordered paris as values    
    def test_initial_results_should_be_empty_dict(self):
        wsearch = Wordsearch("")
        self.assertEqual(dict(),wsearch.results)

    #Test ability to load in and store a list of keywords data in wordsearch object
    def test_store_keywords_in_wordsearch(self):
        wsearch = Wordsearch("")
        myKeywords = ["KEYWORDONE","KEYWORDTWO","KEYWORDTHREE"]
        wsearch.loadData(keywords=myKeywords)
        self.assertEqual(myKeywords,wsearch.keywords)
        
    #Test ability to load and store a character grid (matrix) into wordsearch object
    #This list of lists will represent the wordsearch grid data
    def test_store_grid_in_wordsearch(self):
        wsearch = Wordsearch("")
        myGrid = [['A','B','C'],['E','F','G'],['H','I','J']]
        wsearch.loadData(grid = myGrid)
        self.assertEqual(myGrid,wsearch.grid)
        
if __name__ == "__main__":
    unittest.main()