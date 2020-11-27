import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("test")         # creates empty window for trackbars

cv2.createTrackbar("l_h", "test", 98, 255, nothing)   # creates trackbars
cv2.createTrackbar("l_s", "test", 185, 255, nothing)
cv2.createTrackbar("l_v", "test", 67, 255, nothing)

cv2.createTrackbar("u_h", "test", 120, 255, nothing)
cv2.createTrackbar("u_s", "test", 255, 255, nothing)
cv2.createTrackbar("u_v", "test", 206, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   # converts BGR feed to HSV

    lH = cv2.getTrackbarPos("l_h", "test")     # gets trackbar position
    lS = cv2.getTrackbarPos("l_s", "test")
    lV = cv2.getTrackbarPos("l_v", "test")

    uH = cv2.getTrackbarPos("u_h", "test")
    uS = cv2.getTrackbarPos("u_s", "test")
    uV = cv2.getTrackbarPos("u_v", "test")

    lowerBlue = np.array([lH, lS, lV])   # sets the hsv value derived from trackbar
    upperBlue = np.array([uH, uS, uV])

    mask = cv2.inRange(hsv, lowerBlue, upperBlue)  # creates mask for cloak

    res = cv2.bitwise_and(frame, frame, mask=mask) 

    cv2.imshow("final", res)
    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
