import unittest
from wordsearch import *

class WordsearchInputTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #This method opens a wordsearch example and parses/stores the keywords and the grid of characters
        f = open("wordsearchEx1.txt",'r')
        lines = f.readlines()
        f.close()
        
        #store keywords in class variable that setUp method can access
        cls.keywords = lines[0].replace("\n","").split(",")
        
        grid = []
        for row in lines[1:]:
            grid.append(row.replace("\n","").split(","))
        
        #store grid in class variable that setUp method can access
        cls.grid = grid
        
    def setUp(self):
        self.wsearch = Wordsearch("")
        self.wsearch.loadData(keywords=WordsearchInputTests.keywords.copy(), grid=WordsearchInputTests.grid.copy())
        
    #results should be an empty dictionary that will later be filled with the solutions. 
    #The solutions to the word puzzle consists of the words as keys and lists of ordered paris as values    
    def test_initial_results_should_be_empty_dict(self):
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
        
    #tests that the row count and column count are equal (that it is a square grid)
    def test_wordsearch_data_not_valid_if_row_count_not_same_as_col_count(self):
        myKeywords = ["KEYONE", "KEYTWO"]
        myGrid = [['A','B','C'],['E','F','G']]
        self.wsearch.loadData(keywords=myKeywords, grid=myGrid)
        self.assertEqual(False, self.wsearch.isValid())
       
    #test that the elements of a grid are single chars [A-Z] else the data is not considered valid    
    def test_wordsearch_data_not_valid_if_grid_elements_not_single_chars_AtoZ(self):
        myKeywords = ["KEYONE", "KEYTWO"]
        myGrid = [['A','B','C'], ['E','F','G'], ['E','FF','G']]
        myGrid2 = [['A','B','C'], ['E','','G'], ['E','F','G']]
        self.wsearch.loadData(keywords=myKeywords, grid=myGrid)
        self.assertEqual(False, self.wsearch.isValid())
        self.wsearch.loadData(keywords=myKeywords, grid=myGrid2)
        self.assertEqual(False, self.wsearch.isValid())
        
    
    #test that keywords can fit in the square grid, else the data is not considered valid
    def test_wordsearch_data_not_valid_if_keywords_dont_fit_in_grid(self):
        myKeywords = ["KEYA", "KEYB", "KEYCA"]
        myGrid = [['A','B','C','X'], ['E','F','G','Y'], ['E','F','G','Z'],['E','F','G','Z']]
        self.wsearch.loadData(keywords = myKeywords, grid = myGrid)
        self.assertEqual(False, self.wsearch.isValid())
        
    #test that the example test file is valid (wordsearchEx1.txt, which is loaded by default)
    def test_wordsearch_data_from_example1_is_valid(self):
        self.assertEqual(True, self.wsearch.isValid())
        
    #####################################################################
    #--tests for loading an parsing an external file
    
    #test that the wordsearch parse method gives the same result as in our setUpClass
    def test_wordsearch_parse_example_file(self):
        f = open("wordsearchEx1.txt",'r')
        lines = f.readlines()
        f.close()
        myKeywords, myGrid = self.wsearch.parse(lines)
        
        #myKeywords and myGrid should be the same values as values in setUpClass
        for kw in self.wsearch.keywords:
            if not (kw in myKeywords):
                self.fail()
                
        for i in range(len(self.wsearch.grid)):
            for j in range(len(self.wsearch.grid[i])):
                if self.wsearch.grid[i][j] != myGrid[i][j]:
                    self.fail()
    
    #test that when a wordsearch object is instantiated with the example file location, it is parsed, loaded, and valid
    def test_wordsearch_instantiation_with_example_external_file_location_is_valid(self):
        wsearch = Wordsearch("wordsearchEx1.txt")
        self.assertEqual(True, wsearch.isValid())
        
    
if __name__ == "__main__":
    unittest.main()