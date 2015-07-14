from random import randint
from os import system

global COLS
COLS = 6
global ROWS
ROWS = 5

def getRandomNum():
	return randint(0,3)

def prompt(colorGrid, boolGrid):
	system('cls')
	showGrid(colorGrid)
	select = input('Choose a number you wish to spread: ')
	for r in range(0, ROWS):	
		for c in range (0, COLS):
			if boolGrid[r][c] == True:
				print colorGrid[r][c]
	
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
	grids = checkSpread(colorGrid, boolGrid)
	colorGrid = grids[0]
	boolGrid = grids[1]

def checkSpread(colorGrid, boolGrid):
	for r in range(0, ROWS):
			for c in range (0, COLS):
				if boolGrid[r][c] == True:
					if(r == 0 and c == 0):
							
						if(boolGrid[r+1][c+1] == False): 
							boolGrid[r+1][c+1] = True
							colorGrid[r+1][c+1] = colorGrid[r][c]
						if(boolGrid[r+1][c] == False):
							boolGrid[r+1][c] = True
							colorGrid[r+1][c] = colorGrid[r][c]
						if(boolGrid[r][c+1] == False):
							boolGrid[r][c+1] = True
							colorGrid[r][c+1] = colorGrid[r][c]

					#bottom left corner
					elif(r == ROWS-1 and c == 0):
					
						if(boolGrid[r-1][c+1] == False):	
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
						if(boolGrid[r-1][c] == False):   	
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
						if(boolGrid[r][c+1] == False): 	
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]

					#top right corner
					elif(r == 0 and c == COLS-1):
					
						if(boolGrid[r+1][c-1] == False):	
							boolGrid[r+1][c-1] = True 
							colorGrid[r+1][c-1] = colorGrid[r][c]
						if(boolGrid[r+1][c] == False):	
							boolGrid[r+1][c]  = True 
							colorGrid[r+1][c]  = colorGrid[r][c]
						if(boolGrid[r][c-1] == False):	   
							boolGrid[r][c-1] = True
							colorGrid[r][c-1] = colorGrid[r][c]

					#Bottom right corner
					elif(r == ROWS-1 and c == COLS-1):
					
						if(boolGrid[r-1][c-1] == False):	 
							boolGrid[r-1][c-1] = True 
							colorGrid[r-1][c-1] = colorGrid[r][c]
						if(boolGrid[r-1][c] == False):		
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
						if(boolGrid[r][c-1] == False):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]


					#Top Row Checks
					elif(r == 0 and (c != 0 or c != COLS)):
					
						if(boolGrid[r][c+1] == False):	
							boolGrid[r][c+1] = True
							colorGrid[r][c+1] = colorGrid[r][c]
						if(boolGrid[r][c-1] == False):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
						if(boolGrid[r+1][c+1] == False):
							boolGrid[r+1][c+1] = True 
							colorGrid[r+1][c+1] = colorGrid[r][c]
						if(boolGrid[r+1][c-1] == False):
							boolGrid[r+1][c-1] = True 
							colorGrid[r+1][c-1] = colorGrid[r][c]
						if(boolGrid[r+1][c] == False):	
							boolGrid[r+1][c]= True 
							colorGrid[r+1][c] = colorGrid[r][c]

						
					#Bottom Row checks
					elif(r == ROWS-1 and (c != 0 or c != COLS)):
					
						if(boolGrid[r][c+1] == False):	
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
						if(boolGrid[r][c-1] == False):	
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
						if(boolGrid[r-1][c-1] == False):	
							boolGrid[r-1][c-1] = True 
							colorGrid[r-1][c-1] = colorGrid[r][c]
						if(boolGrid[r-1][c+1] == False):	
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
						if(boolGrid[r-1][c] == False):	
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
					
					#Left Side Checks
					elif(c == 0 and (r != 0 or r != ROWS)):

						if(boolGrid[r][c+1] == False):	 
							boolGrid[r][c+1] = True 
							colorGrid[r][c+1] = colorGrid[r][c]
						if(boolGrid[r+1][c] == False):	 
							boolGrid[r+1][c] = True 
							colorGrid[r+1][c] = colorGrid[r][c]
						if(boolGrid[r-1][c] == False):		 
							boolGrid[r-1][c] = True 
							colorGrid[r-1][c] = colorGrid[r][c]
						if(boolGrid[r-1][c+1] == False):	 
							boolGrid[r-1][c+1] = True 
							colorGrid[r-1][c+1] = colorGrid[r][c]
						if(boolGrid[r+1][c+1] == False):	
							boolGrid[r+1][c+1] = True 
							colorGrid[r+1][c+1] = colorGrid[r][c]
					
					#Right Side Checks
					elif(c == COLS-1 and (r != 0 or r != ROWS)):
					
						if(boolGrid[r][c-1] == False):		
							boolGrid[r][c-1] = True 
							colorGrid[r][c-1] = colorGrid[r][c]
						if(boolGrid[r+1][c] == False):	
							boolGrid[r+1][c] = True
							colorGrid[r+1][c] = colorGrid[r][c]
						if(boolGrid[r-1][c] == False):	
							boolGrid[r-1][c] = True
							colorGrid[r-1][c] = colorGrid[r][c]
						if(boolGrid[r-1][c-1] == False):
							boolGrid[r-1][c-1] = True
							colorGrid[r-1][c-1] = colorGrid[r][c]
						if(boolGrid[r+1][c-1] == False):
							boolGrid[r+1][c-1] = True
							colorGrid[r+1][c-1] = colorGrid[r][c]

					#Middle checks
					# elif r > 1 and c > 0:
						# if(boolGrid[r-1][c+1] == False):	
							# boolGrid[r-1][c+1] = True 
							# colorGrid[r-1][c+1] = colorGrid[r][c]
						# if(boolGrid[r][c+1] == False):
							# boolGrid[r][c+1] = True 
							# colorGrid[r][c+1] = colorGrid[r][c]
						# if(boolGrid[r][c-1] == False):
							# boolGrid[r][c-1] = True 
							# colorGrid[r][c-1] = colorGrid[r][c]
						# if(boolGrid[r+1][c] == False):	
							# boolGrid[r+1][c] = True
							# colorGrid[r+1][c] = colorGrid[r][c]
						# if(boolGrid[r-1][c] == False):	
							# boolGrid[r-1][c] = True 
							# colorGrid[r-1][c] = colorGrid[r][c]
						# if(boolGrid[r+1][c+1] == False): 
							# boolGrid[r+1][c+1] = True
							# colorGrid[r+1][c+1] = colorGrid[r][c]
						# if(boolGrid[r-1][c-1] == False):	
							# boolGrid[r-1][c-1] = True 
							# colorGrid[r-1][c-1] = colorGrid[r][c]
						# if(boolGrid[r+1][c-1] == False):
							# boolGrid[r+1][c-1] = True
							# colorGrid[r+1][c-1] = colorGrid[r][c]
	grids = [colorGrid, boolGrid]
	return grids
	
grids = create()
colorGrid = grids[0]
boolGrid = grids[1]
initialize(colorGrid, boolGrid)

#while False in boolGrid:
prompt(colorGrid, boolGrid)
showGrid(boolGrid)
#prompt(colorGrid, boolGrid)
