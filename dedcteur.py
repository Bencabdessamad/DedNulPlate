import cv2
import numpy as np

#load the cascade classifier for number plate detection
cascade = cv2.CascadeClassifier("number_plate_detection.xml")

#open the video stream

cap = cv2.VideoCapture(0)

while(True):
    #read a frame from the video stream
    ret, frame= cap.read()
    # convert the frqme to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_)
    #use gaussian blur to reduce noise
    gray=cv2.cvtColor(gray,(5,5),0)
    #detect number plates in the frame 
    plates = cascade.detectMultiScale(gray,1.1,5)
    #draw a rectangle around the detected number plates
    for (x,y,w,h) in plates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 2)
        #crop the number plate region 
        roi = gray[y:y+h,x:x+w]
        
        #use ocr to extract text from the number plate 
        text = pytesseract.image_to_string(roi,lang='eng',config='--psm 11')
        
        #draw the extracted text on the frame 
        cv2.putText(frame,text,(x,y-13))
        cv2.FONT_HERSHEY_SIMPLEX,(0.5,(0,255,0),2)
        #show the frame on the screen 
        cv2.imshow("Number plate detection ", frame)
        
        #exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0*FF == ord('q'):
            break
        #release the video stream and exit the window
        cap.ralease()
        cv2.destroyAllWindows()