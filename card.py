###################################################################################
# Date Created: 2024-12-18
# Date of Last Edit: 2024-12-18
###################################################################################
class Card: 
    id  = None
    squares = None 

    def __init__(self, id: int, squares: list[list[int]]):
        self.id = id
        self.squares = squares
    

