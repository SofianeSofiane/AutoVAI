import tensorflow as tf
import numpy as np
import cv2
from tensorflow.compat.v1 import lite

#------------------------------------------------------------------------
kernel= cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

text_dict={0:'defected',1:'good'}
rect_color_dict={0:(0,0,255),1:(0,255,0)}


video=cv2.VideoCapture(1)
address='https://192.168.43.1:8080/video'
video.open(address)

resized_img = cv2.resize(img, (250, 250))
grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

#denoise_img = cv2.fastNlMeansDenoising(grayscale_img)
ret, timg = cv2.threshold(grayscale_img, 145, 255, cv2.THRESH_BINARY_INV)
#closing = cv2.morphologyEx(timg, cv2.MORPH_CLOSE, kernel)
imags = []
imags.append(timg)
imags = np.array(imags,dtype=np.float32)
imags = np.reshape(imags, (imags.shape[0], 250, 250, 1))
#----------------------------------------------------------------------------------------

label = 0

prediction = (text_dict[label])

print(prediction)
im,cnt,heirarchy = cv2.findContours(timg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   # Finding contours detection

for c in cnt:
   if len(c)>100:
       x=c

for i in x:
   print(i)
cv2.drawContours(resized_img, [x], 0, rect_color_dict[label], 2)
cv2.putText(resized_img, text_dict[label],(100,125), cv2.FONT_HERSHEY_SIMPLEX, 0.4, rect_color_dict[label], 2)

cv2.imshow('ll',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
