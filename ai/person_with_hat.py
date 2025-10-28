import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

image_path = "person.png" # ВАШЕ ЗОБРАЖЕННЯ
hat_path = "cylinder_hat.png"
img_cv = cv2.imread(image_path)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
img = Image.open(image_path).convert("RGBA")
hat = Image.open(hat_path).convert("RGBA")

for (x, y, w, h) in faces:
    hat_width = w
    aspect_ratio = hat.width / hat.height
    hat_height = int(hat_width / aspect_ratio)
    hat_resized = hat.resize((hat_width, hat_height))
    hat_y = y - hat_height + int(h / 10)
    if hat_y < 0:
        hat_y = 0
    img.paste(hat_resized, (x, hat_y), hat_resized)

img.save("person_with_hat.png")
result = cv2.imread("person_with_hat.png")
cv2.imshow("Person with Hat", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
