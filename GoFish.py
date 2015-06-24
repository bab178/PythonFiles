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
			
		spacing = 8
		for h in range(0, len(self.hand)):
			print '-' * spacing
			if self.hand[h] == 1:
				print ' ' * (spacing/3), 'A'
			elif self.hand[h] == 11:
				print ' ' * (spacing/3), 'J'
			elif self.hand[h] == 12:
				print ' ' * (spacing/3), 'Q'
			elif self.hand[h] == 13:
				print ' ' * (spacing/3), 'K'
			else:
				print ' ' * (spacing/3), self.hand[h]
		print '-' * spacing
		print '\n'
	
	def popCard(self, x, y):
		#print "Popping: ", x, ':',self.cards[x][y]
		self.cards[x].pop(y)
		
		
		
#START
c = Deck()
c.showDeck()

c.getHand()
c.showHand()
c.showDeck()
