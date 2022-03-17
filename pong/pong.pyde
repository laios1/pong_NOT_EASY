x = 300
y = 300
vx = 0
vy = 0
a = 0
b = 0
yc1 = 200
xc1 = 530


def setup() :
    size (600,600)

def draw() :
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

    
    circle (x,y,50)
    rect(xc1,yc1,50,200,7)
    textSize(20)
    text("your score = ", 100, 50)
    text(a, 230, 50)
    text("your best score = ", 300, 50)
    text(b, 475, 50)
    if keyPressed:
        if key == 'p':
            yc1 = yc1-16
            if x+ 25 >600 :
                textSize(32)
                text("GAME OVER", 220, 300)
                fill(255, 0, 0)
            else :
                x = x + vx
                if y-25 < 0:
                    vy = -vy
                    y = y + 2*vy
                elif y+ 25 > 600 :
                    vy = -vy
                    y = y + 2*vy
                elif x -25<0:
                    vx = -vx
                    x = x + 2*vx
                elif x > xc1-25 :
                    if yc1-25 <y< yc1+200 :
                        vx = (x - xc1)
                        vy = (y - (yc1+100))/4
                        a = a+1
                        x = x+2
                    else :
                        y = y+vy
                else :
                    y = y + vy 
        if key == "m":
            yc1 = yc1+16
            if x+ 25 >600 :
                textSize(32)
                text("GAME OVER", 220, 300)
                fill(255, 0, 0)
            else :
                x = x + vx
                if y-25 < 0:
                    vy = -vy
                    y = y + 2*vy
                elif y+ 25 > 600 :
                    vy = -vy
                    y = y + 2*vy
                elif x -25<0:
                    vx = -vx
                    x = x + 2*vx
                elif x > xc1-25 :
                    if yc1-25<y< yc1+200 :
                        vx = (x - xc1)
                        vy = (y - (yc1+100))/4
                        a = a+1
                        x = x+2
                    else :
                        y = y+vy
                else :
                    y = y + vy 
    else:
        if x+ 25 >600 :
            textSize(32)
            text("GAME OVER", 220, 300)
            fill(255, 0, 0)
        else :
            x = x + vx
            if y-25 < 0:
                vy = -vy
                y = y + 2*vy
            elif y+ 25 > 600 :
                vy = -vy
                y = y + 2*vy
            elif x -25<0:
                vx = -vx
                x = x + 2*vx
            elif x > xc1-25 :
                if yc1-25<y< yc1+200 :
                    vx = (x - xc1)
                    vy = (y - (yc1+100))/4
                    a = a+1
                    x = x + 2
                else :
                    y = y+vy
            else :
                y = y + vy 
                
                
    if b<=a :
        b = a 
    
    if keyPressed :
        if key == "k":
             x = 300
             y = 300
             a = 0
             background(0)
             fill(255,255,255)
             vx = 0
             vy = 0
        if key == ENTER :
            background(0)
            vx = random.randint(-10,10)
            vy = random.randint(-10,10)
             
