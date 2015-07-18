#BLAKE BORDOVSKY
from os import system, path, name
from time import strftime
from sys import stdout
from collections import OrderedDict

class CashTracker(object):

	def __init__(self):		
		self.startTime = strftime("%Y-%m-%d_%H-%M-%S")
		self.mainMenuItems = ['Sell items', 'Show items',  'End Session']
		self.transactionTypes = {}
		self.totalCash = 0.00
		self.fileIsOpen = False
		self.stdout = file
		self.itemNames = []
		if path.isfile("CashTrackerInput.csv"):
			for item in self.file_split(open("CashTrackerInput.csv")):
				self.itemNames.append(item)
	
	def getDateTime(self):
		return strftime("%Y-%m-%d_%H-%M-%S")

	def sortDict(self,temp):
		#self.transactionTypes = OrderedDict(sorted(self.transactionTypes.items(), key=lambda t: t[0]))
		pass
		
	def clear(self):
		if name == 'nt':
			return system('cls')
		else:
			return system('clear')
	
	def openFile(self):
		if(self.fileIsOpen == False):
			self.file = file(self.startTime+'.csv', 'a')
			line = "Time Sold ,Num Sold,Item,Price,Subtotal" 
			print >> self.file, line
			self.fileIsOpen = True

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
				self.transactionTypes[item] = x
				if switch == True:
					both = x.split('\n')
					front = both[0]
					if len(both) > 1:
						back = both[1]
						x = front
						self.transactionTypes[x] = back
					
				else:
					item = x
					switch = True
									
			else:
				prev += s
				
		if prev:
			self.transactionTypes[prev] = item
			yield prev
	
	def mainMenu(self):
		print "Main Menu:\n"
		count = 1
		for x in self.mainMenuItems:
			print str(count) + ". " + x
			count += 1
		
		choice = -1
		while choice not in range(0, len(self.mainMenuItems) + 1):
				choice = input("\n> ")
		
		print
		if choice == 1:
			self.promptTransaction()
			return 1
		elif choice == 2:
			self.showItems()
			return 2
		elif choice == 3:
			self.endSession()
			return 0
			
	def promptTransaction(self):
		self.clear()
		index = -1
		while(index != 0):
			index = -1
			num = 0
			choice = ""
			if len(self.itemNames) < 1:
				print "No Items in list."
				self.newTransaction()
			else:
				print "Choose an item:"
				count = 1
				dict = {}
				for x in self.itemNames:
					print str(count) + ". " + x
					dict[str(count)] = x
					count += 1
				print "\n0. Exit Sales"
				while index not in range(0, len(self.itemNames) + 1):
					index = input("\n> ")
				if index == 0:
					self.clear()
					break
			
				choice = dict[str(index)]
				while num < 1:
					num = input("How many " + choice + "(s) are being sold: ")

				if choice in self.transactionTypes and num > 0:
					self.showQuote(choice, num, self.transactionTypes[choice])
			print

	def showQuote(self, item, num, price):
		price = float(price)
		num = int(num)
		subtotal = num*price
		#To Console
		self.clear()
		print self.getDateTime(), str(num), item + "(s) at",
		print ('$%.2f' % price),
		print '=',
		print ('$%.2f' % subtotal)
		#To CSV
		line = self.getDateTime() + "," + str(num) + "," + item + "," + '$%.2f' % price + "," + '$%.2f' % subtotal
		if(self.fileIsOpen == False):
			self.openFile()
		print >> self.file, line
		self.totalCash += subtotal
		
	def newTransaction(self):
		item = ""
		while item == "":
			item = raw_input("Enter the name of your new item: ")
		price = -1.0
		while price < 0 :
			price = raw_input("Enter the price of your item: ")
		
		if price[0] in str(range(0,9)):
			self.transactionTypes[item] = price
			#self.sortDict()
		else:
			print "Invalid Price."
		print
	
	def showItems(self):
		self.clear()
		for x in self.itemNames:
			if len(x) < 7: 
				print x+":\t\t",
			else:
				print x+":\t",
			print '${:,.2f}'.format(float(self.transactionTypes[x]))
		print
	
	def endSession(self):
		self.clear()
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


cash = CashTracker()
cash.clear()
retVal = -1
while retVal != 0:
	retVal = cash.mainMenu()
