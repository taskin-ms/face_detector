import cv2
path = input("Ekhane ekta file url dao: ")
faceCascade = cv2.CascadeClassifier("C:/opencv/haarcascade_frontalface_default.xml")
img = cv2.imread(path)

scale_percent = 50


width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
faces = faceCascade.detectMultiScale(img, 1.1, 4)

# coverting to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating bounding box
text = input("Ekta shundor label dao toh dekhi: ")
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
    cv2.putText(img,text,(x+5, y+10) , cv2.FONT_HERSHEY_COMPLEX_SMALL,1,
    (0,0,0),2 )

cv2.imshow("Result", img)
cv2.waitKey(0)
