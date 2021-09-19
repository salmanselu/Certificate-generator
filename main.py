from PIL import Image, ImageDraw, ImageFont
import pandas as pd
cx = 843
cy = 577
df = pd.read_csv('list.csv')
font = ImageFont.truetype('italianno.ttf',140)
fill = (207,255,229) 
for j in df.iterrows():
    image = Image.open('template.png')
    canvas = ImageDraw.Draw(image)

    person = j['name']
    if person.isupper(): # if the person has entered their name
        continue         # in full uppercase, we skip their 
                         # name to manually process it later.

    email = j['email']
    w, h = font.getsize(person)
    canvas.text(xy = ( cx - w/2, cy - h/2), text=f'{person}', fill=fill, font=font)
    image.save(f'generated-certificates/{email}.png')