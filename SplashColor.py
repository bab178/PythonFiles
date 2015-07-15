from random import randint
from os import system

class colorSplash(object):

	ROWS = 10
	COLS = 20
	SUMALL = ROWS*COLS
	cursum = 0
	NUMCOLORS = 3
	colorGrid = []
	boolGrid = []
	
	def __init__(self):
		#create board
		for r in range(0, self.ROWS):
			colorRow = []
			boolRow = []
			for c in range (0, self.COLS):
				colorRow.append(self.getRandomNum(self.NUMCOLORS))
				boolRow.append(False)
			self.colorGrid.append(colorRow)
			self.boolGrid.append(boolRow)
		#Plant virus
		x = self.getRandomNum(self.ROWS-1)
		y = self.getRandomNum(self.COLS-1)
		self.boolGrid[x][y] = True
		virus = int(self.colorGrid[x][y])
		self.checkSpread(virus, 0)
	
	
	def getRandomNum(self, MAX):
		return randint(0, MAX)

	def prompt(self):
		system('cls')
		select = ""
		while select not in range(0, self.NUMCOLORS+1):
			self.showGrid(self.colorGrid)
			select = raw_input('Choose a number you wish to spread ' + str(range(0, self.NUMCOLORS+1)) + ' : ')
			system('cls')
			
			if select != "":
				select = int(select)

		return select
				
	def showGrid(self, grid):
		for r in range(0, self.ROWS):
			for c in range (0, self.COLS):
				print grid[r][c],
			print
		print

	def checkSpread(self, virus, match):
		match = False
		for r in range(0, self.ROWS):
				for c in range (0, self.COLS):
					if self.boolGrid[r][c] == True:
						if(r == 0 and c == 0):
							
							if(self.boolGrid[r+1][c+1] == False and self.colorGrid[r+1][c+1] == virus): 
								self.boolGrid[r+1][c+1] = True
								self.colorGrid[r+1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):
								self.boolGrid[r+1][c] = True
								self.colorGrid[r+1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus):
								self.boolGrid[r][c+1] = True
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True

						#bottom left corner
						elif(r == self.ROWS-1 and c == 0):
						
							if(self.boolGrid[r-1][c+1] == False and self.colorGrid[r-1][c+1] == virus):	
								self.boolGrid[r-1][c+1] = True 
								self.colorGrid[r-1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):   	
								self.boolGrid[r-1][c] = True 
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus): 	
								self.boolGrid[r][c+1] = True 
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True

						#top right corner
						elif(r == 0 and c == self.COLS-1):
						
							if(self.boolGrid[r+1][c-1] == False and self.colorGrid[r+1][c-1] == virus):	
								self.boolGrid[r+1][c-1] = True 
								self.colorGrid[r+1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):	
								self.boolGrid[r+1][c]  = True 
								self.colorGrid[r+1][c]  = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):	   
								self.boolGrid[r][c-1] = True
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True

						#Bottom right corner
						elif(r == self.ROWS-1 and c == self.COLS-1):
						
							if(self.boolGrid[r-1][c-1] == False and self.colorGrid[r-1][c-1] == virus):	 
								self.boolGrid[r-1][c-1] = True 
								self.colorGrid[r-1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):		
								self.boolGrid[r-1][c] = True 
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):	
								self.boolGrid[r][c-1] = True 
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True


						#Top Row Checks
						elif(r == 0 and (c != 0 or c != self.COLS)):
						
							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus):	
								self.boolGrid[r][c+1] = True
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):	
								self.boolGrid[r][c-1] = True 
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c+1] == False and self.colorGrid[r+1][c+1] == virus):
								self.boolGrid[r+1][c+1] = True 
								self.colorGrid[r+1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c-1] == False and self.colorGrid[r+1][c-1] == virus):
								self.boolGrid[r+1][c-1] = True 
								self.colorGrid[r+1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):	
								self.boolGrid[r+1][c]= True 
								self.colorGrid[r+1][c] = self.colorGrid[r][c]
								match = True

							
						#Bottom Row checks
						elif(r == self.ROWS-1 and (c != 0 or c != self.COLS)):
						
							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus):	
								self.boolGrid[r][c+1] = True 
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):	
								self.boolGrid[r][c-1] = True 
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c-1] == False and self.colorGrid[r-1][c-1] == virus):	
								self.boolGrid[r-1][c-1] = True 
								self.colorGrid[r-1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c+1] == False and self.colorGrid[r-1][c+1] == virus):	
								self.boolGrid[r-1][c+1] = True 
								self.colorGrid[r-1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):	
								self.boolGrid[r-1][c] = True 
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
						
						#Left Side Checks
						elif(c == 0 and (r != 0 or r != self.ROWS)):

							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus):	 
								self.boolGrid[r][c+1] = True 
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):	 
								self.boolGrid[r+1][c] = True 
								self.colorGrid[r+1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):		 
								self.boolGrid[r-1][c] = True 
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c+1] == False and self.colorGrid[r-1][c+1] == virus):	 
								self.boolGrid[r-1][c+1] = True 
								self.colorGrid[r-1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c+1] == False and self.colorGrid[r+1][c+1] == virus):	
								self.boolGrid[r+1][c+1] = True 
								self.colorGrid[r+1][c+1] = self.colorGrid[r][c]
								match = True
						
						#Right Side Checks
						elif(c == self.COLS-1 and (r != 0 or r != self.ROWS)):
						
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):		
								self.boolGrid[r][c-1] = True 
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):	
								self.boolGrid[r+1][c] = True
								self.colorGrid[r+1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):	
								self.boolGrid[r-1][c] = True
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c-1] == False and self.colorGrid[r-1][c-1] == virus):
								self.boolGrid[r-1][c-1] = True
								self.colorGrid[r-1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c-1] == False and self.colorGrid[r+1][c-1] == virus):
								self.boolGrid[r+1][c-1] = True
								self.colorGrid[r+1][c-1] = self.colorGrid[r][c]
								match = True

						#Middle checks
						elif r > 0 and c > 0:
							if(self.boolGrid[r-1][c+1] == False and self.colorGrid[r-1][c+1] == virus):	
								self.boolGrid[r-1][c+1] = True 
								self.colorGrid[r-1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c+1] == False and self.colorGrid[r][c+1] == virus):
								self.boolGrid[r][c+1] = True 
								self.colorGrid[r][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r][c-1] == False and self.colorGrid[r][c-1] == virus):
								self.boolGrid[r][c-1] = True 
								self.colorGrid[r][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c] == False and self.colorGrid[r+1][c] == virus):	
								self.boolGrid[r+1][c] = True
								self.colorGrid[r+1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c] == False and self.colorGrid[r-1][c] == virus):	
								self.boolGrid[r-1][c] = True 
								self.colorGrid[r-1][c] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c+1] == False and self.colorGrid[r+1][c+1] == virus): 
								self.boolGrid[r+1][c+1] = True
								self.colorGrid[r+1][c+1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r-1][c-1] == False and self.colorGrid[r-1][c-1] == virus):	
								self.boolGrid[r-1][c-1] = True 
								self.colorGrid[r-1][c-1] = self.colorGrid[r][c]
								match = True
							if(self.boolGrid[r+1][c-1] == False and self.colorGrid[r+1][c-1] == virus):
								self.boolGrid[r+1][c-1] = True
								self.colorGrid[r+1][c-1] = self.colorGrid[r][c]
								match = True
		
		#RECURSION
		while match == True:
			self.checkSpread(virus, match)
			match = False
			
		self.cursum = self.updateSpread(virus)


	def updateSpread(self, virus):
		sum = 0
		for r in range(0, self.ROWS):
				for c in range (0, self.COLS):
					if self.boolGrid[r][c] == True:
						self.colorGrid[r][c] = '*'
						sum += 1
		return sum
						
	def checkWin(self):
		if self.cursum == self.SUMALL:
			self.showGrid(self.colorGrid)
			print "		YOU WON!!!"
			return True
		return False

system('cls')
grid = colorSplash()
virus = grid.prompt()
grid.checkSpread(virus, 0)

while grid.checkWin() == False:
	virus = grid.prompt()
	grid.checkSpread(virus, 0)

