###################################################################################
# Date Created: 2024-12-18
# Date of Last Edit: 2024-12-18
###################################################################################
from game import Game
import vision

# Creating a new instance of the game. This preprocessing stage encodes all of 
# the bingo cards and puts them in a lookup table.
game1 = Game(vision.getCards())

print("Encoded bingo cards")
start = input("Start game? (y/n)")

# Start the game when the user says so.
while start != "y":
    start = input("Start game? (y/n)")

game1.playGame()

