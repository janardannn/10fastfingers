# ABOUT

The script automates typing in [play.typeracer.com](https://play.typeracer.com) using image recognition through pytesseract module.

## Installation

```bash
pip install -r requirements.txt
```
The script also uses the Tesseract-OCR binary, install it from [here](https://github.com/UB-Mannheim/tesseract/wiki) and add it to PATH as well.

## How to use

```python
python3 playtyperacer.py
```
This will prompt the Snipping Tool window. Use the Snipping tool to precisely capture the text and then save it in the Resources/ folder and name the file "Capture.png" (windows default).
Close the Snipping Tool window, the script will count down from 3 to 1, in the mean time click the text field in the browser window.

## Known Issues

The scripts isn't able to identify "" in text and completely ignores them(quotes).

Also, many a times it doesn't recognizes the first character in the text.
