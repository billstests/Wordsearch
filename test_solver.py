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
        
    #tests that wordsearchsolver can find a word by searching vertical and down and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_down(self):
        result = self.wsSolver.search(keyword="BONES", direction="DOWN")
        knownResult = [(0,6),(0,7),(0,8),(0,9),(0,10)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching up and to the left and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_up_and_horizontally_left(self):
        result = self.wsSolver.search(keyword="SULU", direction="UPLEFT")
        knownResult = [(3,3),(2,2),(1,1),(0,0)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching up and to the right and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_up_and_horizontally_right(self):
        result = self.wsSolver.search(keyword="JEM", direction="UPRIGHT")
        knownResult = [(7,9),(8,8),(9,7)]
        self.assertEqual(result, knownResult)
        
    #tests that wordsearchsolver can find a word by searching down and to the left and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_down_and_horizontally_left(self):
        result = self.wsSolver.search(keyword="UHURA", direction="DOWNLEFT")
        knownResult = [(4,0),(3,1),(2,2),(1,3),(0,4)]
        self.assertEqual(result, knownResult)
    
    #tests that wordsearchsolver can find a word by searching down and to the right and returns the correct list of the letter coordinates
    def test_wordsearchsolve_search_vertical_down_and_horizontally_right(self):
        result = self.wsSolver.search(keyword="SPOCK", direction="DOWNRIGHT")
        knownResult = [(2,1),(3,2),(4,3),(5,4),(6,5)]
        self.assertEqual(result, knownResult)
    
    #test that wordsearchsolver can find a word by searching all directions and return the correct list of the letter coordinates
    def test_wordsearchsolve_search_all_direction(self):
        #Try with 2 different words
        result = self.wsSolver.searchAllDirections(keyword="SPOCK")
        knownResult = [(2,1),(3,2),(4,3),(5,4),(6,5)]
        self.assertEqual(result, knownResult)
        
        result = self.wsSolver.searchAllDirections(keyword="KIRK")
        knownResult = [(4,7),(3,7),(2,7),(1,7)]
        self.assertEqual(result, knownResult)
    
    def test_wordsearchsolve_solve_puzzle_and_fill_wordsearch_results_with_solution(self):
        self.wsSolver.solve()
        theResults = self.wsSolver.wordsearch.results
        #check solutions
        self.assertEqual(theResults["BONES"],[(0,6),(0,7),(0,8),(0,9),(0,10)])
        self.assertEqual(theResults["KHAN"],[(5,9),(5,8),(5,7),(5,6)])
        self.assertEqual(theResults["KIRK"],[(4,7),(3,7),(2,7),(1,7)])
        self.assertEqual(theResults["SCOTTY"],[(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)])
        self.assertEqual(theResults["SPOCK"],[(2,1),(3,2),(4,3),(5,4),(6,5)])
        self.assertEqual(theResults["SULU"],[(3,3),(2,2),(1,1),(0,0)])
        self.assertEqual(theResults["UHURA"],[(4,0),(3,1),(2,2),(1,3),(0,4)])
        
    def test_wordsearchsolve_solve_and_output_solution_in_correct_format(self):
        expectedOutput="BONES: (0,6),(0,7),(0,8),(0,9),(0,10)\n"
        expectedOutput+="KHAN: (5,9),(5,8),(5,7),(5,6)\n"
        expectedOutput+="KIRK: (4,7),(3,7),(2,7),(1,7)\n"
        expectedOutput+="SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)\n"
        expectedOutput+="SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)\n"
        expectedOutput+="SULU: (3,3),(2,2),(1,1),(0,0)\n"
        expectedOutput+="UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)\n"
        myOutput = self.wsSolver.generateSolutionOutput()
        self.assertEqual(myOutput,expectedOutput)
        
    ############################################################################
    #Below tests deal with implementing a faster method for searching for wonds in the wordsearch
    
    #fastsearch will implement a faster way to search by flattening the grid into a line obtained by
    #itterating through the grid in a certain search direction  
    def test_wordsearchsolve_fastsearch_flatten_grid_using_up_right_diagonal_concatenation(self):
        wsearch = Wordsearch("")
        #make a grid that is easy to check that it is 'flattened' correctly
        grid1 = [["A","C","F"],
                 ["B","E","H"],
                 ["D","G","I"]]
        wsearch.loadData(keywords=["KW","QW"], grid = grid1)
        wsSolver = WordsearchSolver(wsearch)
        
        #flatten the grid into a string consiting of all the up-right diagonals (start in top left corner)
        wsSolver.flattenGrid()
        self.assertEqual(wsSolver.line_grid["UPRIGHT"],"ABCDEFGHI")
        #check that the coordinates are stored correctly as well.  These are stored because inverting the flattened diagonals is not as trivial as strickly horizontal or vertical directions
        self.assertEqual(wsSolver.line_grid_coords["UPRIGHT"],[(0,0),(0,1),(1,0),(0,2),(1,1),(2,0),(1,2),(2,1),(2,2)])
        
    def test_wordsearchsolve_fastsearch_flatten_grid_using_up_left_diagonal_concatenation(self):
        wsearch = Wordsearch("")
        #make a grid that is easy to check that it is 'flattened' correctly
        grid1 = [["F","C","A"],
                 ["H","E","B"],
                 ["I","G","D"]]
        wsearch.loadData(keywords=["KW","QW"], grid = grid1)
        wsSolver = WordsearchSolver(wsearch)
        
        #flatten the grid into a string consiting of all the up-left diagonals (start in top right corner)
        wsSolver.flattenGrid()
        self.assertEqual(wsSolver.line_grid["UPLEFT"],"ABCDEFGHI")
        #check that the coordinates are stored correctly as well.  These are stored because inverting the flattened diagonals is not as trivial as strickly horizontal or vertical directions
        self.assertEqual(wsSolver.line_grid_coords["UPLEFT"],[(2,0),(2,1),(1,0),(2,2),(1,1),(0,0),(1,2),(0,1),(0,2)])
        
    def test_wordsearchsolve_fastsearch_flatten_grid_using_up_right_horizontal_concatenation(self):
        wsearch = Wordsearch("")
        #make a grid that is easy to check that it is 'flattened' correctly
        grid1 = [["A","B","C"],
                 ["D","E","F"],
                 ["G","H","I"]]
        wsearch.loadData(keywords=["KW","QW"], grid = grid1)
        wsSolver = WordsearchSolver(wsearch)
        
        #flatten the grid into a string consiting of all the up-left diagonals (start in top right corner)
        wsSolver.flattenGrid()
        self.assertEqual(wsSolver.line_grid["RIGHT"],"ABCDEFGHI")
    
    def test_wordsearchsolve_fastsearch_flatten_grid_using_down_vertical_concatenation(self):
        wsearch = Wordsearch("")
        #make a grid that is easy to check that it is 'flattened' correctly
        grid1 = [["A","D","G"],
                 ["B","E","H"],
                 ["C","F","I"]]
        wsearch.loadData(keywords=["KW","QW"], grid = grid1)
        wsSolver = WordsearchSolver(wsearch)
        
        #flatten the grid into a string consiting of all the up-left diagonals (start in top right corner)
        wsSolver.flattenGrid()
        self.assertEqual(wsSolver.line_grid["DOWN"],"ABCDEFGHI")

    #test fastsearch on known result for word that is in the horizontal-right and horizontal-left orientation        
    def test_wordsearchsolve_fastsearch_fastSearch_right_and_left(self):
        #right search
        result = self.wsSolver.fastSearch(keyword="SCOTTY")
        knownResult = [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)]
        self.assertEqual(result, knownResult)
        
        #left search
        result = self.wsSolver.fastSearch(keyword="KIRK")
        knownResult = [(4,7),(3,7),(2,7),(1,7)]
        self.assertEqual(result, knownResult)
        
        
if __name__ == "__main__":
    unittest.main()