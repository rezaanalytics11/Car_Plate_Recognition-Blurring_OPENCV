import cv2

import imutils
from imutils import contours
from imutils.perspective import four_point_transform

image_original=cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\soduku.png")

image_original=cv2.resize(image_original,(0,0),fx=2,fy=2)
image=image_original.copy()
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blurred=cv2.GaussianBlur(image,(7,7),3)

treshold=cv2.adaptiveThreshold(image_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

treshold=cv2.bitwise_not(treshold)

countours=cv2.findContours(treshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
countours=countours[0]

countours=sorted(countours,key=cv2.contourArea)
countours=reversed(countours)

soduku_counter=None

for countour in countours:
    epsilon=0.02*cv2.arcLength(countour,True)
    approx=cv2.approxPolyDP(countour,epsilon,True)
    if len(approx)==4:
        soduku_counter=approx
        x,y,w,h = cv2.boundingRect(countour)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        for i in approx:
            cv2.circle(image,(i[0][0], i[0][1]),2,(0,0,255), thickness=4)
        warped = four_point_transform(image, approx.reshape(4,2))

result=cv2.drawContours(image_original,[soduku_counter],-1,(0,255,0),10)

cv2.imshow('out',warped)
cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\picture_soduku_warped.png',warped)
cv2.waitKey()