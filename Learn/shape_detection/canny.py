import cv2

img = cv2.imread("images/testing-image.jpeg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

_, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Image",img)
cv2.imshow("Edges",edges)
cv2.imshow("Threshhold",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()