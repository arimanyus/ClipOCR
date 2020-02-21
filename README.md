# ClipOCR
Turn your screenshot/clipboard image into a .txt text file with Tesseract-powered OCR tool.

*Note: I created this program as Windows-only for the moment being. However, it can be optimized for other platforms with the correct Tesseract OCR module downloaded. –[arimanyus](https://github.com/arimanyus)*

## Prerequisite
Python 3.5+

## Dependencies
- Tesseract binary
- PyTesseract

### Input
The program automatically grabs the image that the user has in clipboard.

## Installation
- Please download the Teserract Binaries [here](https://tesseract-ocr.github.io/tessdoc/Downloads), in accordance to your operating system.
- Install 'Pillow' module using pip: `pip install pillow`
- Install 'PyTesseract' module in your Python terminal via `pip install pytesseract`

## Usage
On running `main.py`, the program will grab the image that you have in your clipboard, save it as a PNG file titled 'defFile.png'. It'll then read its content, showcase in the console while also printing it as a .txt file named 'Output.txt'.

Tesseract recommends images above 300 dpi to function well. It's unlikely for your clipboard to encompass such images and therefore 100% accuracy is not guarenteed.

Windows 10 users can use Windows' inbuilt Snip & Sketch program (`Win + Shift + S)` to take screenshots and save them to clipboards. MacOS users can use the shortcut `Alt + Shift + 4` to do the same.
