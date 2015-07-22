#http://www.reddit.com/r/dailyprogrammer/comments/psewf/2162012_challenge_8_intermediate/
from sys import argv

class IntToWords(object):
	def __init__(self):
		self.toWords = {
		"0":"", "1":"One", "2":"Two", "3":"Three", "4":"Four",
		"5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine",
		"10":"Ten", "11":"Eleven",  "12":"Twelve",  "13":"Thirteen", "14":"Fourteen", 
		"15":"Fifteen", "16":"Sixteen", "17":"Seventeen",  "18":"Eighteen",  "19":"Nineteen", 
		"20":"Twenty", "30":"Thirty", "40":"Forty",  "50":"Fifty", "60":"Sixty", "70":"Seventy", "80":"Eighty", "90":"Ninety",
		}
	
	def convertToWords(self, num):
		print num,
		num = str(num)
		ls = []
		for i in num:
			ls.append(int(i))
		
		
		
		if len(ls) == 1:
			if ls[0] == 0:
				print "Zero"
				ls.pop(0)
	
		while len(ls) != 0:
			if len(ls) == 9 and ls[0] != 0:
				print self.toWords[str(ls[0])], "Billion",
				ls.pop(0)
			elif len(ls) == 8 and ls[0] != 0:
				if ls[0] == 0:
						ls.pop(0)
				elif ls[0] == 1:
					print self.toWords[str(ls[0]) + str(ls[1])], "Million",
					ls.pop(0)
					ls.pop(0)
				elif ls[0] != 0:
					print self.toWords[str(ls[0]*10)], "Million",
					ls.pop(0)
			elif len(ls) == 7 and ls[0] != 0:
				print self.toWords[str(ls[0])], "Million",
				ls.pop(0)
			elif len(ls) == 6 and ls[0] != 0:
				print self.toWords[str(ls[0])], "Hundred Thousand",
				ls.pop(0)
			elif len(ls) == 5 and ls[0] != 0:
				if ls[0] == 0:
						ls.pop(0)
				elif ls[0] == 1:
					print self.toWords[str(ls[0]) + str(ls[1])], "Thousand",
					ls.pop(0)
					ls.pop(0)
				elif ls[0] != 0:
					print self.toWords[str(ls[0]*10)], "Thousand",
					ls.pop(0)
			elif len(ls) == 4 and ls[0] != 0:
				print self.toWords[str(ls[0])], "Thousand",
				ls.pop(0)
			elif len(ls) == 3 and ls[0] != 0:
				print self.toWords[str(ls[0])], "Hundred",
				ls.pop(0)
			elif len(ls) == 2:
				if ls[0] == 0:
					ls.pop(0)
				elif ls[0] == 1:
					print self.toWords[str(ls[0]) + str(ls[1])],
					ls.pop(0)
					ls.pop(0)
				elif ls[0] != 0:
					print self.toWords[str(ls[0]*10)],
					ls.pop(0)
			elif ls[0] != 0:
				print self.toWords[str(ls[0])],
				ls.pop(0)
			else:
				ls.pop(0)
		print
		
		
	
w = IntToWords()
if len(argv) == 2:
	w.convertToWords(argv[1])
else:
	for x in range (0, 100000000+1):
		if x% 10000 == 0:
			w.convertToWords(x)
