class Game:									
	def __init__(self, new_player_name): #every function corresponding to the same class must call "self" (same iteration)
		self.player_name = new_player_name
		self.user = "NA"
		self.AI = "NA"
		self.winner = "NA"
		print("New Game for player " + str(new_player_name))

	def runGame(self):

		if ((self.user == 1 and self.AI == 3) or (self.user == 2 and self.AI == 1) or (self.user == 3 and self.AI == 2)):
			self.winner = "You win"

		elif((self.user == 1 and self.AI == 2) or (self.user == 2 and self.AI == 3) or (self.user == 3 and self.AI == 1)):
			self.winner = "You lose"

		elif((self.user == 1 and self.AI == 1) or (self.user == 2 and self.AI == 2) or (self.user == 3 and self.AI == 3)):
			self.winner = "You tied"
		else:
			self.winner = "invalid input, please try again"

		print(self.winner)

	def computer_response(self):

		import time	  #time is a library corresponding to time functions

		if(self.AI == 1):
			print("Computer picks rock")
		elif(self.AI == 2):
			print("Computer picks paper")
		elif(self.AI == 3):
			print("Computer picks scissors")

		time.sleep(2) # by default, the standard units of time in python is seconds


def main():
	import random #random is a library corresponding to randomly generated values

	name = input("Please enter your name: ")
	myGame = Game(name)
	myGame.user = int(input("Pick between a number between 1(rock), 2 (paper), 3(scissors): "))
	myGame.AI = (random.randint(1, 3))
	myGame.computer_response()
	myGame.runGame()


main()
