import cv2
import numpy as np
def carplate(file_name):
 img_original = cv2.imread(rf'C:\Users\Ariya Rayaneh\Desktop\{file_name}')
 carPlate = cv2.CascadeClassifier(r'C:\Users\Ariya Rayaneh\Desktop\haarcascade_russian_plate_number.xml')
 plateRect = carPlate.detectMultiScale(img_original,
                                 scaleFactor=1.3,
                                 minNeighbors=4,
                                 minSize=(30, 30),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

 for(x,y,w,h) in plateRect:
  cv2.rectangle(img_original,(x,y),(x+w,y+h),(0,255,0),5)
  print(x,y,w,h)
  break


 blurimg=cv2.blur(img_original[y:y+h,x:x+w],(40,40))
 img_original[y:y+h,x:x+w]=blurimg

 cv2.imshow('output',img_original)
 cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\{file_name}_out.jpg',img_original)
 cv2.waitKey()

carplate('car22.jpg')
