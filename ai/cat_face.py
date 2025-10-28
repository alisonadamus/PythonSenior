import cv2

cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
img = cv2.imread("cat.webp") # ВАШЕ ЗОБРАЖЕННЯ
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x, y, w, h) in cats:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Cat Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
