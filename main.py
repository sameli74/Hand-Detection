import cv2 as cv
import time

cvNet = cv.dnn.readNetFromTensorflow('./model/frozen_inference_graph.pb', './model/graph.pbtxt')


img = cv.imread('./examples/example2.jpg')


rows = img.shape[0]
cols = img.shape[1]
cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
start = time.time()
cvOut = cvNet.forward()

end = time.time()
print(end-start)
for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv.imshow('img', img)
cv.waitKey()
