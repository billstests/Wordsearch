from wordsearch import *

class WordsearchSolver:
    def __init__(self, wordsearch):
        self.wordsearch = wordsearch
        
    def solve(self):
        if not self.wordsearch.isValid():
            raise ValueError("Wordsearch must return True for isValid() to be able to solve")
        return

    def search(self, keyword, direction):
        grid = self.wordsearch.grid
        firstLetter = keyword[0]
        length = len(keyword)
        result = []         #if keyword is found, the list ordered pairs that represent the letters positions
        N = len(grid)       #length of square grid
        for i in range(N):
            for j in range(N):
                if direction == "RIGHT":
                    if j+(length-1) < N:                #test if search will stay in the bounds of the grid (going right)
                        if firstLetter == grid[i][j]:
                            chars = [grid[i][j+u] for u in range(length)] 
                            if "".join(chars) == keyword:
                                result = [(j+u,i) for u in range(length)]
                                break
                if direction == "LEFT":
                    if j-(length-1) >= 0:               #test if search will stay in tje bounds of the grid (going left)
                        if firstLetter == grid[i][j]:
                            chars = [grid[i][j-u] for u in range(length)] 
                            if "".join(chars) == keyword:
                                result = [(j-u,i) for u in range(length)]
                                break
        return result
                        
                    
                
                