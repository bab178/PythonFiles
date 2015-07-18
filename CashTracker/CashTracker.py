#BLAKE BORDOVSKY
from os import system, path
from time import strftime
from sys import stdout
from collections import OrderedDict

class CashTracker(object):

	def __init__(self):		
		self.startTime = strftime("%Y-%m-%d_%H-%M-%S")
		self.mainMenuItems = ['Add new item', 'Sell items', 'Show items',  'Exit']
		self.transactionTypes = {}
		self.totalCash = 0.00
		self.fileIsOpen = False
		self.stdout = file
		if path.isfile("CashTrackerInput.csv"):
			for item in self.file_split(open("CashTrackerInput.csv")):
				pass
			self.sortDict()
	def getDateTime(self):
		return strftime("%Y-%m-%d_%H-%M-%S")
		
	def sortDict(self):
		self.transactionTypes = OrderedDict(sorted(self.transactionTypes.items(), key=lambda t: t[0]))
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
				both = x.split('\n')
				x = both[0]
				self.transactionTypes[item] = x
				if switch == True:
					both = x.split('\n')
					front = both[0]
					if len(both) > 1:
						back = both[1]
						x = front
						self.transactionTypes[x] = back
					yield x
				else:
					item = x
					switch = True
									
			else:
				prev += s
				
		if prev:
			self.transactionTypes[prev] = item
			yield prev
	
	def mainMenu(self):
		print "Choose an option:\n"
		count = 1
		for x in self.mainMenuItems:
			print str(count) + ". " + x
			count += 1
		
		choice = -1
		while choice not in range(0, len(self.mainMenuItems) + 1):
				choice = input("\n> ")
		
		print
		if choice == 1:
			self.newTransaction()
			return 1
		elif choice == 2:
			self.promptTransaction()
			return 2
		elif choice == 3:
			self.showTransactions()
			return 3
		elif choice == 4:
			self.endSession()
			return 4
			
	def openFile(self):
		if(self.fileIsOpen == False):
			self.file = file(self.startTime+'.csv', 'a')
			line = "Time Sold ,Num Sold,Item,Price,Subtotal" 
			print >> self.file, line
			self.fileIsOpen = True
	
	def promptTransaction(self):
		num = 0
		choice = ""
		index = -1
		if len(self.transactionTypes) < 1:
			print "No Items in list."
			self.newTransaction()
		else:
			print "Choose an item:"
			count = 1
			dict = {}
			for x in self.transactionTypes:
				print str(count) + ". " + x
				dict[str(count)] = x
				count += 1

			while index not in range(0, len(self.transactionTypes) + 1):
				index = input("\n> ")

	
			choice = dict[str(index)]
			num = input("How many " + choice + "(s) are being sold: ")

			if choice in self.transactionTypes and num > 0:
				self.showQuote(choice, num, self.transactionTypes[choice])
		print

	def showQuote(self, name, num, price):
		price = float(price)
		num = int(num)
		subtotal = num*price
		#To Console
		print self.getDateTime(), str(num), name + "(s) at",
		print ('$%.2f' % price),
		print '=',
		print ('$%.2f' % subtotal)
		#To CSV
		line = self.getDateTime() + "," + str(num) + "," + name + "," + '$%.2f' % price + "," + '$%.2f' % subtotal
		if(self.fileIsOpen == False):
			self.openFile()
		print >> self.file, line
		self.totalCash += subtotal
		
	def newTransaction(self):
		name = ""
		while name == "":
			name = raw_input("Enter the name of your new item: ")
		price = -1.0
		while price < 0 :
			price = raw_input("Enter the price of your item: ")
		
		if price[0] in str(range(0,9)):
			self.transactionTypes[name] = price
			self.sortDict()
		else:
			print "Invalid Price."
		print
	
	def showTransactions(self):
		for x in self.transactionTypes:
			if len(x) < 7: 
				print x+":\t\t",
			else:
				print x+":\t",
			print '${:,.2f}'.format(float(self.transactionTypes[x]))
		print
	
	def endSession(self):
		print "Start Time: " + self.startTime + "\nEnd Time:   " + self.getDateTime() + "\n"
		print "TOTAL: " + str('${:,.2f}'.format(self.totalCash)) + "\n"
		#To CSV
		if(self.fileIsOpen == True):
			print >> self.file, ",,,,TOTAL: " + str('${:.2f}'.format(self.totalCash)) + "\n"
			print >> self.file, "Start Time: "
			print >> self.file, self.startTime
			print >> self.file, "End Time:"
			print >> self.file, self.getDateTime()
			self.file.close()
			print "File:", self.startTime+'.csv', "created."
		else:
			print "No file created."
		
#--------------------------------------------------------------------------------------------------

system('cls')
cash = CashTracker()
retVal = -1
while retVal != 4:
	retVal = cash.mainMenu()
