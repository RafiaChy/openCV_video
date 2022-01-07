import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    cv2.imshow('Frame Window', gray_frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
