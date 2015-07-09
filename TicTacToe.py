from random import randint

board = ['1','2','3','4','5','6','7','8','9']

game_over = False

def print_board():
	print '_' * 61
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '|        ',board[0],'        |        ',board[1],'        |        ',board[2],'        |'
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '|','_'*17,'|','_'*17,'|','_'*17,'|'
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '|        ',board[3],'        |        ',board[4],'        |        ',board[5],'        |'
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '|','_'*17,'|','_'*17,'|','_'*17,'|'
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '|        ',board[6],'        |        ',board[7],'        |        ',board[8],'        |'
	print '|',' '*17,'|',' '*17,'|',' '*17,'|'
	print '_' * 61

def validate_choice(choice):
	while choice.upper() != 'X' and choice.upper() != 'O':
		choice = raw_input("Choose X's or O's: (X,O)")

def check_victory(num_turns):
	#WINS
	if num_turns > 2:
		#Horozontals
		if(board[0] == board[1] == board[2]):
			print board[0], "WINS"
			return True
		if(board[3] == board[4] == board[5]):
			print board[3], "WINS"
			return True
		if(board[6] == board[7] == board[8]):
			print board[6], "WINS"
			return True
		#Verticals
		if(board[0] == board[3] == board[6]):
			print board[0], "WINS"
			return True
		if(board[1] == board[4] == board[7]):
			print board[1], "WINS"
			return True
		if(board[2] == board[5] == board[8]):
			print board[2], "WINS"
			return True
		#Diagonals
		if(board[0] == board[4] == board[8]):
			print board[0], "WINS"
			return True
		if(board[6] == board[4] == board[2]):
			print board[6], "WINS"
			return True
	#DRAW
	if num_turns == 9:
		print "DRAW"
		return True
	#No wins or draw
	return False

print "Welcome to Blake's Tic-Tac-Toe Python Adventure"

choice = raw_input("Choose X's or O's: (X,O)")

validate_choice(choice)

if(choice.upper() == 'X'):
	turn = True
else:
	turn = False

print_board()
num_turns = 0

while game_over == False:

	if turn == True:
		print "It is X's turn:"
	else:
		print "It is O's turn:"

	space = input("Choose a space: (1 - 9)")

	
	while board[space-1] != '1' and board[space-1] != '2' and board[space-1] != '3' and board[space-1] != '4' and board[space-1] != '5' and board[space-1] != '6' and board[space-1] != '7' and board[space-1] != '8' and board[space-1] != '9':
		space = input("That space is taken or not available choose another space: (1 - 9)")


	if turn == True:
		board[space-1] = 'X'
	else: 
		board[space-1] = 'O'

	print_board()

	turn = not(turn)
	num_turns += 1

	game_over = check_victory(num_turns)

	#random = randint(0,8)
	#print random
	if game_over == True:
		choice = raw_input("Would you like to play again?: (Y,N)")
		if choice.upper() == 'Y':
			game_over = False
			num_turns = 0
			board = ['1','2','3','4','5','6','7','8','9']
			print_board()
		else:
			game_over = True
