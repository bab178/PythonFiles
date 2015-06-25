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
	
	def __init__(self, playerNum, other = None):
		self.playerNum = playerNum
		self.cards = []
		self.hand = []
		self.pairs = 0
		if other:
			self.cards = other.cards
		else:
			#Get Deck
			for suits in range(0,4):
				self.cards.append(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
				
	def showDeck(self):
		if len(self.cards) != 0:
			for suit in range(4):
				print self.cards[suit]
		
		self.printNumCards()

	def numCards(self):
		sum = 0
		if len(self.cards) != 0:
			for d in range(4):
				sum += len(self.cards[d]) 
		return sum
		
	def printNumCards(self):
		print "Cards left: ", self.numCards()
		
	def numCardsInHand(self):
		return len(self.hand)
	
	def randomCard(self):
		coords = []
		x = randint(0, len(self.cards)-1)
		i = choice(self.cards[x])
		y = self.cards[x].index(i)
		coords.append(x)
		coords.append(y)
		return coords
		
	def getHand(self):
		if self.numCards() >= 1 and len(self.hand) < 5:
			for h in range(0, 5 - len(self.hand)):
				coords = self.randomCard()
				self.hand.append(self.cards[coords[0]][coords[1]])
				self.popCard(coords[0], coords[1])
	
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
		else:
			print 'Player', self.playerNum, "'s hand is empty"
		print
		
	def popCard(self, x, y):
		#print "Popping: ", x, ':',self.cards[x][y]
		del self.cards[x][y]
			
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
player1 = Deck(1)
player2 = Deck(2)
player3 = Deck(3)
player4 = Deck(4)

#print 'Player', player1.playerNum, ': '
#player1.getHand()
#player1.checkHand()
#player1.showHand()
#player1.showDeck()

players = []
players.append(player1)
players.append(player2)
players.append(player3)
players.append(player4)

prevPlayer = player1

for i in players:
	i.cards = prevPlayer.cards
	prevPlayer = i
	i.getHand()
	
print 'All', len(players), 'players have drawn their hands.'
round = 1

while len(players[0].hand) != 0 and len(players[1].hand) and len(players[2].hand) and len(players[3].hand):
	for i in players:
		i.cards = prevPlayer.cards
		prevPlayer = i
		i.getHand()
		i.printNumCards()
		i.showHand()
		choice = raw_input('Player ' + str(i.playerNum) + ', pick a card: ')
		i.pick(choice)
		system('cls')
	print 'End of round ' + str(round) + '.'
	score(players)
	round += 1
print 'Game Over'
score(players)