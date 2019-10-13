from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw

backlight.set_all(255,0,255)
backlight.show()

def displayText():
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    text = "Etch a Sketch"
    w, h = font.getsize(text)
    x = (width - w) // 2
    y = (height - h) // 2
    draw.text((x,y), text, 1, font)
    for x in range(128):
        for y in range(64):
            pixel = image.getpixel((x, y))
            lcd.set_pixel(x, y, pixel)
    lcd.show() 

print("Does it work?")
displayText()