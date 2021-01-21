import cv2
from PIL import Image

image_path = "img/r.jpg"
im = Image.open('img/r.jpg')
watermark = Image.open('img/ch.png')
watermark = watermark.resize((100, 100), Image.ANTIALIAS)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)

faces_detected = "Лиц обнаружено: " + format(len(faces))
print(faces_detected)
# Рисуем квадраты вокруг лиц

for (x, y, w, h) in faces:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
    watermark = watermark.resize((w, h), Image.ANTIALIAS)
    im.paste(watermark, (x, y), watermark)

im.show()

