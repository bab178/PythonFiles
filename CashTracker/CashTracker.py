#BLAKE BORDOVSKY
from os import system
from time import strftime
from sys import stdout

class CashTracker(object):

	def __init__(self):		
		self.startTime = strftime("%Y-%m-%d_%H-%M-%S")
		self.orig_stdout = stdout
		self.file = file(self.startTime+'.csv', 'a')
		self.stdout = file
		self.transactionTypes = {'Glowstick':'2', 'Ticket':'10'}
		self.mainMenuItems = ['Add new item', 'Sell items', 'Show items',  'Exit']
		self.totalCash = 0.00
		line = "Time Sold ,Num Sold,Item,Price,Subtotal" 
		print >> self.file, line

	def getDateTime(self):
		return strftime("%Y-%m-%d_%H-%M-%S")
	
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
		choice = ""
		index = -1
		if len(self.transactionTypes) < 1:
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
		print >> self.file, line
		self.totalCash += subtotal
		
	def newTransaction(self):
		name = raw_input("Enter the name of your new item: ")
		price = -1
		while price < 0:
			price = input("Enter the price of your item: ")
		self.transactionTypes[name] = price
		print
	
	def showTransactions(self):
		num = 0
		for x in self.transactionTypes:
			print x + ": " + str('${:,.2f}'.format(int(self.transactionTypes[x])))
			num += 1
		print
	
	def endSession(self):
		print "Start Time: " + self.startTime + "\nEnd Time:   " + self.getDateTime() + "\n"
		print "TOTAL: " + str('${:,.2f}'.format(self.totalCash)) + "\n"
		#To CSV
		print >> self.file, ",,,,TOTAL: " + str('${:.2f}'.format(self.totalCash)) + "\n"
		print >> self.file, "Start Time: "
		print >> self.file, self.startTime
		print >> self.file, "End Time:"
		print >> self.file, self.getDateTime()
		self.file.close()
		
		
#--------------------------------------------------------------------------------------------------

system('cls')
cash = CashTracker()
retVal = -1
while retVal != 4:
	retVal = cash.mainMenu()
