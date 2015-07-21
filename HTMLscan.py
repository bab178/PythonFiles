#http://www.reddit.com/r/dailyprogrammer/comments/qhe4u/342012_challenge_17_intermediate/
import urllib2
import ctypes
from os import name, system
import sys


class HTMLscan(object):
	def __init__(self):
		self.url = sys.argv[1]
		self.source = urllib2.urlopen(self.url)
			
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
		if not name == 'nt':
			return self.bcolors["OKGREEN"] + str + self.bcolors["ENDC"]
		else:
			return str
		
	def badPrint(self, str):
		if not name == 'nt':
			return self.bcolors["WARNING"] + str + self.bcolors["ENDC"]
		else:
			return str
	
	
	def find(self):
		matches = []
		target = sys.argv[2]
		count = 0
		for i in self.source: 
			line = self.source.read()
			#count broken
			count += 1
			words = line.split("\n")
			for i in words:
				if i.find(target) != -1:
					print i[:i.find(target)] +  self.goodPrint(i[i.find(target):i.find(target)+len(target)]) + i[i.find(target)+len(target):]
					matches.append(i)
		
		if len(matches) > 0:
			print "Found " + self.goodPrint(str(len(matches))) + " instances of " + self.goodPrint(target)
		else:
			print self.badPrint("Nothing Found")
if name == 'nt':
	system('cls')
else:
	system('clear')
scan = HTMLscan()
scan.find()
