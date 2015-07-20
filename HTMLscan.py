#http://www.reddit.com/r/dailyprogrammer/comments/qhe4u/342012_challenge_17_intermediate/
import urllib2
import ctypes
from os import name


class HTMLscan(object):
	def __init__(self):
		self.source = urllib2.urlopen("http://www.reddit.com/r/dailyprogrammer/comments/qhe4u/342012_challenge_17_intermediate/")
		if name == "nt":
			self.windows = True
		else:
			self.windows = False
			
		self.bcolors = {
		"HEADER":"\033[95m",
		"OKBLUE":"\033[94m",
		"OKGREEN":"\033[92m",
		"WARNING":"\033[93m",
		"FAIL":"\033[91m",
		"ENDC":"\033[0m",
		"BOLD":"\033[1m",
		"UNDERLINE":"\033[4m"
		}
		
	def goodPrint(self, str):
		return self.bcolors["OKGREEN"] + str + self.bcolors["ENDC"]
		
	def badPrint(self, str):
		return self.bcolors["WARNING"] + str + self.bcolors["ENDC"]
	
	
	def find(self):
		matches = []
		
		target = raw_input("Find: " + self.bcolors["HEADER"])
		print self.bcolors["ENDC"]
		
		count = 0
		for i in self.source: 
			line = self.source.read()
			#count broken
			count += 1
			words = line.split("\n")
			for i in words:
				if i.find(target) != -1:
					print "Line",count, ":\n",  i[:i.find(target)] +  self.goodPrint(i[i.find(target):i.find(target)+len(target)]) + i[i.find(target)+len(target):]
					matches.append(i)
		
		if len(matches) > 0:
			print "Found " + self.goodPrint(str(len(matches))) + " instances of " + self.goodPrint(target)
		else:
			print self.badPrint("Nothing Found")
		
		
			
scan = HTMLscan()
scan.find()
