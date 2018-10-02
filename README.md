# Wordsearch
My Word Search Kata

##Overview:
I programmed the word search kata and ran tests using Python 3.6. This program can be used to solve a word search, given the keywords and the word search grid in the correct format (as described in the kata).

Files:
-example.py (Provides an example of how to use the program as well as benchmarking details)
-README.md (THIS!)
-solver.py (Contains WordSearchSolver class used for solving a worsearch)
-test_solver.py (Tests for WordSearchSolver)
-test_wordsearch.py (Tests for WordSearch)
-wordsearch.py (Contains WordSearch class used for storing word search info)


 

##Running Tests:
Two main sets of tests were used to drive development:
-Tests for the WordSearch object which deals with reading in a word search puzzle file, formating, and validation.

To run these tests run: python test_wordsearch.py

-Tests for the WordSearchSolver object which deals with searching for the keywords in a WordSearch object, generating the list of coordinates from a keyword that has been found, and outputing the solution.

To run these tests run: python test_solver.py

##Example file (example.py)
This file can be used to explore some basic workings of the word search and solver objects.

The most basic use is to run: python example.py
-without any parameters and it will output the solution to "WordsearchEx1.txt" (the word search given in the kata description)

Another use is to run: python example.py timetrial
-This will compare the time it takes to run the original search method I implemented vs a faster (but more obscure) method (fastSearch).  It does the comparison for "WordsearchEx1.txt" as well as another word search puzzle that I generated with the given website, "WordsearchEx2.txt"



