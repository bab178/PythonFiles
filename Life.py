from random import randint
from os import system
from time import sleep


def randomNo():
	rn = randint(0, 1)
	return rn

def RandomGrid(ROWS, COLS):
	Grid = {}
	for r in range (0,ROWS):
		Grid [r] = {}
		for c in range (0,COLS):
			Grid[r][c] = randomNo()
	return Grid

def PrintGrid(Grid, ROWS, COLS):
	#Prints entire Grid
	for r in range (0,ROWS):
		for c in range (0,COLS):
			if  Grid[r][c] == 1:
				print '#',
			else:
				print ' ',
		print
	#newline after Grid
	print

def Neighbours(Grid, ROWS, COLS):
	#Creates NGrid of 0's
	NGrid = {}
	for r in range (0,ROWS):
		NGrid [r] = {}
		for c in range (0,COLS):
			NGrid[r][c] = 0
			
	NCount = 0
	
	for r in range(0,ROWS):
		for c in  range(0,COLS):
			#Corner checks first
			#Top left corner
			if(r == 0 and c == 0):
			
				if(Grid[r+1][c+1] == 1):NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1
				if(Grid[r][c+1] == 1):	NCount += 1
				
				#set NeighborGrid to NCount, set NCount to 0
				NGrid[r][c] = NCount
				NCount = 0
	
			#bottom left corner
			elif(r == ROWS-1  and c == 0):
			
				if(Grid[r-1][c+1] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):   	NCount += 1
				if(Grid[r][c+1] == 1): 	NCount += 1
				
				NGrid[r][c] = NCount
				NCount = 0
			
			#top right corner
			elif(r == 0 and c == COLS-1):
			
				if(Grid[r+1][c-1] == 1):	NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1
				if(Grid[r][c-1] == 1):	    NCount += 1

				NGrid[r][c] = NCount
				NCount = 0
			
			#Bottom right corner
			elif(r == ROWS-1 and c == COLS-1):
			
				if(Grid[r-1][c-1] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):		NCount += 1
				if(Grid[r][c-1] == 1):		NCount += 1
				
				NGrid[r][c] = NCount
				NCount = 0

			#Top Row Checks
			elif(r == 0 and (c != 0 or c != COLS)):
			
				if(Grid[r][c+1] == 1):	NCount += 1
				if(Grid[r][c-1] == 1):		NCount += 1
				if(Grid[r+1][c+1] == 1):NCount += 1
				if(Grid[r+1][c-1] == 1):	NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1

				NGrid[r][c] = NCount
				NCount = 0
				
			#Bottom Row checks
			elif(r == ROWS-1 and (c != 0 or c != COLS)):
			
				if(Grid[r][c+1] == 1):	NCount += 1
				if(Grid[r][c-1] == 1):		NCount += 1
				if(Grid[r-1][c-1] == 1):	NCount += 1
				if(Grid[r-1][c+1] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):		NCount += 1
				
				NGrid[r][c] = NCount
				NCount = 0
			
			#Left Side Checks
			elif(c == 0 and (r != 0 or r != ROWS)):

				if(Grid[r][c+1] == 1):	NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):		NCount += 1
				if(Grid[r-1][c+1] == 1):	NCount += 1
				if(Grid[r+1][c+1] == 1):	NCount += 1
				
				NGrid[r][c] = NCount
				NCount = 0
			
			#Right Side Checks
			elif(c == COLS-1 and (r != 0 or r != ROWS)):
			
				if(Grid[r][c-1] == 1):		NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):		NCount += 1
				if(Grid[r-1][c-1] == 1):	NCount += 1
				if(Grid[r+1][c-1] == 1):	NCount += 1
				
				NGrid[r][c] = NCount
				NCount = 0

			#Middle checks
			else:
				if(Grid[r-1][c+1] == 1):	NCount += 1
				if(Grid[r][c+1] == 1):	NCount += 1
				if(Grid[r][c-1] == 1):		NCount += 1
				if(Grid[r+1][c] == 1):	NCount += 1
				if(Grid[r-1][c] == 1):		NCount += 1
				if(Grid[r+1][c+1] == 1):NCount += 1
				if(Grid[r-1][c-1] == 1):	NCount += 1
				if(Grid[r+1][c-1] == 1):	NCount += 1

				NGrid[r][c] = NCount
				NCount = 0

	return NGrid

def iterateGeneration(Grid, ROWS, COLS):
	NGrid = Neighbours(Grid, ROWS, COLS)
	for r in range(0,ROWS):
		for c in  range(0,COLS):
			if(Grid[r][c] == 1 and (NGrid[r][c] == 0 or NGrid[r][c] == 1)):
				#Loneliness: Cell dies
				Grid[r][c] = 0
		   #elif(Grid[r][c] == 1 and (NGrid[r][c] == 2 or NGrid[r][c] == 3)):	#Nothing happens
			elif(Grid[r][c] == 0 and NGrid[r][c] == 3):
				#New Cell is born
				Grid[r][c] = 1
			elif(Grid[r][c] == 1 and NGrid[r][c] >= 4):
				#Overcrowding: Cell dies
				Grid[r][c] = 0

ROWS = -1
COLS = -1
TIMES = -1
speed_choice = ''
				
while ROWS < 0:
		ROWS = int(input("Enter the number of rows: "))

while COLS < 0:
		COLS = int(input("Enter the number of columns: "))

while TIMES < 0:
		TIMES = int(input("Enter the number of generations: "))

speeds = {'Slow' : 1.2, 'Fast' : .7, 'Hyper' : .1}
while speed_choice != 'Slow' and  speed_choice != 'Fast' and  speed_choice != 'Hyper':
	for x in speeds: 
		print (x)
	speed_choice = str(raw_input("Choose a speed: "))

rGrid =	RandomGrid(ROWS, COLS)

for times in range(0, TIMES):
	iterateGeneration(rGrid,ROWS, COLS)
	PrintGrid(rGrid,ROWS, COLS)
	sleep(speeds[speed_choice])
	system('cls')

	