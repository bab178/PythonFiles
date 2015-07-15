from random import randint
from os import system


global ROWS
ROWS = 20
global COLS
COLS = 26
global SUMALL
SUMALL = ROWS*COLS
global NUMCOLORS
NUMCOLORS = 3

def getRandomNum():
	return randint(0,NUMCOLORS)

def prompt(colorGrid, boolGrid):
	system('cls')
	select = ""
	while select not in range(0, NUMCOLORS+1):
		showGrid(colorGrid)
		select = raw_input('Choose a number you wish to spread ' + str(range(0, NUMCOLORS+1)) + ' : ')
		system('cls')
		
		if select != "":
			select = int(select)

	return select
	
def create():
	colorGrid = []
	boolGrid = []
	for r in range(0, ROWS):
		colorRow = []
		boolRow = []
		for c in range (0, COLS):
			colorRow.append(getRandomNum())
			boolRow.append(False)
		colorGrid.append(colorRow)
		boolGrid.append(boolRow)
		grids = [colorGrid, boolGrid]
	return grids
	
def showGrid(grid):
	for r in range(0, ROWS):
		for c in range (0, COLS):
			print grid[r][c],
		print
	print

def initialize(colorGrid, boolGrid):
	#Top Left Corner is Owned
	boolGrid[0][0] = True
	checkSpread(colorGrid[0][0], 0, colorGrid, boolGrid)

def checkSpread(virus, match, colorGrid, boolGrid):
	match = False
	for r in range(0, ROWS):
			for c in range (0, COLS):
				if boolGrid[r][c] == True:
					if(r == 0 and c == 0):
						
						if(boolGrid[r+1][c+1] == False and colorGrid[r+1][c+1] == virus): 
							boolGrid[r+1][c+1] = True
							colorGrid[r+1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):
							boolGrid[r+1][c] = True
							colorGrid[r+1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus):
							boolGrid[r][c+1] = True
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True

					#bottom left corner
					elif(r == ROWS-1 and c == 0):
					
						if(boolGrid[r-1][c+1] == False and colorGrid[r-1][c+1] == virus):	
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):   	
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus): 	
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True

					#top right corner
					elif(r == 0 and c == COLS-1):
					
						if(boolGrid[r+1][c-1] == False and colorGrid[r+1][c-1] == virus):	
							boolGrid[r+1][c-1] = True 
							colorGrid[r+1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):	
							boolGrid[r+1][c]  = True 
							colorGrid[r+1][c]  = colorGrid[r][c]
							match = True
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):	   
							boolGrid[r][c-1] = True
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True

					#Bottom right corner
					elif(r == ROWS-1 and c == COLS-1):
					
						if(boolGrid[r-1][c-1] == False and colorGrid[r-1][c-1] == virus):	 
							boolGrid[r-1][c-1] = True 
							colorGrid[r-1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):		
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True


					#Top Row Checks
					elif(r == 0 and (c != 0 or c != COLS)):
					
						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus):	
							boolGrid[r][c+1] = True
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c+1] == False and colorGrid[r+1][c+1] == virus):
							boolGrid[r+1][c+1] = True 
							colorGrid[r+1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c-1] == False and colorGrid[r+1][c-1] == virus):
							boolGrid[r+1][c-1] = True 
							colorGrid[r+1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):	
							boolGrid[r+1][c]= True 
							colorGrid[r+1][c] = colorGrid[r][c]
							match = True

						
					#Bottom Row checks
					elif(r == ROWS-1 and (c != 0 or c != COLS)):
					
						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus):	
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c-1] == False and colorGrid[r-1][c-1] == virus):	
							boolGrid[r-1][c-1] = True 
							colorGrid[r-1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c+1] == False and colorGrid[r-1][c+1] == virus):	
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):	
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
					
					#Left Side Checks
					elif(c == 0 and (r != 0 or r != ROWS)):

						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus):	 
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):	 
							boolGrid[r+1][c] = True 
							colorGrid[r+1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):		 
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c+1] == False and colorGrid[r-1][c+1] == virus):	 
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c+1] == False and colorGrid[r+1][c+1] == virus):	
							boolGrid[r+1][c+1] = True 
							colorGrid[r+1][c+1] = colorGrid[r][c]
							match = True
					
					#Right Side Checks
					elif(c == COLS-1 and (r != 0 or r != ROWS)):
					
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):		
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):	
							boolGrid[r+1][c] = True
							colorGrid[r+1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):	
							boolGrid[r-1][c] = True
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c-1] == False and colorGrid[r-1][c-1] == virus):
							boolGrid[r-1][c-1] = True
							colorGrid[r-1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c-1] == False and colorGrid[r+1][c-1] == virus):
							boolGrid[r+1][c-1] = True
							colorGrid[r+1][c-1] = colorGrid[r][c]
							match = True

					#Middle checks
					elif r > 0 and c > 0:
						if(boolGrid[r-1][c+1] == False and colorGrid[r-1][c+1] == virus):	
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c+1] == False and colorGrid[r][c+1] == virus):
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r][c-1] == False and colorGrid[r][c-1] == virus):
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c] == False and colorGrid[r+1][c] == virus):	
							boolGrid[r+1][c] = True
							colorGrid[r+1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c] == False and colorGrid[r-1][c] == virus):	
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c+1] == False and colorGrid[r+1][c+1] == virus): 
							boolGrid[r+1][c+1] = True
							colorGrid[r+1][c+1] = colorGrid[r][c]
							match = True
						if(boolGrid[r-1][c-1] == False and colorGrid[r-1][c-1] == virus):	
							boolGrid[r-1][c-1] = True 
							colorGrid[r-1][c-1] = colorGrid[r][c]
							match = True
						if(boolGrid[r+1][c-1] == False and colorGrid[r+1][c-1] == virus):
							boolGrid[r+1][c-1] = True
							colorGrid[r+1][c-1] = colorGrid[r][c]
							match = True
	
	#RECURSION
	while match == True:
		checkSpread(virus, match, colorGrid, boolGrid)
		match = False
		
	return updateSpread(virus, colorGrid, boolGrid)


def updateSpread(virus, colorGrid, boolGrid):
	sum = 0
	for r in range(0, ROWS):
			for c in range (0, COLS):
				if boolGrid[r][c] == True:
					colorGrid[r][c] = '*'
					sum += 1
	return sum
					
					
def checkWin(cursum):
	if cursum == SUMALL:
		showGrid(colorGrid)
		print "					YOU WON!!!"
		return True
	return False

system('cls')
grids = create()
colorGrid = grids[0]
boolGrid = grids[1]
initialize(colorGrid, boolGrid)
virus = prompt(colorGrid, boolGrid)
cursum = checkSpread(virus, 0, colorGrid, boolGrid)


while checkWin(cursum) == False:
	virus = prompt(colorGrid, boolGrid)
	cursum = checkSpread(virus, 0, colorGrid, boolGrid)

