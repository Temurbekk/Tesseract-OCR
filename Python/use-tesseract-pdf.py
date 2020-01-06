""""
This code opens the pdf file containing text, recognizes characters. If possible, it converts the file 
into editable text and prints it to the console or it can output to a file.

This is simple but yet great way to converting pdf files into editable text.
OCR is capable of reading the editable text on the given pdf file.

All the packages:
    Python version 2.7+
    Python input/output library
    Python Image Library(Pillow/PIL forked)
    Pytesseract - OCR tool for Python
    Install both via terminal:
        $ sudo pip3 install pillow pytesseract
    Install Wand for Python to do image processing(similar to ImageMagick)
        $ pip install Wand
""""
#The following line imports the input/output library
import io
#Required to use Pillow to open an image
from PIL import Image
#Required to import pytesseract to convert the image text into string
import pytesserac
#wand is a ImageMagick binding for image processing
from wand.image import Image as wi

pdf = wi(filename = "sample2.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

images = []

#convert the pdf into a jpeg
for img in pdfImage.sequence:
	imgPage = wi(image = img)
	images.append(imgPage.make_blob('jpeg'))

recognized_text = []

#Recognize the text in images
for imgBlob in images:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)
#Print to console
print(recognized_text)
"""
You can also print separate pages of the pdf file in such way:
   print(recognized_text[0]) //This prints the first page of the pdf file
   print(recognized_text[1]) //This prints the second page of the pdf file 
"""