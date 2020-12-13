from PIL import Image, ImageDraw

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