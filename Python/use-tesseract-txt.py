""""
This code opens an image containing text, recognizes characters. If possible, it converts the image
text into written text and prints it to the console.

This is simple but yet great way to converting image into text.
OCR is capable of reading the text on the given image.

All the packages:
    Python version 2.7+
    Python Image Library(Pillow/PIL forked)
    Pytesseract - OCR tool for Python
    Install via terminal:
        $ sudo pip3 install pillow pytesseract
""""
#Required to use Pillow to open an image
from PIL import Image
#Required to import pytesseract to convert the image text into string
import pytesseract

#Following line opens the image called 'text.png'
image = Image.open("text.png")

#The following line converts the image into text in english language
text = pytesseract.image_to_string(image, lang = 'eng')

#Following line prints the output to the console
print(text)
#printed text read "HAPPY NEW YEAR"


