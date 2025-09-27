import cv2
import sys

def getPoint():
    x = int(input("width: "))
    y = int(input("height: "))
    return (x,y)

def getThickness():
    thickness = int(input("Thickness: "))
    return thickness

def getColor():
    print("Enter color")
    b = int(input("Blue: "))
    r = int(input("Red: "))
    g = int(input("Green: "))
    return (b,g,r)

def showImage(image):
    cv2.imshow("Image Viewer",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showDimensions(image):
    (h,w,c) = image.shape
    print("Dimensions of the image:")
    print(f"Height: {h}")
    print(f"Width: {w}")
    print(f"Color channel: {c}")
    
def askAndSave(image):
    file_name = input("Do you want to save image? If yes enter filename: ")
    if file_name:
        cv2.imwrite(file_name, image)
        print(f"File {file_name} saved succesfully!")

def draw_line(image):
    print("Enter point1 details")
    p1 = getPoint()
    print("Enter point2 details")
    p2 = getPoint()
    color = getColor()
    thickness = getThickness()
    new_image = cv2.line(image, p1, p2, color, thickness)
    showImage(new_image)
    askAndSave(new_image)
    
def draw_rectangle(image):
    print("Enter top left point details")
    p1 = getPoint()
    print("Enter bottom right point details")
    p2 = getPoint()
    color = getColor()
    thickness = getThickness()
    new_image = cv2.rectangle(image, p1, p2, color, thickness)
    showImage(new_image)
    askAndSave(new_image)

def draw_circle(image):
    print("Enter center point details")
    center = getPoint()
    radius = int(input("Enter radius: "))
    color = getColor()
    thickness = getThickness()
    new_image = cv2.circle(image, center, radius, color, thickness)
    showImage(new_image)
    askAndSave(new_image)

def put_text(image):
    text = input("Enter the text:")
    org = getPoint()
    color = getColor()
    thickness = getThickness()
    new_image = cv2.putText(image, text, org, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, color, thickness)
    showImage(new_image)
    askAndSave(new_image)


if __name__ == "__main__":
    try:
        file_location = input("Enter the image path: ")
        
        image = cv2.imread(file_location)
        if image is None:
            raise Exception(f"Failed to load image from path: {file_location}")
        print("Image loaded successfully!")
        
        showDimensions(image)
        while True:
            choice = input("Choice List:\n1. draw line.\n2. draw rectangle.\n3. draw circle.\n4. put text\n5. Exit\nEnter your choice: ")
            match(choice):
                case '1':
                    draw_line(image)
                case '2':
                    draw_rectangle(image)
                case '3':
                    draw_circle(image)
                case '4':
                    put_text(image)
                case '5':
                    sys.exit()
                case _:
                    continue


    except Exception as e:
        print(e)

    

