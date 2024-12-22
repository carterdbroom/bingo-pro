###################################################################################
# Date Created: 2024-12-18
# Date of Last Edit: 2024-12-19
###################################################################################
import cv2
import easyocr
from pathlib import Path
from card import Card

# The image path of where our test image is. 
sourceDir = Path('C:/bingoImages/')
files = sourceDir.iterdir()

# Making our reader for the image.
reader = easyocr.Reader(['en'])

# Will hold all the text in the image.
data = []

# Iterating through all the files in the directory.
for file in files:
    # Preparing image input and grayscaling it for easier reading.
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecting text in the image.
    textData = reader.readtext(gray_image)
    # Looping through the data to put the text in the data array.
    for (boundingBox, text, confidence) in textData:
        data.append(text)
    data.append("|END|")

# This is list of Card objects which will encapsulate the data.
cards = []

# Encoding everything from the data array into Card opjects.
for idx, val in enumerate(data):
    # Get id and squares
    # Encode into cards
    None

# Returns the list of Card objects.
def getCards() -> list[Card]:
    return cards

# Displaying the data.
print(data)


# Rather than encoding the normal bingo cards we can just encode whether they are marked or not. We can use the lookup table before 
# Just an idea, might be better, we'll see
#bingo_card = np.array([
# [1, 1, 1, 1, 1],  # Complete row (win)
#    [0, 1, 0, 1, 0],
#    [1, 0, 1, 0, 1],
#    [0, 1, 0, 1, 0],
#    [1, 0, 1, 0, 1]
# ])
