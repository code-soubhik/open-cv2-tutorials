import cv2

img = cv2.imread("images/testing-image.jpeg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(grey, 220, 255, cv2.THRESH_BINARY_INV)

#Find contours
c,h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, c, -1, (0,255,0), 2)

cv2.imshow("Image", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()