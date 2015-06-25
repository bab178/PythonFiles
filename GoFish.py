#*****************************************************
#	Author: Blake Bordovsky
#	GoFish.py
#  Version: 1.0
#*****************************************************
from random import choice
from random import randint
from os import system
from time import sleep

class Deck(object):
	
	def __init__(self, other = None):
		self.cards = []
		self.hand = []
		self.pairs = 0
		if other:
			self.cards = other.cards
		else:
			#Get Deck
			for d in range(0,4):
				self.cards.append(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
				
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
		
	def numCardsInHand(self):
		return len(self.hand)
	
	def randomCard(self):
		x = randint(0, len(self.cards)-1)
		y = choice(self.cards[x])
		coords = [x,y]
		return coords
		
	def getHand(self):
		if self.numCards() >= 5 and len(self.hand) < 5:
			for h in range(0, 5 - len(self.hand)):
				coords = self.randomCard()
				x = coords[0]
				y = self.cards[x].index(coords[1])
				self.hand.append(self.cards[x][y])
				self.popCard(x, coords[1])
	
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
				else:
					visual[3] += (' |  ' + str(self.hand[v]) + '  |')
					
				visual[4] += (' |  ' + '   |')
				visual[5] += (' |  ' + '   |')
				visual[6] += (' -------')
				
		if len(self.hand) != 0:
			for v in range(0, 7):
				print visual[v]
		print
		
	def popCard(self, x, y):
		#print "Popping: ", x, ':',self.cards[x][y]
		del self.cards[x][self.cards[x].index(y)]
			
	def pick(self, card):
		if card.upper() not in str(self.hand):
			print "Card not in hand. Try another card."
			return
		if card.upper() != 'K' and card.upper() != 'Q' and card.upper() != 'J' and card.upper() != 'A':
			self.hand.pop(self.hand.index(int(card)))
		else:
			self.hand.pop(self.hand.index(card.upper()))
	#BROKEN		
	# def checkHand(self):
		# ind = []
		# card = self.hand[0]
		# if card not in self.hand:
			# return
		# for i in self.hand:
			# if i == card and self.hand.index(i) != self.hand.index(card):
				# ind.append(card)
			# card = i
		# if len(ind) > 1:
			# print "Pair(s) found", len(ind)/2
	
	def checkOther(self, card, other = None):
		ind = []
		for i in self.hand:
			if i == card:
				ind.append(self.hand.index(card))
		if len(ind) > 1:
			print "Pair found"
#*********************************************************************
#END Deck() class11

def score(players):
	count = 1
	print
	print '-------Scoreboard-------\n'
	for p in players:
		print 'Player', count, 'Score:', p.pairs, '\n'
		count += 1
	print '------------------------\n'

#START
system('cls')
player1 = Deck()

print 'Player 1: '
player1.getHand()
#player1.checkHand()
player1.showHand()
#player1.showDeck()

#Copies cards over from player1 and gives empty hand
player2 = Deck()
player3 = Deck()
player4 = Deck()


players = []
players.append(player1)
players.append(player2)
players.append(player3)
players.append(player4)

prevPlayer = player1
count = 1
for i in players:
	if i == 0:
		continue
	#print 'Player', count, ':'
	i.getHand()
	#i.showHand()
	#i.showDeck()
	i.cards = prevPlayer.cards
	prevPlayer = i
	count += 1
print 'All', count - 1, 'players have drawn their hands.'
score(players)
while player1.numCardsInHand() > 0:
	choice = raw_input('Pick a card: ')
	player1.pick(choice)
	player1.showHand()