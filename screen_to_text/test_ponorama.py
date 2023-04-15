import cv2 as cv
import os
cv.ocl.setUseOpenCL(False)
dirname = os.path.dirname(__file__)
images_path = dirname+"/example_pictures/"
images = []
for i in range(23 , 26):
    img = cv.imread(images_path+str(i)+".png")
    img = cv.resize(img , (0,0),None , 0.2 , 0.2)
    images.append(img)
print(len(images))
sticher = cv.Stitcher.create()
print("درسته؟")
(s , result) = sticher.stitch(images)
print("درسته؟")

if s == cv.STITCHER_OK:
    print("اوضاع خوبه")
    cv.imshow("natije" , result)
    cv.waitKey(0)
cv.imwrite( "Panorama.jpg" , result )