###################################################################################
# Date Created: 2024-12-18
# Date of Last Edit: 2024-12-19
###################################################################################
import cv2
import easyocr
from pathlib import Path

# The image path of where our test image is. 
sourceDir = Path('C:/bingoImages/')
files = sourceDir.iterdir()

# Making our reader for the image.
reader = easyocr.Reader(['en'])

# Will hold all the text in this list.
data = []

for file in files:
    # Preparing image input and grayscaling it for easier reading.
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecting text in the image.
    textData = reader.readtext(gray_image)
    # Looping through the data to put the text in the data array.
    for (boundingBox, text, confidence) in textData:
        data.append(text)

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
