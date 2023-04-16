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
def update_img():
    global asli , pardazesh
    img = asli.copy()
    for i in range(0,len(ignore_list)//2,2):
        cv.rectangle(img, ignore_list[i], ignore_list[i+1], (255, 255, 255), -1)
    
    for i in range(0,len(tasvir_list)//2,2):
        cv.rectangle(img, tasvir_list[i], tasvir_list[i+1], (255, 255, 255), -1)
    pardazesh = img

# %%
ignore_list = []
tasvir_list = []
def mouse_click(event, x, y, flags, param):
    global ignore_list , tasvir_list
    # add
    if event == cv.EVENT_LBUTTONDOWN and param == 'i':
        ignore_list.append([int(x * (1/scale)) , int(y* (1/scale))])
    elif event == cv.EVENT_LBUTTONUP and param == 'i':
        ignore_list.append([int(x * (1/scale)) , int(y* (1/scale))])
    # remove
    if event == cv.EVENT_RBUTTONDOWN and param == 'i':
        ignore_list.pop()
    elif event == cv.EVENT_RBUTTONUP and param == 'i':
        ignore_list.pop()
    # add
    if event == cv.EVENT_LBUTTONDOWN and param == 't':
        tasvir_list.append([int(x * (1/scale)) , int(y* (1/scale))])
    elif event == cv.EVENT_LBUTTONUP and param == 't':
        tasvir_list.append([int(x * (1/scale)) , int(y* (1/scale))])
    # remove
    if event == cv.EVENT_RBUTTONDOWN and param == 't':
        tasvir_list.pop()
    elif event == cv.EVENT_RBUTTONUP and param == 't':
        tasvir_list.pop()
    
    
    if event == cv.EVENT_LBUTTONDOWN and param == 'space':
        update_img()
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
asli = np.array(images[0])
pardazesh = cv.cvtColor(asli , cv.COLOR_GRAY2BGR)
for i in range(len(img_data["level"])):
    if img_data["level"][i] == 5:
        index = i
        #print(img_data["text"][i])
        x1= int(img_data['left'][index])
        y1= int(img_data['top'][index])
        x2 = x1 + int(img_data['width'][index])
        y2 = y1 + int(img_data['height'][index])
        zarib_sehat = img_data["conf"][index]
        cv.rectangle(pardazesh ,  (x1, y1), (x2, y2), ((zarib_sehat*255)/100,(zarib_sehat*70)/100,(zarib_sehat*70)/100), 10)
t = ""
scale = 0.2
while True:
    
    namayesh= pardazesh.copy()
    
    cv.putText(img = namayesh, text = t , org= (40 , 100),
        fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3,
        color=(0, 255, 0),thickness=3)
        
    cv.imshow("salam", cv.resize(namayesh, (0,0),None , scale , scale))
    
    key = cv.waitKey(5)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('i'):
        t = "i"
        cv.setMouseCallback('salam', mouse_click , 'i')
    elif key == ord('t'):
        cv.setMouseCallback('salam', mouse_click , 't')
        t = "t"
    elif key == 32:
        t = ""
        cv.setMouseCallback('salam', mouse_click , 'space')
 # %%
# %%
img_data.head(20)
# %%
tasvir_list
# %%
ignore_list
# %%
