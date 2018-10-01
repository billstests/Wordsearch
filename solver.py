from wordsearch import *

class WordsearchSolver:
    def __init__(self, wordsearch):
        self.wordsearch = wordsearch
        self.directions = {"UP":(0,-1), "DOWN":(0,1), "LEFT":(-1,0), "RIGHT":(1,0), "UPLEFT":(-1,-1), "UPRIGHT":(1,-1),
                           "DOWNLEFT":(-1,1), "DOWNRIGHT":(1,1)}
        
    #print out the wordsearch solution: the keywords and their respective coordinates
    def printSolution(self):
        resultsStr = self.generateSolutionOutput()
        print(resultsStr)
        
    #generate the solution string consisting of the keywords and their coordinates
    def generateSolutionOutput(self):
        self.solve()
        results = self.wordsearch.results.items()
        solutionOutput = ""
        for keyword, coords in results:
            solutionOutput = solutionOutput + keyword + ": " + self.coordListToStr(coords) + "\n"
        return solutionOutput
    
    def coordListToStr(self, coordList):
        coordStr = ""
        for i, c in enumerate(coordList):
            coordStr += str(c).replace(" ","")
            if i < len(coordList)-1:
                coordStr += ","
        return coordStr
    
    #fill the wordsearch results dictionary with the letter coordinates
    def solve(self):
        if not self.wordsearch.isValid():
            raise ValueError("Wordsearch must return True for isValid() to be able to solve")
        #Find results for all keywords
        for keyword in self.wordsearch.keywords:
            result = self.searchAllDirections(keyword)
            self.wordsearch.results.update({keyword:result})
    
    #search for a keyword in all directions.  Return the coordinates if it is found (else return an empty list)
    def searchAllDirections(self, keyword):
        for direction in self.directions:
            found = self.search(keyword, direction)
            if found:
                break
        return found
    
    #search for a keyword in the grid in a given search direction    
    def search(self, keyword, direction):
        #dx: x itteration 'direction'.  Positive moves the search to the right, negative moves it left
        #dy: y itteration 'direction'. Positive moves the search down and negative moves it up
        dx,dy = self.directions[direction]
        
        grid = self.wordsearch.grid
        firstLetter = keyword[0]
        length = len(keyword)
        result = []         #if keyword is found, the list ordered pairs that represent the letters positions
        N = len(grid)       #length of square grid
        for i in range(N):
            for j in range(N):
                    if self.__inBounds(j,i,length,dx,dy,N):       #test if search will stay in the bounds of the grid
                        if firstLetter == grid[i][j]:
                            chars = [grid[i+dy*u][j+dx*u] for u in range(length)] 
                            if "".join(chars) == keyword:
                                result = [(j+dx*u,i+dy*u) for u in range(length)]
                                break
        return result
                        
    #tests if the search will stay in bounds.
    def __inBounds(self, x_i, y_i, L, dx, dy, gridLength):
        BC_x1 = (x_i+(L-1)*dx >= 0)                 #boundary condition 1 for x-direction (horizontal)
        BC_x2 = (x_i+(L-1)*dx < gridLength)         #boundary condition 2 for x-direction (horizontal)
        BC_y1 = (y_i+(L-1)*dy >= 0)                 #boundary condition 1 for y-direction (vertical)
        BC_y2 = (y_i+(L-1)*dy < gridLength)         #boundary condition 2 for y-direction (vertical)
        return BC_x1 and BC_x2 and BC_y1 and BC_y2
        
                
                