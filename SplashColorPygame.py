from random import randint
from os import system
from pygame.locals import Color
import pygame

class colorSplash(object):

	ROWS = 10
	COLS = 20
	SUMALL = ROWS*COLS
	cursum = 0
	NUMCOLORS = 3
	colorGrid = []
	boolGrid = []
	# Define some colors
	colors = {
	'RED'   : Color(255,0,0),
	'GREEN' : Color(0,255,0),
	'BLUE'  : Color(0,0,255),
	'WHITE' : Color(255,255,255),
	'BLACK' : Color(0,0,0)
	}
	 
	# This sets the WIDTH and HEIGHT of each grid location
	WIDTH = 20
	HEIGHT = 20
	 
	# This sets the margin between each cell
	MARGIN = 5
	
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
			enumColors = []
			for keys in self.colors:
				enumColors.append(keys)
			select = raw_input('Choose a number you wish to spread ' + str(enumColors) + ' : ')
			system('cls')
			
			if select != "":
				select = int(select)

		return select
				
	def showGrid(self, grid):
		# Draw the grid
		for r in range(0, self.ROWS):
			for c in range (0, self.COLS):
				if grid[r][c] == 0:
					color = self.colors['WHITE']
					pygame.draw.rect(screen,
					color,
					[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
					(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
					self.WIDTH,
					self.HEIGHT])
				elif grid[r][c] == 1:
					color = self.colors['GREEN']
					pygame.draw.rect(screen,
					color,
					[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
					(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
					self.WIDTH,
					self.HEIGHT])
				elif grid[r][c] == 2:
					color = self.colors['BLUE']
					pygame.draw.rect(screen,
					color,
					[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
					(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
					self.WIDTH,
					self.HEIGHT])
				elif grid[r][c] == 3:
					color = self.colors['RED']
					pygame.draw.rect(screen,
					color,
					[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
					(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
					self.WIDTH,
					self.HEIGHT])
				else:
					color = self.colors['BLACK']
					pygame.draw.rect(screen,
					color,
					[(self.MARGIN + self.WIDTH) * c + self.MARGIN,
					(self.MARGIN + self.HEIGHT) * r + self.MARGIN,
					self.WIDTH,
					self.HEIGHT])


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
WINDOW_SIZE = [grid.ROWS * grid.WIDTH * grid.MARGIN, grid.COLS * grid.HEIGHT + grid.MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Splash Color")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            c = pos[0] /(grid.WIDTH + grid.MARGIN)
            r = pos[1] /(grid.HEIGHT + grid.MARGIN)
            # Set that location to zero
            print("Click ", pos, "Grid coordinates: ", r, c)
	# Set the screen background
	print grid.colors["BLACK"]
	screen.fill((0,0,0))
	virus = grid.prompt()
	grid.showGrid(grid.colorGrid)
	pygame.display.update()
	# Limit to 60 frames per second
	#clock.tick(60)
	# Go ahead and update the screen with what we've drawn.
	#pygame.display.flip()
	
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()