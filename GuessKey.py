from random import randint
from os import system

class GuessKey(object):
	def __init__(self):
		self.key = []
		self.keyLength = 4
		self.MAX = 4
		self.genKey()
		self.guesses = 0
	def genKey(self):
		for i in range(0,self.keyLength):
			self.key.append(randint(0,self.MAX))
		print "A", self.keyLength, "digit key has been generated.\n\nThe possible digits of the key are:",
		for i in range(0,self.MAX):
			print i,
	
	def showKey(self):
		print self.key
		
	def prompt(self):
		print
		temp = []
		for i in range(self.keyLength):
			temp.append(self.key[i])
		g = ""
		while len(g) != self.keyLength:
			if g != "":
				print "\nIncorrect key length or value."
			g = raw_input("\nEnter your " + str(self.keyLength) + " digit guess: ")
		self.guesses += 1
		guess = []
		for s in g:
			guess.append(int(s))
		
		pos = 0
		exist = 0
		for x in range(0,self.keyLength):
			if self.key[x] == guess[x]:
				pos += 1
				temp[x] = -1
		for x in range(0,self.keyLength):
			if guess[x] in temp:
				exist += 1
		if pos == self.keyLength:
			print "YOU WON WITH", self.guesses, "GUESSES!"
			return True
		else:
			print "\nPosition is correct in key:",pos,"\nExists otherwise in key:",exist
			return False
		
system('cls')
newKey = GuessKey()
while newKey.prompt() == False:
	pass
