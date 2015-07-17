from time import gmtime, strftime
from os import system
from sys import stdout

class CashTracker(object):
	startTime = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
	orig_stdout = stdout
	file = file(startTime+'.txt', 'a')
	stdout = file
	transactionTypes = []
	transactionPrices = []
	mainMenuItems = ['Add new item', 'Sell items', 'Show items',  'Exit']
	totalCash = 0.00
	

	def __init__(self):		
		pass
	
	def output(self, str):
		print >> self.file, str
	
	def getDateTime(self):
		return strftime("%Y-%m-%d_%H:%M:%S", gmtime())
	
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
			
	
	def promptTransaction(self):
		num = 0
		choice = -1
		if len(self.transactionTypes) < 1:
			self.newTransaction()
		else:
			print "Choose an item:"
			count = 1
			for x in self.transactionTypes:
				print str(count) + ". " + x
				count += 1
			
			while choice not in range(0, len(self.transactionTypes) + 1):
				choice = input("\n> ")
			
			num = input("How many " + self.transactionTypes[choice - 1] + "(s) are being sold: ")
			self.showQuote(self.transactionTypes[choice - 1], self.transactionPrices[choice - 1], num)
		print

	def showQuote(self, name, num, quote):
		print self.getDateTime() + " " + str(num) + " " + name + "(s) at " + str('${:,.2f}'.format(quote) + " = " + str('${:,.2f}'.format(num*quote)))
		self.output(self.getDateTime() + " " + str(num) + " " + name + "(s) at " + str('${:,.2f}'.format(quote)) + " = " + str('${:,.2f}'.format(num*quote)))
		self.totalCash += num*quote
		
	def newTransaction(self):
		name = raw_input("Enter the name of your new item: ")
		self.transactionTypes.append(name)
		price = -1
		while price < 0:
			price = input("Enter the price of your item: ")
		self.transactionPrices.append(price)
		print
	
	def showTransactions(self):
		num = 0
		for x in self.transactionTypes:
			print x + ": " + str('${:,.2f}'.format(self.transactionPrices[num]))
			num += 1
		print
	
	def endSession(self):
		print "Start Time: " + self.startTime + "\nEnd Time:   " + self.getDateTime() + "\n"
		print "TOTAL: " + str('${:,.2f}'.format(self.totalCash)) + "\n"
		self.output("Start Time: " + self.startTime + "\nEnd Time:   " + self.getDateTime() + "\n")
		self.output("TOTAL: " + str('${:,.2f}'.format(self.totalCash)) + "\n")
		stdout = self.orig_stdout
		self.file.close()

system('clear')
cash = CashTracker()
retVal = -1
while retVal != 4:
	retVal = cash.mainMenu()
