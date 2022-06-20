import cv2
print("\nREAD AN IMAGE USING OPENCV")

filepath = "Dahyun.jpg"

input2 = int(input("\n [1]COLOR \n [2]GRAYSCALE \n [3]UNCHANGED \n CHOOSE DAHYUN'S STYLE: "))
if input2 == 1:
            image = cv2.imread(filepath, 1)
            cv2.imshow("Colored Dahyun", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
elif input2 == 2:
           image = cv2.imread(filepath, 0)
           cv2.imshow("Grayscaled Dahyun", image) 
           cv2.waitKey(0)
           cv2.destroyAllWindows()
else:
           image = cv2.imread(filepath, -1)
           cv2.imshow("Unchanged Dahyun", image)
           cv2.waitKey(0)
           cv2.destroyAllWindows()
