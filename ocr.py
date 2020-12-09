import pytesseract
import cv2
# pytesseract.pytesseract.tesseract_cmd="/usr/local/lib/python3.6/dist-packages/pytesseract/__init__.py"
# reading the image
image=cv2.imread("test.png")
# converting it to the grey
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# threshold
ret,threshold=cv2.threshold(gray,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
# getting the structure of the image
structure=cv2.getStructuringElement(cv2.MORPH_RECT,(18,18))
# dilating the image
dilate=cv2.dilate(threshold,structure,iterations=1)
# finding the points to found the rectangle
countour,h=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
file=open("Text.txt","w+")
file.write("")
file.close()
image_2=image.copy()
count=1
# extracting the text with the help of the pytessaract
for i in countour[::-1]:
    count=count+1
    # founding the rectangle
    x,y,w,h=cv2.boundingRect(i)
    # cropping that part
    block_crop=image_2[y:y+h,x:x+w]
    # extracting the text
    print(pytesseract.image_to_string(block_crop))
# cv2.imshow("Gray",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()