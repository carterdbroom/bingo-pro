###################################################################################
# Date Created: 2024-12-18
# Date of Last Edit: 2024-12-18
###################################################################################
import card
class Game: 
    cards = None
    global lookUpTable

    # In the constructor we initialize 
    def __init__(self, cards: list[list[int]]):
        self.cards = cards
        lookUpTable = {}
        for card in enumerate(cards):
            for square in card.squares():
                for row in range(5):
                    for column in range(5):
                        number = square[row][column]
                        if number not in lookUpTable:
                            lookUpTable[number] = []
                        lookUpTable[number].append((card.id, row, column, False))    

    # Marks a number in the lookup table.
    def markNumber(number: int) -> None:
        for spot in lookUpTable[number]:
            spot[3] = True

    # Checks every row for a line win.
    def checkRowWin():
        return None
    
    # Checks every column for a line win.
    def checkColumnWin():
        return None
    
    # Checks every diagonal for a line win.
    def checkDiagonalWin():
        return None
    
    # Checks every square for a full square win. 
    def checkSquareWin():
        return None
    
    # Checks every card for a full card win.
    def checkCardWin():
        return None
    
    # Runs the game after preprocessing is done.
    def playGame() -> None:
        
        answer = ""
        calledNumbers = []
        
        # The starting prompts for user.
        print("Here the commands:")
        print("q ---> Quit Game")
        print("l ---> Display List of Called Numbers")
        print("w ---> Change What Mode You Are In")
        print("One full line counts as a win by default, change mode to fit your needs")
        print("To mark a number, simply enter the number that was called")

        # By default a win counts as one full line.
        gameMode = "line"

        # Starting the game.
        answer = input("Enter a command or the number that was called out: ")
        while answer != "q":
            
            # If the user commands, display the list of called numbers.
            if answer == "l":
                print(calledNumbers)
            
            # If the answer is a valid positive bingo number then add it to the list
            # of called numbers and check for wins. Indicate that it has been marked.
            if answer.isdigit():
                calledNumbers.append(int(answer))
                if gameMode == "line":
                    checkRowWin()
                    checkColumnWin()
                    checkDiagonalWin()
                elif gameMode == "square":
                    checkSquareWin()
                elif gameMode == "card":
                    checkCardWin()
                print("Marked that spot!")
            
            # If the user commands, change the conditions for a win.
            if answer == "w":
                newMode = input("Enter what mode you want to switch to (line/square/card):")
                while True:
                    if newMode == "line":
                        gameMode = "line"
                        break
                    elif newMode == "square":
                        gameMode = "sqaure"
                        break
                    elif newMode == "card":
                        gameMode = "card"
                        break
                    print("Not a valid input!")
                    newMode = input("Enter what mode you want to switch to (line/square/card):")

            # Continue to play the game (jumps back to the top of the while loop).
            answer = input("Enter a command or the number that was called out: ")
        
        print("Thanks for playing!")
