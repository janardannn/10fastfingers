from PIL import ImageGrab, Image
from datetime import datetime
import pyautogui as pyg
import pytesseract
import os
import time
import sys

def take_ss():
    
    ss = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    
    # x1,y1,x2,y2 are the cordinates of the white text box
    
    return ss

def get_text():
    ''' Getting text from the image.
        Now the thing is that there are \n 
        in the text which we don't want and 
        a weird character in the end of the 
        text, so we will do some string 
        manipulation as well.
    '''
    #os.system('SnippingTool.exe')
    im = take_ss()
    text = pytesseract.image_to_string(im)
    text = text[:-2]
    text = " ".join(text.split("\n"))
    
    
    ''' finally return the text '''
    return (text + " ")

def start_typing(text):
    ''' now we will use pyautogui
        module to type the text obtained
        from the image
    '''
    ''' interval is necessary even if 
        it is as low as 0.01, otherwise 
        it will be too fast for the website
        to consider as valid input
    '''

    pyg.write(text,interval=0.0545)
    

def time_to_quit(end):
    
    now = datetime.now()
    
    if now >= end:
        return 1     

def main():
    
    start = datetime.now()
    
    if start.minute == 60:
        end = start.replace(hour=start.hour+1)
    else:
        end = start.replace(minute=start.minute+1)
        
    k = input("Start? y/n: ").strip()
    time.sleep(2.5)
    if k.lower()=='y':
        
        while True:
            text = get_text()
            start_typing(text)
            res = time_to_quit(end)
            if res == 1:
                break
    sys.exit()


main()