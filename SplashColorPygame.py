from random import randint
from os import system
from pygame.locals import Color
import pygame

class colorSplash(object):
	
	def __init__(self):
	
		self.NUMCOLORS = 3
		self.ROWS = 15
		self.COLS = 30
		#PER CELL
		self.WIDTH = 20
		self.HEIGHT = 20
		self.MARGIN = 5
		self.SUMALL = self.ROWS*self.COLS
		self.cursum = 0
		self.colorGrid = []
		self.boolGrid = []
		self.BLACK = Color(0,0,0)
		self.colors = {
		'BLUE'   : Color(0,0,255),
		'GREEN' : Color(0,255,0),
		'RED'     : Color(255,0,0),
		'WHITE' : Color(255,255,255)
		}
		 
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
				
	def showGrid(self, grid):
		# Draw the grid
	
		for r in range(0, self.ROWS):
			for c in range (0, self.COLS):
				if grid[r][c] == 0:
					color = self.colors['BLUE']
				elif grid[r][c] == 1:
					color = self.colors['WHITE']
				elif grid[r][c] == 2:
					color = self.colors['GREEN']
				elif grid[r][c] == 3:
					color = self.colors['RED']
				else:
					color = self.BLACK
			
				pygame.draw.rect(screen,color,
				[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
				(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
				self.WIDTH, self.HEIGHT])
		w = 5
		for c in self.colors:
				pygame.draw.rect(screen, self.colors[c],[w,  self.ROWS*(self.WIDTH + self.MARGIN) + self.MARGIN ,self.WIDTH,self.HEIGHT])
				w += 25

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


 
# Initialize pygame
pygame.init()

grid = colorSplash()

# Set the HEIGHT and WIDTH of the screen
#WINDOW_SIZE = [grid.COLS * grid.HEIGHT + grid.MARGIN + 100, grid.COLS * grid.HEIGHT + grid.MARGIN - 150]
WINDOW_SIZE = [grid.COLS * grid.HEIGHT + grid.MARGIN*21
						, grid.ROWS * grid.HEIGHT + grid.MARGIN*20 + 5]
print "Windows Size: ", WINDOW_SIZE
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Splash Color")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not(grid.checkWin()):
    for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			pygame.quit() # Flag that we are done so we exit this loop
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# User clicks the mouse. Get the position
			pos = pygame.mouse.get_pos()
			# Change the x/y screen coordinates to grid coordinates
			c = pos[0] /(grid.WIDTH + grid.MARGIN)
			r = pos[1] /(grid.HEIGHT + grid.MARGIN)
			#print("Click ", pos, "Grid coordinates: ", r, c)
			if(r == grid.ROWS and c == 0):
				#BLUE
				grid.checkSpread(0,0)
			elif(r == grid.ROWS and c == 1):
				#GREEN
				grid.checkSpread(1,0)
			elif(r == grid.ROWS and c == 2):
				#WHITE
				grid.checkSpread(2,0)
			elif(r == grid.ROWS and c == 3):
				#RED
				grid.checkSpread(3,0)
			elif(r == grid.ROWS and c == 4):
				#BLACK
				grid.checkSpread(4,0)
			
		screen.fill(grid.BLACK)
		grid.showGrid(grid.colorGrid)
		pygame.display.update()
		# Limit to 60 frames per second
		#clock.tick(60)