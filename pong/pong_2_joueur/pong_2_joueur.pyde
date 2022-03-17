
x = 500
y = 300
vx = 0
vy = 0
a = 0
b = 0
yc1 = 200
xc1 = 950
yc2 = 200
xc2 = 20

    
def setup():
    size (1000,600)

def draw () :
    import random
    background(0)
    global x
    global y
    global vx
    global vy
    global yc1
    global xc1
    global a
    global b
    global yc2
    global xc2
    textSize(32)
    text(b, 220, 100)
    textSize(32)
    text(a, 800, 100)
    circle (x,y,25)
    rect(xc1,yc1,25,100,7)
    rect(xc2,yc2,25,100,7)
    rect(499,0,2,600)
    if x-25 <= 0:
        fill(255,0,0)
        if keyPressed:
            if key == "g":
                a = a+1
                x = 500
                y = 300
                vx = 0
                vy = 0
                yc1 = 250
                yc2 = 250
                fill(255,255,255)
    elif x+ 25 >= 1000 :
        fill(255,0,0)
        if keyPressed:
            if key == "g":
                b=b+1
                x = 500
                y = 300
                vx = 0
                vy = 0
                yc1 = 250
                yc2 = 250
                fill(255,255,255)
    else:
        rebond()
        commandC()
    if keyPressed:
        if key == "t" :
            background(0)
            vx =  random.randint(-10,10)
            vy =  random.randint(-10,10)

def rebond ():
    global x
    global y
    global b
    global a
    global vx
    global vy
    global xc1
    global yc1
        
    
    if y-25 < 0:
        vy = -vy
        y = y + 2*vy
    elif y+ 25 > 600 :
        vy = -vy
        y = y + 2*vy
    elif x < xc2 + 25 and yc2-25<y< yc2+100:
        vx = (x - xc2)/3
        vy = (y - (yc2+50))/6
        x = x + 2
    elif x > xc1-25 and yc1-25<y< yc1+100 :
        vx = (x - xc1)/3
        vy = (y - (yc1+50))/6
        x = x - 2
    else :
            y = y + vy 
            x = x + vx
        
        
def commandC():
    global yc2
    global yc1
    if x < 500:    
        if keyPressed:
            if key == "z":
                yc2 = yc2 - 8
            if key == "s":
                yc2 = yc2 + 8
    elif x > 500:
        if keyPressed:
            if key == "p":
                yc1 = yc1 - 8
            if key == "m":
                yc1 = yc1 + 8
