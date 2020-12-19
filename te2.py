from PIL import Image

im = Image.open('img/teimg.jpg')
watermark = Image.open('img/sm.png')

watermark = watermark.resize((100, 100), Image.ANTIALIAS)
# Вычисляем расположение watermark
position = (im.width - watermark.width,
             im.height - watermark.height)

im.paste(watermark, position, watermark)

im.show()