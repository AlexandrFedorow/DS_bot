from PIL import Image

watermark= Image.open('img/FOX.png')
img = Image.open('img/MASK1.png')

img.paste(watermark, (1000, 1000),  watermark)
img.save("img/img.png")