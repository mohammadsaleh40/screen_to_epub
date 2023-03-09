import pandas as pd
import numpy as np
import cv2 as cv
import time
import mss
import pytesseract
import tkinter as tk
from pytesseract import Output
import os
from functions import moshabehat , ezafe_df , img_to_df
dirname = os.path.dirname(__file__)
dirname
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

chaharchoob = {"top": 0, "left": 0, "width": 0, "height": 0}

def update_screenshot(top, left, width, height):
    global chaharchoob
    chaharchoob = {
        "top": top,
        "left": left,
        "width": width,
        "height": height
    }

def draw_rectangle(screenshot_array):
    global chaharchoob
    cv.rectangle(screenshot_array, (chaharchoob["left"], chaharchoob["top"]), (chaharchoob["left"] + chaharchoob["width"], chaharchoob["top"] + chaharchoob["height"]), (0, 255, 0), 2)
    cv.imshow("salam", screenshot_array)

def set_region():
    top = int(top_entry.get())
    left = int(left_entry.get())
    width = int(width_entry.get())
    height = int(height_entry.get())
    update_screenshot(top, left, width, height)
    root.destroy()

root = tk.Tk()
top_label = tk.Label(root, text="Top:")
top_label.grid(row=0, column=0)
text = tk.StringVar()
text.set("200")
top_entry = tk.Entry(root , textvariable = text)
top_entry.grid(row=0, column=1)
left_label = tk.Label(root, text="Left:")
left_label.grid(row=1, column=0)
text = tk.StringVar()
text.set("1000")
left_entry = tk.Entry(root , textvariable = text)
left_entry.grid(row=1, column=1)
width_label = tk.Label(root, text="Width:")
width_label.grid(row=2, column=0)
text = tk.StringVar()
text.set("850")
width_entry = tk.Entry(root , textvariable = text)
width_entry.grid(row=2, column=1)
height_label = tk.Label(root, text="Height:")
height_label.grid(row=3, column=0)
text = tk.StringVar()
text.set("840")
height_entry = tk.Entry(root , textvariable = text)
height_entry.grid(row=3, column=1)
set_button = tk.Button(root, text="Set Region", command=set_region)
set_button.grid(row=4, column=0, columnspan=2)
root.mainloop()
last_text = ""
matn = ""
last_screenshot_array = np.array([])
#chand_omin_ax = 0
with mss.mss() as sct:
    cv.namedWindow("salam")
    sct_img = sct.grab(sct.monitors[1])
    print(chaharchoob)    
    #chaharchoob = {"top": int(top_entry.get()), "left": int(left_entry.get()), "width": int(width_entry.get()), "height": int(height_entry.get())}
    sct_img = sct.grab(chaharchoob)
        
    screenshot_array = np.array(sct_img)
    screenshot_center = screenshot_array[chaharchoob["height"]*23//50:chaharchoob["height"]*28//50 , chaharchoob["width"]*25//50:chaharchoob["width"]*26//50]
    #print(screenshot_center)
    df = pd.DataFrame(columns=["line_num" , "matn" , "width", "sehat"])
    gray = cv.cvtColor(screenshot_array, cv.COLOR_BGR2GRAY)
    df = img_to_df(screenshot_array, df)
    img_data = pytesseract.image_to_data(gray, lang='fas+eng' , output_type=Output.DICT)
        
    while True:
        
        
        sct_img = sct.grab(chaharchoob)
        
        screenshot_array = np.array(sct_img)
        if not np.all(screenshot_center == screenshot_array[chaharchoob["height"]*23//50:chaharchoob["height"]*28//50 , chaharchoob["width"]*25//50:chaharchoob["width"]*26//50]):
            #matn = ""
            screenshot_center = screenshot_array[chaharchoob["height"]*23//50:chaharchoob["height"]*28//50 , chaharchoob["width"]*25//50:chaharchoob["width"]*26//50]
            df_t = pd.DataFrame(columns=["line_num" , "matn" , "width", "sehat"])
            gray = cv.cvtColor(screenshot_array, cv.COLOR_BGR2GRAY)
            df_t = img_to_df(screenshot_array, df_t)
            df = ezafe_df(df, df_t)
            print("*-*-*-*-*<<",len(df),">>*-*-*--*-*-*")
            img_data = pytesseract.image_to_data(gray, lang='fas+eng' , output_type=Output.DICT)
            #print(img_data)
        
            for index,text in enumerate(img_data['text']):
                if img_data["level"][index]==4:
                    x1= int(img_data['left'][index])
                    y1= int(img_data['top'][index])
                    x2 = x1 + int(img_data['width'][index])
                    y2 = y1 + int(img_data['height'][index])
                    cv.rectangle(gray, (x1, y1), (x2, y2), (85,70,60), 1)
                    
            
            #cv.imwrite("example_pictures/h_"+str(chand_omin_ax)+".jpg" , gray)
            #chand_omin_ax+=1
        cv.imshow("salam", gray)
        key = cv.waitKey(5)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
        
matn_chapter = ""
for i in range(len(df)):
    matn_chapter += df["matn"][i]
f = open("file.txt" , "w")
f.write(matn_chapter)
f.close()
