import unittest
from wordsearch import *
from solver import *


class WordsearchSolverTests(unittest.TestCase):
        
    #test that wordsearchsolve can store a wordsearch object successfully  
    def test_wordsearchsolver_object_stores_wordsearch_object(self):
        wsearch = Wordsearch("wordsearchEx1.txt")
        wsSolver = WordsearchSolver(wsearch)
        self.assertEqual(wsSolver.wordsearch, wsearch)

    #test that wordsearchsolver will raise a ValueError when it tries to solve a wordsearch that is not valid
    def test_wordsearchsolver_raises_error_if_it_tries_to_solve_an_invalid_wordsearch(self):
        wsearch = Wordsearch("wordsearchEx1.txt")
        wsearch.keywords = [] #make sure the wordsearch will not be considered valid (keywords can't be empty list)
        wsSolver = WordsearchSolver(wsearch)
        try:
            wsSolver.solve()
        except ValueError:
            return
        self.fail()
    
if __name__ == "__main__":
    unittest.main()