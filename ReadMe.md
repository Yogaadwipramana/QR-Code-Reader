# How it's works
1. First import the library that we need
````
import cv2	
import pyzbar.pyzbar as pyzbar
````
2. Connect the webcam to the program 
````
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv2.imshow('QR Code', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
````
3. Read The QR Code
````
decode_QR = pyzbar.decode(frame)
````
4. Make a loop
````
for barcode in decode_QR:
````
5. Draw a rectangle in QR Code
`````
(x, y, w, h) = barcode.rect
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),2)
`````
6. Put the text in the frame
``````
cv2.putText(frame, str(barcode.data), (100, 100), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 0), 3)
``````

# Demo

Clik the picture to see the Video
[![Watch the video](https://img.youtube.com/vi/dm1jecRQhO0/maxresdefault.jpg)](https://youtu.be/dm1jecRQhO0)
