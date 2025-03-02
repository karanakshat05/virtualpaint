import cv2
import numpy as np
framewidth = 640
frameheight = 480
cap= cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)



cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)


def empty(a):
    pass


cv2.createTrackbar("Hue min", "Trackbars", 90, 179,empty)
cv2.createTrackbar("Hue max", "Trackbars", 179, 179,empty)
cv2.createTrackbar("Sat min", "Trackbars", 140kk, 255,empty)
cv2.createTrackbar("Sat max", "Trackbars", 255, 255,empty)
cv2.createTrackbar("Val min", "Trackbars", 80, 255,empty)
cv2.createTrackbar("Val max", "Trackbars", 255, 255,empty)

while True:
    success, img = cap.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower= np.array([h_min, s_min,v_min])
    upper= np.array([h_max, s_max, v_max])
    mask= cv2.inRange(imghsv, lower, upper)
    imgresult = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("webcam",img)
    cv2.imshow("mask" , mask)
    cv2.waitKey(1)