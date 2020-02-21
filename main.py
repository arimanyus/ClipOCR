from PIL import Image, ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"PATH" #Comment this out if you've set Tesseract in your environment PATH already. Replace PATH with tesseract executable's. Ex: C:\Program Files (x86)\Tesseract-OCR\tesseract.exe

#im = Image.open("sample.png") #Uncomment this and comment lines 7 & 8 if you don't want to use the cliboard capturing feature.
imSaved = ImageGrab.grabclipboard()
imSaved.save('Image.png','PNG')

im = Image.open('Image.png')

text = pytesseract.image_to_string(im, lang='eng')

print(text)

textout = open("Output.txt", "w")
textout.write("%s" % text)
textout.close()
