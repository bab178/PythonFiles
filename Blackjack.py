from random import choice
from random import randint
from os import system
from time import sleep

class Deck(object):
	
	def __init__(self, playerNum, other = None):
		self.playerNum = playerNum
		self.cards = []
		self.hand = []
		if other:
			self.cards = other.cards
		else:
			#Get Deck
			for suits in range(4):
				self.cards.append(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
	
	def randomCard(self):
		if(self.cards > 0):
			coords = []
			x = randint(0, len(self.cards)-1)
			i = choice(self.cards[x])
			y = self.cards[x].index(i)
			coords.append(x)
			coords.append(y)
			return coords
		
	def hitMe(self):
		if len(self.cards) > 0:
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
		print

	def getTotal(self):
		total = 0
		aces = 0
		for card in self.hand:
			if card == 'A':
				aces += 1
			elif card == '2':
				total += 2
			elif card == '3':
				total += 3 
			elif card == '4':
				total += 4 
			elif card == '5':
				total += 5 
			elif card == '6':
				total += 6 
			elif card == '7':
				total += 7 
			elif card == '8':
				total += 8 
			elif card == '9':
				total += 9 
			elif card == '10' or card == 'J' or card == 'Q' or card == 'K':
				total += 10
				
		for a in range(aces):
			if total + 11 <= 21:
				total += 11
			else:
				total += 1
			
		return total
	
	def prompt(self):
		print
		select = raw_input('Hit or Stay? (1,2)')
		while not select == '1' and not select == '2':
			select = raw_input('Hit or Stay? (1,2)')
		print
		return select

player = Deck(1)
#send players' deck to dealer
dealer = Deck(2, player)

player.hitMe()
player.hitMe()

dealer.hitMe()
dealer.hitMe()

dealerStay = False

while player.getTotal() < 21 and dealer.getTotal() < 21 and dealerStay == False:
	system('cls')
	player.showHand()
	print "Player Total:", player.getTotal(), "\n"

	dealer.showHand()
	print "Dealer Total:", dealer.getTotal()
	select = player.prompt()
	if select == '1':
		player.hitMe()
	else:
		#finish dealer
		if dealer.getTotal() + 7 < 21:
			dealer.hitMe()
			print "\nDealer hits.\n"
			sleep(2)
		else:
			print "\nDealer stays.\n"
			sleep(2)
			dealerStay = True

system('cls')
player.showHand()
print "Player Total:", player.getTotal(), "\n"

dealer.showHand()
print "Dealer Total:", dealer.getTotal()
			
if player.getTotal() <= 21 and dealer.getTotal() > 21:
	print "DEALER BUSTS: YOU WIN!"
elif player.getTotal() <= 21 and dealer.getTotal() <= 21:
	if player.getTotal() == dealer.getTotal():
		print "DRAW!"
	if player.getTotal() == 21:
		print "BLACKJACK: YOU WIN!"
	elif player.getTotal() > dealer.getTotal():
		print "BEST HAND: YOU WIN!"
	else:
		print "WORST HAND: YOU LOSE!"
else:
	print "PLAYER BUSTS: YOU LOSE!"
		
