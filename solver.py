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
            solutionOutput = solutionOutput + keyword + ": " + self.__coordListToStr(coords) + "\n"
        return solutionOutput
    
    def __coordListToStr(self, coordList):
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
        #dx: x iteration 'direction'.  Positive moves the search to the right, negative moves it left
        #dy: y iteration 'direction'. Positive moves the search down and negative moves it up
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

    def fastSearch(self, keyword):
        #create flattened grid if it doesn't exist
        if not hasattr(self,"line_grid"):
            self.flattenGrid()
            
        #dictionary for mapping oppositie directions to the correct line_grid that should be used for the search
        oppositeDirection = {"LEFT":"RIGHT", "DOWNLEFT":"UPRIGHT", "UP":"DOWN", "DOWNRIGHT":"UPLEFT"}
        
        #search directions in line_grid.keys for the keyword
        for direction in self.line_grid.keys():
            kw_index = self.line_grid[direction].find(keyword)                  #get index where keyword occurs
            if kw_index > -1:                                                   #if the keyword is found the index will be greater than -1
                return self.__getCoordList(keyword, direction, kw_index)
        
        #search opposite directions of the lin_grid.keys for the keyword
        for direction in ["LEFT"]:
            kw_index = self.line_grid[oppositeDirection[direction]].find(keyword[::-1])  #look to see if reverse word is in line_grid
            if kw_index > -1:
                return self.__getCoordList(keyword, direction, kw_index)
    
    def __getCoordList(self, keyword, direction, kw_index):
        d = len(self.wordsearch.grid)
        L = len(keyword)
        dx,dy = self.directions[direction]
        searchDirection = direction

        result = []

        #offset is used so we can get proper coordinates for reverse searches
        offset = (0,0)                  
        if not (direction in self.line_grid.keys()):
            offset = (-dx*(L-1),-dy*(L-1))
                
        if direction in ["LEFT","RIGHT"]:
            row = kw_index//d
            col_i = kw_index%d
            for j in range(L):
                result.append((col_i+dx*j+offset[0],row+offset[1]))
            return result
        
    #flatten the grid by sweeping different directions and store them in memory to be searched for keywords
    def flattenGrid(self):
        grid = self.wordsearch.grid
        d = len(grid) #divisor
        
        #create dictionaries to store the linearized path through the grid with the sweep direction as the key
        self.line_grid = dict()
        
        #line_grid_coords stores the (x,y) coordinates for a character in the corresponding flattened grid.
        #This is only done when the sweep direction is diagonal, because horizontal and vertical sweeps are
        #easy to invert and find the coordinate
        self.line_grid_coords = dict()
        
        #########
        #up-right diagonal sweep
        #########
        upRight = ""
        upRightCoords = []
        for N in range(2*(d-1)+1):            #iterate over left/bottom grid boundary
            k=N*(1-N//d)+(2*(d-1)-N)*(N//d)   #a given diagonal's length
            q=N//d                            #quotient
            r=N%d                             #remainder
            y0=r*(1-q)+(d-1)*q                #starting y coordinate of diagonal
            x0=q*(r+1)                        #starting x coordinate of diagonal
            for i in range(k+1):              #concatenate along diagonal and append corresponding coordinates
                upRight += grid[y0-i][x0+i]
                upRightCoords.append((x0+i,y0-i))
        self.line_grid.update({"UPRIGHT":upRight})
        self.line_grid_coords.update({"UPRIGHT":upRightCoords});
        
        ##########
        #up-left diagonal sweep
        ##########
        upLeft = ""
        upLeftCoords = []
        for N in range(2*(d-1)+1):          #iterate over right/bottom grid boundary
            k=N*(1-N//d)+(2*(d-1)-N)*(N//d)
            q=N//d
            r=N%d
            y0=r*(1-q)+(d-1)*q
            x0=(d-1)-q*(r+1)
            for i in range(k+1):
                upLeft += grid[y0-i][x0-i]
                upLeftCoords.append((x0-i,y0-i))
        self.line_grid.update({"UPLEFT":upLeft})
        self.line_grid_coords.update({"UPLEFT":upLeftCoords})
        
        ###########
        #right-horizontal sweep
        ###########
        #Note: nothing added to line_grid_coords since this direction is easy to invert (given a character index)
        right = ""
        for i in range(d):
            right += "".join(grid[i])
        self.right = right
        self.line_grid.update({"RIGHT":right})
        
        ###########
        #down-vertical sweep
        ###########
        #Note: nothing added to line_grid_coords since this direction is easy to invert (given a character index)
        down = ""
        for j in range(d):
            down += "".join([grid[i][j] for i in range(d)])
        self.line_grid.update({"DOWN":down})
        
        
        
                
                