import cv2
import numpy as np
cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, current = cap.read()
    if ret:
        hsv_frame = cv2.cvtColor(current,cv2.COLOR_BGR2HSV)
        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame,l_red,u_red)
