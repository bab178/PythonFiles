#*****************************************************
#	Author: Blake Bordovsky
#	Date: 6/24/2015
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
				self.cards.append(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
				
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
		if(self.cards > 0):
			coords = []
			x = randint(0, len(self.cards)-1)
			i = choice(self.cards[x])
			y = self.cards[x].index(i)
			coords.append(x)
			coords.append(y)
			return coords
		
	def getHand(self):
		if self.numCards() > 0:
			coords = self.randomCard()
			self.hand.append(self.cards[coords[0]][coords[1]])

			del self.cards[coords[0]][coords[1]]
	
	def showHand(self):
		visual = []
		#Create visual cards
		for v in range(0, len(self.hand)):
			if v == 0:
				visual.append('-' * 7)
				visual.append('|  ' + '   |')
				visual.append('|  ' + '   |')
				
				if self.hand[v] == '10':
					visual.append('| ' + self.hand[v] + '  |')
				else:
					visual.append('|  ' + self.hand[v] + '  |')
					
				visual.append('|  ' + '   |')
				visual.append('|  ' + '   |')
				visual.append('-' * 7)
			else:
				visual[0] += (' -------')
				visual[1] += (' |  ' + '   |')
				visual[2] += (' |  ' + '   |')
				
				if self.hand[v] == '10':
					visual[3] += (' | ' + self.hand[v] + '  |')
				else:
					visual[3] += (' |  ' + self.hand[v] + '  |')
					
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
		if card.upper() not in self.hand:
			print "Player " + str(self.playerNum) + " mutters to themselves: I don't have any of those, better try a different card if I want to get any pairs."
			return False
		return True
			
	def aiPick(self):
		return choice(self.hand)
		
	def aiSelect(self, card, other = None):
		if card in other.hand:
			return 'yes'
		return 'Go Fish'
	
	def findPairs(self):
		uniques = []
		for i in range(len(self.hand)):
			for j in range(len(self.hand)):
				if self.hand[i] == self.hand[j] and i != j:
					if self.hand[i] not in uniques:
						uniques.append(self.hand[i])

		if len(uniques) > 0:
			for i in range(0, len(uniques)):
					print
					print 'Player', str(self.playerNum), 'found a pair of ' + str(uniques[i]) + "'s!"
			self.pairs += len(uniques)
			if self.playerNum == 1:
				self.showHand()
				print 'You remove them from your hand and gain a point for each pair.'
			for p in range(len(uniques)):
				del self.hand[self.hand.index(uniques[p])]
				del self.hand[self.hand.index(uniques[p])]
		print 'Player', str(self.playerNum) + "'s score is:      ", str(self.pairs) + '.'
				
	def aiFish(self, select, card, other = None):
		#You have it and Admit it
		if(select.lower() == 'yes' or select.lower() == 'ye' or select.lower() == 'yeah' or select.lower() == 'yar' or select.lower() == 'y') and (self.playerNum != 1) and (card in other.hand):
			print 'Player ' + str(other.playerNum) + " says: Darn you found my " + str(card) + "!"
			self.hand.append(card)
			print card, other.hand
			if card in other.hand:
				del other.hand[other.hand.index(card)]
			self.findPairs()
		#You have it and Lie
		elif(select.lower() != 'yes' and select.lower() != 'ye' and select.lower() != 'yeah' and select.lower() != 'yar' and select.lower() != 'y') and (self.playerNum != 1) and (card in other.hand):
			print 'Player ' + str(other.playerNum) + ' LIED!!! -2 points!'
			other.pairs -= 2
			self.hand.append(card)
			if card in other.hand:
				del other.hand[other.hand.index(card)]
			self.findPairs()
		#You Don't have it and Lie
		elif(select.lower() == 'yes' or select.lower() == 'ye' or select.lower() == 'yeah' or select.lower() == 'yar' or select.lower() == 'y') and (self.playerNum != 1) and (not(card in other.hand)):
			print 'Player ' + str(other.playerNum) + ' LIED!!! -2 points!'
			other.pairs -= 2
			self.hand.append(card)
			if card in other.hand:
				del other.hand[other.hand.index(card)]
			self.findPairs()

		else:
			print 'Player ' + str(other.playerNum) + " says: Go Fish!"
		
	def goFish(self, card, other = None):
		foundOne = False
		card = card.upper()
		for i in other.hand:
			if str(i) == str(card):
				system('cls')
				foundOne = True
				print 'Player ' + str(other.playerNum) + " says: You got my ", card, "!"
				self.hand.append(card)
				del other.hand[other.hand.index(card)]
				self.findPairs()
				self.showHand()
				print "Next player's turn..."
				sleep(4)
		print
		if foundOne == False:
			print 'Player ' + str(other.playerNum) + " says: Go Fish."
	
#*********************************************************************
#END class Deck
#*********************************************************************

def startGame(prevPlayer):
	numPlayers = 1
	players = []
	
	while numPlayers <= 1 or numPlayers > 4:
		numPlayers = input('How many players do you want? (2-4): ')
	
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
	player.getHand()
	player.getHand()
	player.getHand()
	player.printNumCards()
	player.findPairs()
	if player.playerNum == 1:
		player.showHand()

def runInput(player, players):
	selectedPlayer = 1
	while(selectedPlayer == 1 or selectedPlayer > len(players)):
		selectedPlayer = input('Player ' + str(player.playerNum) + " says: Hey Player <2, 3, 4>!: ")

	select = raw_input('Player ' + str(player.playerNum) + " says: Do you have any _'s? ")
	player.pick(select)
	if(player.playerNum == 1):
		player.goFish(select, players[selectedPlayer - 1])
	sleep(2)
			
def runAI(player, players):
	flag = False
	selectedPlayer = player.playerNum
	#available = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

	otherPlayers = players
	
	while selectedPlayer == player.playerNum:
		selectedPlayer = choice(otherPlayers).playerNum
	card = player.aiPick()
	
	print 'Player ' + str(player.playerNum) + " says: Hey Player ", str(selectedPlayer) +'! '
	if selectedPlayer == 1:
		print 'Your Hand:'
		players[0].showHand()
		select = raw_input('Player ' + str(player.playerNum) + " says: Do you have any " + card + "'s? (Yes/Go Fish)")
		sleep(2)
	else:
		print 'Player ' + str(player.playerNum) + " says: Do you have any " + card + "'s? (Yes/Go Fish)"
		select = player.aiSelect(card, players[selectedPlayer - 1])
		player.aiFish(select, card, players[selectedPlayer - 1])
		sleep(4)
	
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


#START

#Mac/Linux
#system('clear')

#Windows
system('cls')

#		     Deck(playerNum)
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
		if i == player1:
			runInput(i, players)
		else:
			runAI(i, players)
		system('cls')
	print 'End of round ' + str(round) + '.'
	gameOver = checkEnd(players)
	score(players)
	round += 1
print 'Game Over'
score(players)
winner = 1
for w in players:
	if i.pairs > winner.pairs:
		winner = i.playerNum
print 'Player', winner, 'wins!'
