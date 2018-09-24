import unittest
from wordsearch import *

class WordsearchInputTests(unittest.TestCase):
    
    def test_initial_results_should_be_empty_dict(self):
        #results should be an empty dictionary that will later be filled with the solutions. 
        #The solutions to the word puzzle consists of the words as keys and lists of ordered paris as values
        wsearch = Wordsearch("")
        self.assertEqual(dict(),wsearch.results)

        
if __name__ == "__main__":
    unittest.main()