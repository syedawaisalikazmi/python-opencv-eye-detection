#eye detect using opencv live webcam
import cv2
#haar cascade classifier ka use karain ge eye detection ke liye
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)
# ya xml file hai jisme eye detection ke liye trained data hota hai
#live webcam se video capture karain ge
camera_detect = cv2.VideoCapture(0)
if not camera_detect.isOpened():
    print("Camera not found")
    exit()
while True:
    #video frame read karain ge
    camera_status, frame = camera_detect.read()
    #agar frame read ho gaya to eye detection karain ge
    if camera_status:
        #grayscale image banain ge eye detection ke liye
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #eye detection karain ge
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        #eye detection ke baad rectangle draw karain ge detected eyes ke around
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)#(ya 0 kya aur 255 ,0) ya color code hai jo rectangle ka color define karta hai, yahan par green color use kiya gaya hai
        #video frame display karain ge
        cv2.imshow('Eye Detection', frame)
    #agar user 'q' press kare to loop break karain ge
    if cv2.waitKey(1) == ord('q'):
        break

#camera release karain ge
camera_detect.release()
#all windows close karain ge
cv2.destroyAllWindows()
print("Eye detection stopped.")
