import urllib, urllib2
from bs4 import BeautifulSoup, Comment
import random

#Get raw HTML
url='http://www.disneymovieslist.com/animated-disney-movies.asp'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

#Collect movies from page
def collect():
	array = []
	
	#(Specific to this page)
	for row in soup.find_all('td',attrs={"class" : "content"}):
		array.append(row.text)
		
	#Remove first four garbage items
	del array[0]
	del array[0]
	del array[0]
	del array[0]
	
	return array
	
#Print all movies
def display_all(array):
	for m in array:
		print m
		
def pick_random(array):
	print(random.choice(array))
		
movies = collect()
# display_all(movies)
pick_random(movies)


