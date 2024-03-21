import cv2
import numpy as np

def highlight_defects(image_path):
    img = cv2.imread(image_path) #get image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to greyscale 

    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)# on grey scale we find while spots

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# contour white spots

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Highlighted Defects', img)#displaying highlights
    cv2.waitKey(0)
    cv2.destroyAllWindows()

highlight_defects('Base Image.png')
highlight_defects('Small Defect.png')
highlight_defects('Large Defect.png')
