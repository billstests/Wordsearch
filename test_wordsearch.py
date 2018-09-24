import unittest
from wordsearch import *

class WordsearchInputTests(unittest.TestCase):

    def setUp(self):
        self.wsearch = Wordsearch("")
        
    #results should be an empty dictionary that will later be filled with the solutions. 
    #The solutions to the word puzzle consists of the words as keys and lists of ordered paris as values    
    def test_initial_results_should_be_empty_dict(self):
        self.wsearch = Wordsearch("")
        self.assertEqual(dict(),self.wsearch.results)

    #Test ability to load in and store a list of keywords data in wordsearch object
    def test_store_keywords_in_wordsearch(self):
        myKeywords = ["KEYWORDONE","KEYWORDTWO","KEYWORDTHREE"]
        self.wsearch.loadData(keywords=myKeywords)
        self.assertEqual(myKeywords, self.wsearch.keywords)
        
    #Test ability to load and store a character grid (matrix) into wordsearch object
    #This list of lists will represent the wordsearch grid data
    def test_store_grid_in_wordsearch(self):
        myGrid = [['A','B','C'],['E','F','G'],['H','I','J']]
        self.wsearch.loadData(grid = myGrid)
        self.assertEqual(myGrid, self.wsearch.grid)
    
    #####################################################################
    #--tests to check validity of data (keyword and character grid)
    
    #test that if an empty list of keywords is loaded, that the data is not considered valid
    def test_wordsearch_data_not_valid_if_keywords_is_empty_list(self):
        myKeywords = []
        self.wsearch.loadData(keywords=myKeywords)
        isDataValid = self.wsearch.isValid()
        self.assertEqual(False, isDataValid)
        
    #test that if keywords contains anythings except characters [A-Z], the data is not considered valid
    def test_wordsearch_data_not_valid_if_keywords_chars_not_AtoZ(self):
        keywordTests =  [["KEYWORD1"], ["KEYWORDO.E"], ["KeyWORD", "KEYWORDTWO"]]
        
        for myKeywords in keywordTests:
            self.wsearch.loadData(keywords = myKeywords)
            self.assertEqual(False, self.wsearch.isValid())

    #test that keywords must be at least two chars, else the data is not conidered valid
    def test_wordsearch_data_not_valid_if_keywords_less_than_two_chars(self):
        myKeywords = ["KEYWORDONE", "KEYWORDTWO", "K"]
        self.wsearch.loadData(keywords = myKeywords)
        self.assertEqual(False, self.wsearch.isValid())
        
    #tests that the grid is not an empty list, else the data is not considered valid
    def test_wordsearch_data_not_valid_if_grid_is_empty_list(self):
        myKeywords = ["KEYWORDONE", "KEYWORDTWO"]
        myGrid = []
        self.wsearch.loadData(keywords = myKeywords, grid = myGrid)
        self.assertEqual(False, self.wsearch.isValid())
       
    #tests that that each grid rows of unequal length are not considered valid
    def test_wordsearch_data_not_valid_if_grid_rows_not_same_length(self):
        myKeywords = ["KEYWORDONE","KEYWORDTWO"]
        myGrid = [['A','B'],['D','E','F']]
        self.wsearch.loadData(keywords=myKeywords, grid=myGrid)
        self.assertEqual(False, self.wsearch.isValid())
        
    
        
if __name__ == "__main__":
    unittest.main()