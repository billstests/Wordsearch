import unittest
from wordsearch import *

class WordsearchInputTests(unittest.TestCase):

    #results should be an empty dictionary that will later be filled with the solutions. 
    #The solutions to the word puzzle consists of the words as keys and lists of ordered paris as values    
    def test_initial_results_should_be_empty_dict(self):
        wsearch = Wordsearch("")
        self.assertEqual(dict(),wsearch.results)

    #Load in and store keywords data in wordsearch object
    def test_store_keywords_in_wordsearch(self):
        wsearch = Wordsearch("")
        myKeywords = ["KEYWORDONE","KEYWORDTWO","KEYWORDTHREE"]
        wsearch.loadData(keywords=myKeywords)
        self.assertEqual(myKeywords,wsearch.keywords)
        
        
if __name__ == "__main__":
    unittest.main()