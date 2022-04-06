import cv2
cap=cv2.VideoCapture("Mark.mp4")
face_cascade=cv2.CascadeClassifier("faces.xml")

while (cap.isOpened()):
    check,frame = cap.read()
    if check == True:
        #แปลงภาพสี -> grayscale
        gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        face_detect=face_cascade.detectMultiScale(gray_img,1.3,5)
        #บอกพื้นที่ที่เจอใบหน้า
        for (x,y,w,h) in face_detect:
            #เซ็นเซอร์ใบหน้า
            frame[y:y+h,x:x+w]=cv2.blur(frame[y:y+h,x:x+w],(50,50))
            cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF==ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()