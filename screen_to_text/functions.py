import pandas as pd
import numpy as np
import cv2 as cv
import time
import mss
import pytesseract
import tkinter as tk
from pytesseract import Output
import os
def moshabehat(l1 , l2):
    if len(l1)<2:
        return 0
    r = 0
    l1 = l1.split(" ")
    l2 = l2.split(" ")
    for i in range(min(len(l1),len(l2))):
        if l1[i] == l2[i]:
            r+=1
    r = r/len(l1)
    return r

def img_to_df(img , df):
    line_num = 0
    matn = ""
    sehat = 0
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_data = pytesseract.image_to_data(gray, lang='fas+eng' , output_type=Output.DICT)
    lines ={}
    shorooa = -1
    for i in range(len(img_data["text"])):
        
        if img_data["level"][i] ==4 and line_num==1:
            shorooa = i
            break
        elif img_data["level"][i] ==4:
            line_num+=1
            width = img_data["width"][i]
            
            #print(line_num," " ,i)
            #page_num,block_num,par_num,line_num
        elif img_data["level"][i] ==5:
            matn += img_data["text"][i]+" "
            sehat+= img_data["conf"][i]
    if shorooa == -1:
        print("-*-*-*-")
        print(df)
        return df
    for i in range(shorooa ,len(img_data["text"])):
        if img_data["level"][i] ==4:
            df = df.append({"line_num":line_num , "matn":matn , "width":width , "sehat":sehat}, ignore_index=True )
            width = img_data["width"][i]
            line_num += 1# img_data["page_num"][i]*img_data["block_num"][i]*img_data["par_num"][i]*img_data["line_num"][i]
            matn = ""
            sehat = 0
        if img_data["level"][i] ==5:
            matn+=img_data["text"][i]+" "
            sehat+= img_data["conf"][i]
    return df

def ezafe_df(df_llines , df_llines_t):
    biroon = False
    for index_asli in range(len(df_llines)-1,0,-1):
        for index_t in range(len(df_llines_t)):
            if moshabehat(df_llines.iloc[index_asli]["matn"], df_llines_t.iloc[index_t]["matn"]) ==1:
                last_tupel = (index_asli , index_t)
                try:
                    if first_j!=0:
                        first_j-=1
                    else:
                        biroon = True
                        break
                except:
                    first_j = index_t
        if biroon:
            break
    # باید سعی کنم از concat استفاده کنم این جوری بهتره.
    try:
        df = df_llines.iloc[0:last_tupel[0]]
        for i in range(last_tupel[1],len(df_llines_t)):
            df = df.append({"line_num":df_llines_t["line_num"][i]+len(df)-last_tupel[1] , "matn":df_llines_t["matn"][i] , "width":df_llines_t["width"][i] , "sehat":df_llines_t["sehat"][i]}, ignore_index=True )
    except(UnboundLocalError):
        df = df_llines
        for i in range(len(df_llines_t)):
            df = df.append({"line_num":df_llines_t["line_num"][i]+len(df) , "matn":df_llines_t["matn"][i] , "width":df_llines_t["width"][i] , "sehat":df_llines_t["sehat"][i]}, ignore_index=True )
            
    return df
            