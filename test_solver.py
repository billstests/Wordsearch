import unittest
from wordsearch import *
from solver import *


class WordsearchSolverTests(unittest.TestCase):
        
    def setUp(self):
        self.wsearch = Wordsearch("wordsearchEx1.txt")
        self.wsSolver = WordsearchSolver(self.wsearch)
        
    #test that wordsearchsolve can store a wordsearch object successfully  
    def test_wordsearchsolver_object_stores_wordsearch_object(self):
        wsearch = Wordsearch("wordsearchEx1.txt")
        wsSolver = WordsearchSolver(wsearch)
        self.assertEqual(wsSolver.wordsearch, wsearch)

    #test that wordsearchsolver will raise a ValueError when it tries to solve a wordsearch that is not valid
    def test_wordsearchsolver_raises_error_if_it_tries_to_solve_an_invalid_wordsearch(self):
        self.wsearch.keywords = [] #make sure the wordsearch will not be considered valid (keywords can't be empty list)
        wsSolver = WordsearchSolver(self.wsearch)
        try:
            wsSolver.solve()
        except ValueError:
            return
        self.fail()
    
    #tests that wordsearchsolver can find a word by searching horizontal to the right and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_horizontal_right(self):
        result = self.wsSolver.search(keyword="SCOTTY", direction="RIGHT")
        knownResult = [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching horizontal to the left and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_horizontal_left(self):
        result = self.wsSolver.search(keyword="KIRK", direction="LEFT")
        knownResult = [(4,7),(3,7),(2,7),(1,7)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching vertical and up and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_up(self):
        result = self.wsSolver.search(keyword="KHAN", direction="UP")
        knownResult = [(5,9),(5,8),(5,7),(5,6)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching vertical and up and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_down(self):
        result = self.wsSolver.search(keyword="BONES", direction="DOWN")
        knownResult = [(0,6),(0,7),(0,8),(0,9),(0,10)]
        self.assertEqual(result, knownResult)
    
if __name__ == "__main__":
    unittest.main()