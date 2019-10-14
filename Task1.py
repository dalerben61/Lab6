from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import click


backlight.set_all(255,0,130)
backlight.show()
lcd.clear()
lcd.show()
x = 0
y = 0


print("This program creates a simulation of an Etch a Sketch on the GFX Hat.")
print("Here are a few instructions on how to use the program.")
print("Use the arrow keys to draw lines on the GFX Hat.")
print("Press S to clear the screen.")
print("Press Q to exit.")
print("Press S now to erase the 'Etch a Sketch' message diplayed on the hat")


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

displayText()

while True:
    input = click.getchar()
    click.echo()

    if input == 's':
        lcd.clear()
        lcd.set_pixel(x,y,1)
        lcd.show()
    
    if input == 'q':
        break
    
    if input == '\x1b[A':
        y = y - 1
        if y < 0:
            y = 63
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif input == '\x1b[B':
        y = y + 1
        if y > 63:
            y = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif input == '\x1b[C':
        x = x + 1
        if x > 127:
            x = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif input == '\x1b[D':
        x = x - 1
        if x < 0:
            x = 127
        lcd.set_pixel(x,y,1)
        lcd.show()
    
print("Goodbye!")
backlight.set_all(0,0,0)
backlight.show()
lcd.clear()
lcd.show()