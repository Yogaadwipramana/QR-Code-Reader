import cv2
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)

while True :
    _, frame = cap.read()
    decode_QR = pyzbar.decode(frame)
    for qrcode in decode_QR:
        (x,y,w,h) = qrcode.rect
        cv2.rectangle(frame, (x,y),(x + w, y +w),(0,0,255), 2)
        cv2.putText(frame, str(qrcode.data), (100, 100), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0), 3)
    cv2.imshow("QR Code Scanner",frame)
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break 

cap.release()
cv2.destroyAllWindows()