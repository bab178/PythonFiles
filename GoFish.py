from random import randint
from os import system
from time import sleep

class Deck():
	
	def __init__(self):
		self.cards = []
		self.hand = []
		for d in range(4):
			self.cards.append(range(1,14))
			
	def showDeck(self):
		sum = 0
		for d in range(4):
			print self.cards[d]
			sum += len(self.cards[d]) 
			
		print "Cards left: ", sum
	
	def randomCard(self):
		x = randint(0,3)
		y = randint(0,13)
		coords = [x,y]
		return coords
		
	def getHand(self):
		#if num cards left > 5 or hand is empty
		for h in range(5):
			randCoords = self.randomCard()
			x = randCoords[0]
			y = randCoords[1]
			self.hand.append(self.cards[x][y])
			self.popCard(x, y)
		print
	
	def showHand(self):
		visual = []
		#Create visual cards
		for v in range(0, len(self.hand)):
			if v == 0:
				visual.append('-' * 7)
				visual.append('|  ' + '   |')
				visual.append('|  ' + '   |')
				if self.hand[v] == 10:
					visual.append('| ' + str(self.hand[v]) + '  |')
				elif self.hand[v] == 11:
					visual.append('|  ' + 'J' + '  |')
				elif self.hand[v] == 12:
					visual.append('|  ' + 'Q' + '  |')
				elif self.hand[v] == 13:
					visual.append('|  ' + 'K' + '  |')
				else:
					visual.append('|  ' + str(self.hand[v]) + '  |')
				visual.append('|  ' + '   |')
				visual.append('|  ' + '   |')
				visual.append('-' * 7)
			else:
				visual[0] += (' -------')
				visual[1] += (' |  ' + '   |')
				visual[2] += (' |  ' + '   |')
				if self.hand[v] == 10:
					visual[3] += (' | ' + str(self.hand[v]) + '  |')
				elif self.hand[v] == 11:
					visual[3] += (' |  ' + 'J' + '  |')
				elif self.hand[v] == 12:
					visual[3] += (' |  ' + 'Q' + '  |')
				elif self.hand[v] == 13:
					visual[3] += (' |  ' + 'K' + '  |')
				else:
					visual[3] += (' |  ' + str(self.hand[v]) + '  |')
				visual[4] += (' |  ' + '   |')
				visual[5] += (' |  ' + '   |')
				visual[6] += (' -------')

		for v in range(0, 7):
			print visual[v]
		print

	def popCard(self, x, y):
		#print "Popping: ", x, ':',self.cards[x][y]
		self.cards[x].pop(y)
		
		
		
#START
c = Deck()
c.showDeck()

c.getHand()
c.showHand()
c.showDeck()
