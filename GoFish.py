from random import choice
from random import randint
from os import system
from time import sleep

class Deck(object):
	
	def __init__(self, other = None):
		self.cards = []
		self.hand = []
		if other:
			self.cards = other.cards
		else:
			for d in range(4):
				self.cards.append(range(1,14))

	def showDeck(self):
		if len(self.cards) != 0:
			for d in range(4):
				print self.cards[d]
		
		print "Cards left: ", self.numCards()
		
	def numCards(self):
		sum = 0
		if len(self.cards) != 0:
			for d in range(4):
				sum += len(self.cards[d]) 
		return sum
		
	def randomCard(self):
		x = randint(0, len(self.cards)-1)
		y = choice(self.cards[x])
		coords = [x,y]
		return coords
		
	def getHand(self):
		if self.numCards() >= 5 and len(self.hand) < 5:
			for h in range(0, 5):
				coords = self.randomCard()
				x = coords[0]
				y = self.cards[x].index(coords[1])
				self.hand.append(self.cards[x][y])
				self.popCard(x, y, 0)
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
		
	def popCard(self, x, y, z):
		#print "Popping: ", x, ':',self.cards[x][y]
		if z == 0:
			self.cards[x].pop(y)
		elif z == 1:
			self.hand.pop(y)
	
		
		
#START
player1 = Deck()

print 'Player 1: ',
player1.getHand()
player1.showHand()
player1.showDeck()

player2 = Deck(player1)

print 'Player 2: ',
player2.getHand()
player2.showHand()
player2.showDeck()

#Synchronize Decks after getHand()
player1.cards = player2.cards

player3 = Deck(player1)

print 'Player 3: ',
player3.getHand()
player3.showHand()
player3.showDeck()

#Synchronize Decks after getHand()
player1.cards = player3.cards

player4 = Deck(player1)

print 'Player 4: ',
player4.getHand()
player4.showHand()
player4.showDeck()
