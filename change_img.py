from PIL import Image, ImageDraw
import cv2


"""Тут происходят все изменения над пикчами"""
def chenge1(name):               #для мелких фоток.
    image = Image.open(name)     #Открываем изображение.
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0]        #Определяем ширину. px.
    height = image.size[1]       #Определяем высоту.
    pix = image.load()           #Выгружаем значения пикселей.

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            nc = (a + b + c) / 3
            nc = int(nc)

            a, b, c = nc, nc, nc

            draw.point((i, j), (a, b, c))
    image.save(name, "JPEG")
    del draw

def ov(path):
    watermark = Image.open('img/FOX.png')
    img = Image.open('img/MASK1.png')

    img.paste(watermark, (1000, 1000), watermark)
    img.save("img/img.png")

def overlay_photo(name):
    image_path = name
    im = Image.open(name)
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
        #cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        watermark = watermark.resize((w, h), Image.ANTIALIAS)
        im.paste(watermark, (x, y), watermark)
    im.save(name, 'JPEG')