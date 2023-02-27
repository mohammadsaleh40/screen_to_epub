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
dirname = os.path.dirname(__file__)
dirname
# %%

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# %%
list_lines = []

df_llines = pd.DataFrame(columns=["line_num" , "matn" , "width"])
for j in range(
    #1
    #2
    #4,5
    #100
    ):
    line_num = 0
    df_llines_t = pd.DataFrame(columns=["line_num" , "matn" , "width"])
    matn = ""
    img = cv.imread(dirname+"/example_pictures/h_"+str(j)+".jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_data = pytesseract.image_to_data(gray, lang='fas+eng' , output_type=Output.DICT)
    lines ={}
    for i in range(len(img_data["text"])):
        
        if img_data["level"][i] ==4 and line_num==1:
            shorooa = i
            break
        elif img_data["level"][i] ==4:
            line_num+=1
            width = img_data["width"][i]
            
            print(line_num," " ,i)
            #page_num,block_num,par_num,line_num
        elif img_data["level"][i] ==5:
            matn += img_data["text"][i]+" "
        
    for i in range(shorooa ,len(img_data["text"])):
        if img_data["level"][i] ==4:
            df_llines_t = df_llines_t.append({"line_num":line_num , "matn":matn , "width":width}, ignore_index=True )
            width = img_data["width"][i]
            line_num += 1# img_data["page_num"][i]*img_data["block_num"][i]*img_data["par_num"][i]*img_data["line_num"][i]
            matn = ""
        if img_data["level"][i] ==5:
            matn+=img_data["text"][i]+" "

    #print(img_data)
    #cv.imshow("salam", img)
    #key = cv.waitKey(5)
    #if key == ord('q'):
    #    cv.destroyAllWindows()
    #    break

# %%

# %%
img_data.keys()
# %%
df_llines_t
# %%
gg = gray.copy()
for i in range(len(img_data["level"])):
    if img_data["level"][i] == 3:
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
def moshabehat(l1 , l2):
    r = 0
    l1 = l1.split(" ")
    l2 = l2.split(" ")
    for i in range(min(len(l1),len(l2))):
        if l1[i] == l2[i]:
            r+=1
    r = r/len(l1)
    return r
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
