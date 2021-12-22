import numpy as np
import cv2
import tensorflow as tf

text_dict={0:'defected',1:'good'}
rect_color_dict={0:(0,0,255),1:(0,255,0)}

model=tf.keras.models.load_model('autovai.h5')
i=0


video=cv2.VideoCapture(1)
address='https://192.168.43.1:8080/video'
video.open(address)
while True:
 ret, image = video.read()
 resized_img = cv2.resize(image, (250, 250))
 grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
 k=0
 kernel= cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
 denoise_img = cv2.fastNlMeansDenoising(grayscale_img)
 ret, timg = cv2.threshold(denoise_img, 145, 255, cv2.THRESH_BINARY_INV)
 closing = cv2.morphologyEx(timg, cv2.MORPH_CLOSE, kernel)
 cv2.imshow('N&B', timg)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

 imags = []
 imags.append(closing)
 imags = np.array(imags,dtype=np.float32)
 imags = np.reshape(imags, (imags.shape[0], 250, 250, 1))
 im,cnt,heirarchy = cv2.findContours(closing,cv2.RETR_TREE,
                                     cv2.CHAIN_APPROX_SIMPLE)

 for i in closing:
    for j in i:
        if j==0:
            k=k+1
 print(k)
 if k>=26000:
    imags = []
    imags.append(closing)
    imags = np.array(imags, dtype=np.float32)
    imags = np.reshape(imags, (imags.shape[0], 250, 250, 1))

    print(cnt)
    predictions = model.predict(imags)
    predictions = np.argmax(predictions)
    label = predictions
    prediction = (text_dict[1])

    print(prediction)
    cv2.putText(resized_img, text_dict[label], (100, 125),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                rect_color_dict[label], 2)

    cv2.imshow('Predictions', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 else:
     cv2.imshow('img', resized_img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

