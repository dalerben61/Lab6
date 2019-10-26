from gfxhat import lcd

lcd.clear()
lcd.show()

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

def displayObject(obj,x,y):
    lcd.clear()
    initialPositionx = x
    initialPositiony = y
    for i in obj:
        for j in i:
            if j == 1:
                lcd.set_pixel(initialPositionx, initialPositiony, 1)
                lcd.show()
            initialPositionx += 1
            if initialPositionx > 127:
                initialPositionx = 0
        initialPositiony+=1
        if initialPositiony > 63:
            initialPositiony = 0
        initialPositionx = x
            


choice = int(input("Which of the two objects do you want to display? (1 or 2)"))
x = int(input("Choose a starting value for x:"))
y = int(input("Choose a starting value for y:"))

if choice == 1:
    displayObject(f1,x,y)
elif choice == 2:
    displayObject(pm,x,y)

