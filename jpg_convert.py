from PIL import Image
import config
''' тут происходит конвертация в jpg '''
def convert():
    im = Image.open(config.PNAME)
    bg = Image.new("RGB", im.size, (255, 255,255))
    bg.paste(im, im)
    bg.save("img/color.jpg")
    config.PNAME = "img/color.jpg"