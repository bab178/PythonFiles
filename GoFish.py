#*****************************************************
#	Author: Blake Bordovsky
#	Date: 6/24/2015
#	GoFish.py
#   Version: 1.0
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
				#Pop card from deck
				del self.cards[coords[0]][coords[1]]
	
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
			
	def pick(self, card):
		if card.upper() not in str(self.hand):
			print "Player " + str(self.playerNum) + " mutters to themselves: I don't have any of those, better try a different card."
			return False
		return True
			
	def findPairs(self):
		num = 0
		uniques = []
		for i in range(len(self.hand)):
			for j in range(len(self.hand)):
				if self.hand[i] == self.hand[j] and i != j:
					num += 1
					if self.hand[i] not in uniques:
						uniques.append(self.hand[i])

		if num > 0:
			for i in range(0, len(uniques)):
					print
					print 'Pair of ' + str(uniques[i]) + "'s found!"
			self.pairs += num/2
			self.showHand()
			print 'Removing pairs from hand.'
			for p in range(len(uniques)):
				del self.hand[self.hand.index(uniques[p])]
				del self.hand[self.hand.index(uniques[p])]
				
	def goFish(self, card, other = None):
		print 'goFish'
		toPop = []
		for i in self.hand:
			 print i, '==', card
			 if i == card:
				toPop.append(self.hand.index(card))
		if len(toPop) > 1:
			print other.playerNum, "says: You got my ", toPop[0], "'s!"
			self.hand.append(other.hand.index[other.hand[toPop[0]]])
		else:
			print
			print 'Player ' + other.playerNum + " says: Go Fish."
	
#*********************************************************************
#END class Deck
#*********************************************************************

def startGame(prevPlayer):
	numPlayers = 1
	players = []
	
	while numPlayers <= 1:
		#numPlayers = input('How many players do you want? (2-4)')
		print 'How many players do you want? (2)'
		#hardcoded
		numPlayers = 2
	
	if numPlayers == 2:
		players.append(player1)
		players.append(player2)
	elif numPlayers == 3:
		players.append(player1)
		players.append(player2)
		players.append(player3)
	elif numPlayers == 4:
		players.append(player1)
		players.append(player2)
		players.append(player3)
		players.append(player4)
		
	for i in players:
		i.cards = prevPlayer.cards
		prevPlayer = i
		i.getHand()
	
	return players


def gameSeq(player):
	player.getHand()
	player.printNumCards()
	player.findPairs()
	player.showHand()

def runInput(player, players):
	flag = False
	#hardcoded
	#selectedPlayer = 0
	selectedPlayer = 2
	while(selectedPlayer not in range(1,4)) and (not flag):
		#selectedPlayer = input('Player ' + str(player.playerNum) + " says: Hey Player <1, 2, 3, 4>!: ")
		print 'Player ' + str(player.playerNum) + " says: Hey Player <1, 2, 3, 4>!: (2)"
		select = raw_input('Player ' + str(player.playerNum) + " says: Do you have any ___'s?")
		flag = player.pick(select)
		if(selectedPlayer in range(1,4)):
			player.goFish(select, players[selectedPlayer - 1])

def checkEnd(players):
	sum = 0
	for p in players:
		sum += p.numCardsInHand()
	if sum == 0:
		return True
	else:
		return False
		
def score(players):
	count = 1
	print
	print '-------Scoreboard-------\n'
	for p in players:
		print 'Player', count, 'Score:', p.pairs, '\n'
		count += 1
	print '------------------------\n'
	sleep(5)

#START

#Mac/Linux
#system('clear')

#Windows
system('cls')

#		  Deck(playerNum)
player1 = Deck(1)
player2 = Deck(2)
player3 = Deck(3)
player4 = Deck(4)

prevPlayer = player1

players = startGame(prevPlayer)

gameOver = False

print 'All', len(players), 'players have drawn their hands.'
round = 1
while not gameOver:
	for i in players:
		i.cards = prevPlayer.cards
		prevPlayer = i
		gameSeq(i)
		runInput(i, players)
		sleep(3)
		system('cls')
	print 'End of round ' + str(round) + '.'
	gameOver = checkEnd(players)
	score(players)
	round += 1
print 'Game Over'
score(players)