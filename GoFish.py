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
		for d in range(4):
			print self.cards[d]
		print
	
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
		for h in range(0, len(self.hand)):
			if self.hand[h] == 1:
				print 'A',
			elif self.hand[h] == 11:
				print 'J',
			elif self.hand[h] == 12:
				print 'Q',
			elif self.hand[h] == 13:
				print 'K',
			else:
				print self.hand[h],
		print '\n'
	
	def popCard(self, x, y):
		print "Popping: ", x, ':',self.cards[x][y]
		self.cards[x].pop(y)
		
		
		
#START
c = Deck()
c.showDeck()

c.getHand()
c.showHand()
c.showDeck()