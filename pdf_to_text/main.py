# %%
from pdf2image import convert_from_path
import os
import cv2 as cv
import numpy as np
import pytesseract
from pytesseract import Output
dirname = os.path.dirname(__file__)
dirname
# %%
books_path = dirname[:-11]+"books/"
book_name = "02024226sanjabbook.ir.pdf"
# %%
images = convert_from_path(books_path+book_name , dpi = 500  , first_page=20 , last_page= 24)
for index , img in enumerate(images):
    images[index] = cv.cvtColor(np.array(img) , cv.COLOR_BGR2GRAY)
# %%
img_data = pytesseract.image_to_data(images[0], lang='fas+eng' , output_type=Output.DATAFRAME)
img_data
# %%
gg = cv.cvtColor(np.array(images[0]) , cv.COLOR_GRAY2BGR)
for i in range(len(img_data["level"])):
    if img_data["level"][i] == 5:
        index = i
        #print(img_data["text"][i])
        x1= int(img_data['left'][index])
        y1= int(img_data['top'][index])
        x2 = x1 + int(img_data['width'][index])
        y2 = y1 + int(img_data['height'][index])
        zarib_sehat = img_data["conf"][index]
        cv.rectangle(gg ,  (x1, y1), (x2, y2), ((zarib_sehat*255)/100,(zarib_sehat*70)/100,(zarib_sehat*70)/100), 10)
        """
        if img_data["conf"][i] > 80:
            cv.rectangle(gg ,  (x1, y1), (x2, y2), (127,170,60), 2)
        elif img_data["conf"][i] > 50:
            cv.rectangle(gg ,  (x1, y1), (x2, y2), (224, 0 , 0), 2)
        elif img_data["conf"][i] > 20:
            cv.rectangle(gg ,  (x1, y1), (x2, y2), (0, 0 , 224), 2)
        else:
            cv.rectangle(gg ,  (x1, y1), (x2, y2), (0, 225 , 0), 2)
        """


while True:
    cv.imshow("salam", cv.resize(gg , (0,0),None , 0.2 , 0.2))
    key = cv.waitKey(5)
    if key == ord('q'):
        cv.destroyAllWindows()
        break

# %%
# %%
img_data.head(20)
# %%
