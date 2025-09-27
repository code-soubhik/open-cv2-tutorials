import cv2

image_loc = input("Enter image location: ")

try:
    image = cv2.imread(image_loc)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    choice = input("Enter 1 to save and -1 to show: ")
    if(choice == "1"):
        file_name = input("Enter filename: ")
        success = cv2.imwrite(file_name, grey_image)
        if(success):
            print(f"file {file_name} saved successfully!")
        else:
            raise Exception("Failed to save file")    
    elif(choice == "-1"):
        cv2.imshow("Image Tab", grey_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        raise Exception("Wrong choice")
except Exception as e:
    print(str(e))