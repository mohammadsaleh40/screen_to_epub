# %%
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
# %%

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# %%

# %%
df_llines = pd.DataFrame(columns=["line_num" , "matn" , "width", "sehat"])
img = cv.imread(dirname+"/example_pictures/h_0.jpg")
df_llines = img_to_df(img, df_llines)
df_llines
# %%
for j in range(1,
    #1
    #2
    #4,5
    20
    #100
    ):
    df_llines_t = pd.DataFrame(columns=["line_num" , "matn" , "width", "sehat"])
    img = cv.imread(dirname+"/example_pictures/h_"+str(j)+".jpg")
    
    
    df_llines_t = img_to_df(img, df_llines_t)
    df_llines = ezafe_df(df_llines , df_llines_t)
    #print(img_data)
    #cv.imshow("salam", img)
    #key = cv.waitKey(5)
    #if key == ord('q'):
    #    cv.destroyAllWindows()
    #    break

# %%
df_llines
# %%
matn_chapter = ""
for i in range(len(df_llines)):
    matn_chapter += df_llines["matn"][i]
f = open("file.txt" , "w")
f.write(matn_chapter)
f.close()
# %%
df_llines.to_csv("data_0_20.csv")

# %%
#img_data.keys()
# %%
df_llines_t

# %%
df_llines
# %%
gg = gray.copy()
for i in range(len(img_data["level"])):
    if img_data["level"][i] == 4:
        index = i
        #print(img_data["text"][i])
        x1= int(img_data['left'][index])
        y1= int(img_data['top'][index])
        x2 = x1 + int(img_data['width'][index])
        y2 = y1 + int(img_data['height'][index])
        cv.rectangle(gg ,  (x1, y1), (x2, y2), (85,70,60), 2)
while True:
    cv.imshow("salam", gg)
    key = cv.waitKey(5)
    if key == ord('q'):
        cv.destroyAllWindows()
        break

# %%
df = pd.DataFrame(img_data)
df.to_csv("data4.csv")

# %%
lines ={}
for i in range(len(img_data["text"])):
    
    if img_data["level"][i] ==5:
        if img_data["line_num"][i] not in lines:
            lines[img_data["line_num"][i]] = img_data["text"][i]+" "
        else:
            lines[img_data["line_num"][i]] += img_data["text"][i]+" "
lines

# %%
n=9
for i in range(1,1+len(list_lines[n])):
    for j in range(1,1+len(list_lines[n+1])):
        
        print(moshabehat(list_lines[n][i], list_lines[n+1][j] ), end="|")
    print()
# %%
list_lines[16]
# %%
lines
# %%
len(list_lines[16])
# %%
img_data
# %%
print(pytesseract.image_to_data(gray, lang='fas+eng' ))
# %%
