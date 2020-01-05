# Tesseract-OCR

Using Python and OCR(Optical Character Recognition) to convert text images into text files

## What is Optical Character Recognition:
OCR is a technology that is used to distinguish printed or handwritten text within digital image. The way it works is that it identifies the dark areas as characters that need to be recognized and eventually translated.

Important packages:

```bash
sudo easy_install pip
sudo pip3 install pillow pytesseract

//Install Homebrew to run the following command
brew install imagemagick
```

## Characters are recognized in one of two ways:
Pattern recognition- OCR programs are fed examples of text in various fonts and formats which are then used to compare, and recognize, characters in the scanned document.
        
Feature detection- OCR programs apply rules regarding the features of a specific letter or number to recognize characters in the scanned document. Features could include the number of angled lines, crossed lines or curves in a character for comparison. For example, the capital letter “A” may be stored as two diagonal lines that meet with a horizontal line 

## OCR is better than a traditional scanner:
OCR readers and scanner work similarly in a sence that they both scan documents. However, traditional scanner instead of reproducing it in physical form like a copy machine would, it creates an electronic image file and stores it on your computer, where you can open and manipulate it like any other image file. However, OCR makes it so the text is in editable format. With the help of OCR, you can read your files and turn them into editable format to modify them as you please
