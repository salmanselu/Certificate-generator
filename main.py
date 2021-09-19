from PIL import Image, ImageDraw, ImageFont
import pandas as pd

cx = 843
cy = 577
df = pd.read_csv('list.csv')
font = ImageFont.truetype('italianno.ttf',140)
fill = (207,255,229) 
for index,j in df.iterrows():
    image = Image.open('template.png')
    canvas = ImageDraw.Draw(image)
    name = j['name']
    email = j['email']
    w, h = font.getsize(name)
    canvas.text(xy = ( cx - w/2, cy - h/2), text=f'{name}', fill=fill, font=font)
    image.save(f'generated-certificates/{email}.png')