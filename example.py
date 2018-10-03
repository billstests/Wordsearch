from wordsearch import *
from solver import *
from timeit import default_timer as timer
import sys

#returns the average execution time for solving a wordsearch
def measureSolveExecutionTime(fileLoc = "wordsearchEx1.txt", useFastSearch = False, NumOfTries = 1000):
    wsearch = Wordsearch(fileLoc)
    wsSolver = WordsearchSolver(wsearch)
    
    start = timer()
    for i in range(NumOfTries):           #Run solve method NumTimes times
        wsSolver.solve(useFastSearch)
    avgTimeElapsed = (timer()-start)/NumOfTries   #calculate average time elaped per run
    return avgTimeElapsed

#a simple example of how to use the wordsearch and solver objects to print out a wordsearch solution
def DoExampleWordsearch():
    #create wordsearch object (here using an external text file with keywords and letter grid)
    wsearch = Wordsearch("wordsearchEx1.txt")
    
    #create WordsearchSolver object that takes in a word search
    wsSolver = WordsearchSolver(wsearch)
    
    #solve and print solution
    wsSolver.printSolution()
#compares the fastSolve to the regular solve method for a wordsearch
def CompareSolveTimes(fileLoc = "wordsearchEx1.txt", NumOfTries = 1000):
    tFast = measureSolveExecutionTime(fileLoc, True, NumOfTries)
    tRegular = measureSolveExecutionTime(fileLoc, False, NumOfTries)
    print(fileLoc + ": RegularSearch_Time = " + str(round(tRegular/tFast,3)) + " x FastSearch_Time")

if __name__=="__main__":
    args = sys.argv
    #default behavior: do a simple wordsearch example
    if len(args)==1:
        DoExampleWordsearch()
    #timetrial option
    if len(args)==2:
        if args[1].upper() == "TIMETRIAL":
            CompareSolveTimes("wordsearchEx1.txt")  #regular = 57xfastSolver on my computer
            CompareSolveTimes("wordsearchEx2.txt")  #regular = 146xfastSolver on my computer
