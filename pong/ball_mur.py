def ball mur:
    if x-25 < 0:
        vx = -vx
        x = x + 2*vx
    elif x+ 25 >600 :
        vx = -vx
        x = x + 2*vx
    else :
        x = x + vx
        
    
    if y-25 < 0:
        vy = -vy
        y = y + 2*vy
    elif y+ 25 > 600 :
        vy = -vy
        y = y + 2*vy
    else :
        y = y + vy
