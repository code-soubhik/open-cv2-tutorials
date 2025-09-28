import cv2

def detectShape(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(grey, 254, 255, cv2.THRESH_BINARY_INV)


    con, hei = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contours in con:
        approx = cv2.approxPolyDP(contours, 0.01 * cv2.arcLength(contours, True), True)

        corners = len(approx)

        if corners == 3:
            shape_name = "Triangle"
        elif corners == 4:
            shape_name = "Rectangle"
        elif corners > 5:
            shape_name = "circle"
        else:
            shape_name = "unknown"
        
        cv2.drawContours(img, con, -1, (0,255,0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10
        cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 2)
        
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run():
    img1 = cv2.imread("images/shape/square.png")
    img2 = cv2.imread("images/shape/circle.png")
    img3= cv2.imread("images/shape/triangle.png")
    detectShape(img1)
    detectShape(img2)
    detectShape(img3)


if __name__ == "__main__":
    run()