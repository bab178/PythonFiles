from sys import stdout
from os import system, path, name

class AnimalGuess(object):

	def __init__(self):
		self.animals = {}
		self.attributes = []
		if path.isfile("animals.py"):
			for item in self.file_split(open("animals.py")):
				self.attributes.append(item)

	def file_split(self, f, delim=',', bufsize=1024):
			prev = ''
			item = ''
			x = ''
			front = ''
			back = ''
			switch = False
			while True:
				s = f.readline(bufsize)
				if not s:
					break
				split = s.split(delim)
				if len(split) > 0:
					item = split[0]
					x = split[1]
					yield item
					both = x.split('\n')
					x = both[0]
					self.animals[item] = x
					if switch == True:
						both = x.split('\n')
						front = both[0]
						if len(both) > 1:
							back = both[1]
							x = front
							self.animals[x] = back
						
					else:
						item = x
						switch = True
										
				else:
					prev += s
					
			if prev:
				self.animals[prev] = item
				yield prev
	
	def question(self):
		return raw_input("Is your animal " + self.attributes)
		
		
gameOver = False
animal = AnimalGuess()
while not gameOver:
	choice = animal.question()
	