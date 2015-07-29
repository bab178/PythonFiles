import time

parts = 100
delay = 0.01

for x in range(1,parts):
	y = (x / 10)
	print 'Now loading: [' + '#' * y  + '|' +  ' ' * (10 - y) + ']' + '\r' ,
	time.sleep(delay)

print 'Now loading: [' + '#' * 11
print "DONE"