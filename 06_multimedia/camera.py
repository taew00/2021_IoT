import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame1 = cap.read()
    if not ret:
        break


    frame2 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    frame3 = cv2.Canny(frame1, 100, 150)

    cv2.imshow('frame1',frame1)
    cv2.imshow('frame2',frame2)
    cv2.imshow('frame3',frame3)

    if cv2.waitKey(10) == 27:
        break

cap.release()
out.release()
cv2.destoryAllWindows()