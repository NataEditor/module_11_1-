from PIL import Image, ImageDraw, ImageFont
import sys
try:
    tatras = Image.open('DSC_0524.jpg')
except:
    print('Не удается загрузить изображение')
    sys.exit(1)

idraw = ImageDraw.Draw(tatras)
text = 'Осень пришла - 1 альбом'

font = ImageFont.truetype('arial.ttf', size=40)

idraw.text((40, 40), text, font=font)

tatras.save('DSC_0524_1.png')

image = Image.open('DSC_0524_1.png')
cropped = image.crop((177, 882, 1179, 1707))
cropped.save(r'C:\Users\nata_\PycharmProjects\11_2\cropped_DSC_0524_1.png')