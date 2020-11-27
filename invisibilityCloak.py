import cv2
import numpy as np
import time


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

time.sleep(1)

for i in range(30):
    ret, background = cap.read()

while True:

    ret, img = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerBlue = np.array([169, 175, 75])
    upperBlue = np.array([185, 255, 255])

    mask1 = cv2.inRange(hsv, lowerBlue, upperBlue)

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=2)

    mask2 = cv2.bitwise_not(mask1)

    cloak = cv2.bitwise_and(background, background, mask=mask1)
    non_cloak = cv2.bitwise_and(img, img, mask=mask2)

    final = cv2.addWeighted(cloak, 1, non_cloak, 1, 0)

    cv2.imshow("INVISIBILITY CLOAK", final)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
