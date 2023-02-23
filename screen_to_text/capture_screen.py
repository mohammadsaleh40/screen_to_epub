import numpy as np
import cv2 as cv
import time
import mss
import pytesseract
import tkinter as tk

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
langs = ['fa', 'eng']
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
top_entry = tk.Entry(root)
top_entry.grid(row=0, column=1)
left_label = tk.Label(root, text="Left:")
left_label.grid(row=1, column=0)
left_entry = tk.Entry(root)
left_entry.grid(row=1, column=1)
width_label = tk.Label(root, text="Width:")
width_label.grid(row=2, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=2, column=1)
height_label = tk.Label(root, text="Height:")
height_label.grid(row=3, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1)
set_button = tk.Button(root, text="Set Region", command=set_region)
set_button.grid(row=4, column=0, columnspan=2)
root.mainloop()
last_text = ""
with mss.mss() as sct:
    cv.namedWindow("salam")
    sct_img = sct.grab(sct.monitors[1])
    print(chaharchoob)    
    #chaharchoob = {"top": int(top_entry.get()), "left": int(left_entry.get()), "width": int(width_entry.get()), "height": int(height_entry.get())}
    while True:
        
        
        sct_img = sct.grab(chaharchoob)
        
        screenshot_array = np.array(sct_img)
        gray = cv.cvtColor(screenshot_array, cv.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray , lang='fas+eng')

        cv.imshow("salam", gray)
        key = cv.waitKey(10)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
        if text != last_text:
            last_text = text
            print(last_text)