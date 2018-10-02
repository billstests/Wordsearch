# Wordsearch
My Word Search Kata

## Overview:
I programmed the word search kata and ran tests using Python 3.6. This program can be used to solve a word search, given the keywords and the word search grid in the correct format (as described in the kata).

Short description of files in repository:
- example.py (Provides an example of how to use the program as well as benchmarking details)
- README.md (THIS!)
- solver.py (Contains WordSearchSolver class used for solving a worsearch)
- test_solver.py (Tests for WordSearchSolver)
- test_wordsearch.py (Tests for WordSearch)
- wordsearch.py (Contains WordSearch class used for storing word search info)
- wordsearchEx1.txt (Example word search from kata statement)
- wordsearchEx2.txt (Word search I generated using the website linked in kata)


 

## Running Tests:
Two main sets of tests were used to drive development:
- Tests for the WordSearch class which deals with reading in a word search puzzle file, formating, and validation.

To run these tests run: `python test_wordsearch.py`

- Tests for the WordSearchSolver class which deals with searching for the keywords in a WordSearch object, generating the list of coordinates from a keyword that has been found, and outputing the solution.

To run these tests run: `python test_solver.py`

## Example file (example.py)
This file can be used to explore some basic workings of the word search and solver objects.

The most basic use is to run: `python example.py`
- This will output the solution to "WordsearchEx1.txt" (the word search given in the kata description)

Another use is to run: `python example.py timetrial`
- This will compare the time it takes to run the original search method I implemented vs a faster (but more obscure) method (fastSearch) I wrote.  It does the comparison for "wordsearchEx1.txt" as well as another word search puzzle that I generated with the given website, "wordsearchEx2.txt"

## Notes on the two search methods (search and fastSearch):
- search is the original method I used to search for keywords in the grid (character matrix).  It is used in the WordSearchSolver class.  It is similar to how a human solves a word search.  Itterating through each character, and trying to see if the word lies in all directions emitting from this root position.  It is easy to understand, but the performance is not very good.  This is still the default search method in the .solve() method.
- fastSearch was my attempt to implement a better performing keyword search method for the WordSearchSolver class.  The basic idea is to 'flatten' out the character grid in each direction a search can happen and then use pythons built-in functions to find the index where the word occurs.  Actually, we don't need every direction since, for ex: searching right and left, are very similar if we just reverse the keyword (being careful when we need to return the character coordinates of the reversed case).  So, we only need to keep 4 search drections in memory (not 8).  This way of searching takes more memory (which shouldn't matter unless it's a really really big puzzle), but tests I have run show a big performance gains.  For "wordsearchEx1.txt", the fastSearch method is 57 times faster than the original, while for "wordsearchEx2.txt" (bigger puzzle) the fastSearch method is 146 times faster.  To implement this method in solve enable fastSearch (.solve(useFastSearch=True)).



