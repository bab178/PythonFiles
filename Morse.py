#http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
class MorseTranslator(object):
	def __init__(self):
		self.sample = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
		self.toSym = {
		".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E",
		"..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", 
		"-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O",
		".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", 
		"..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y",
		"--..":"Z", "-----":"0", ".----":"1", "..---":"2", "...--":"3",
		"....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8",
		"----.":"9", "/":" ",
		}
		
	def printMorse(self):
		print self.sample
	
	def translate(self, sample):
		words = sample.split(' ')
		print words
		for i in words:
			print self.toSym[i],
		print
	
#----------------------------------------------------------------------------------------------------

babel = MorseTranslator()
babel.printMorse()
babel.translate(babel.sample)
