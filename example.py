from wordsearch import *
from solver import *

#create wordsearch object (here using an external text file with keywords and letter grid)
wsearch = Wordsearch("wordsearchEx1.txt")

#create WordsearchSolver object that takes in a word search
wsSolver = WordsearchSolver(wsearch)

#solve and print solution
wsSolver.printSolution()