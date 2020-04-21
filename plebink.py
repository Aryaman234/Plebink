from p5 import * 
import random
import time



infectedX = 750
infectedY = 750
policeX = 50
policeY = 50
infectedTurn= True
policeTurn = False
height=800
width=800
infectedMove=False
policeMove=False
screen = 0
f=None
spaces = [0] * 65
BoxXp = 0
BoxYp = 0
BoxXi=0
BoxYi=0
BoXColour = 0
movePolice= 0
moveInfected=63
numberInfectedmove = 0
numberPolicemove = 0 
policePoints = 0
infectedPoints = 0


def setup():
    size(800,800)
    no_stroke()
    spaces[0] = 2
    spaces[63] = 1


def draw():
    global infectedX,infectedY,policeX, policeY,infectedTurn,policeTurn, height, width, infectedMove, policeMove, screen, f, spaces, BoxXp, BoxYp,movePolice, BoxXi, BoxYi, moveInfected, numberInfectedmove, numberPolicemove, policePoints, infectedPoints




    if(screen==0):
        background(255)
        fill(0)
        f = create_font("Arial.ttf", 30)
        text_font(f)
        text_align("CENTER")
        text("Welcome to Plebink:",(400,350))
        text("Arrow keys for blue player",(400,400))
        text("W A S D for red player",(400,450))
        text("Press any key to start",(400,500))
        if key_is_pressed:
            screen=1
    
    if(screen==1):  


        for x in range(0, 64):
            if(spaces[x] == 2):
                l=x
                p=x
                k=x
                j=x
                i=x
                o=x
                n=x
                BoxYp=100*x
                fill(255,128,0)
                rect((0,BoxYp),100,100)
                if(l>=8 and l<16):
                    l=l-8
                    BoxYp=100*l
                    fill(255,128,0)
                    rect((100,BoxYp),100,100)
                if(p>=16 and p<24):
                    p=p-16
                    BoxYp=100*p
                    fill(255,128,0)
                    rect((200,BoxYp),100,100)
                if(k>=24 and k<32):
                    k=k-24
                    BoxYp=100*k
                    fill(255,128,0)
                    rect((300,BoxYp),100,100)
                if(j>=32 and j<40):
                    j=j-32
                    BoxYp=100*j
                    fill(255,128,0)
                    rect((400,BoxYp),100,100)
                if(i>=40 and i<48):
                    i=i-40
                    BoxYp=100*i
                    fill(255,128,0)
                    rect((500,BoxYp),100,100)
                if(o>=48 and o<56):
                    o=o-48
                    BoxYp=100*o
                    fill(255,128,0)
                    rect((600,BoxYp),100,100)
                if(n>=56 and n<64):
                    n=n-56
                    BoxYp=100*n
                    fill(255,128,0)
                    rect((700,BoxYp),100,100)

        for w in range(0, 64):
                    if(spaces[w] == 1):
                        q=w
                        e=w
                        r=w
                        t=w
                        y=w
                        a=w
                        s=w
                        BoxYi=100*w
                        fill(0,0,124)
                        rect((0,BoxYi),100,100)
                        if(q>=8 and l<16):
                            q=q-8
                            BoxYi=100*q
                            fill(0,0,124)
                            rect((100,BoxYi),100,100)
                        if(e>=16 and e<24):
                            e=e-16
                            BoxYi=100*e
                            fill(0,0,124)
                            rect((200,BoxYi),100,100)
                        if(r>=24 and r<32):
                            r=r-24
                            BoxYi=100*r
                            fill(0,0,124)
                            rect((300,BoxYi),100,100)
                        if(t>=32 and t<40):
                            t=t-32
                            BoxYi=100*t
                            fill(0,0,124)
                            rect((400,BoxYi),100,100)
                        if(y>=40 and y<48):
                            y=y-40
                            BoxYi=100*y
                            fill(0,0,124)
                            rect((500,BoxYi),100,100)
                        if(a>=48 and a<56):
                            a=a-48
                            BoxYi=100*a
                            fill(0,0,124)
                            rect((600,BoxYi),100,100)
                        if(s>=56 and s<64):
                            s=s-56
                            BoxYi=100*s
                            fill(0,0,124)
                            rect((700,BoxYi),100,100)
        
        no_stroke()
        fill(0,0,124)
        rect((infectedX-50,infectedY-50),100,100)

        fill(255,128,0)
        rect((policeX-50,policeY-50),100,100)

        fill(255,0,0)
        ellipse((policeX,policeY),50,50)

        fill(0,0,255)
        ellipse((infectedX,infectedY),50,50)

        if(infectedTurn==True):
            if key_is_pressed:
                if key == "LEFT":
                    infectedX=infectedX-100
                    infectedMove=True
                    moveInfected=moveInfected-8
                    spaces[moveInfected]= 1
                    numberInfectedmove= numberInfectedmove + 1
                if key == "UP":
                    infectedY=infectedY-100
                    infectedMove=True
                    moveInfected=moveInfected-1
                    spaces[moveInfected]= 1
                    numberInfectedmove= numberInfectedmove + 1
                if key == "RIGHT":
                    infectedX=infectedX+100
                    infectedMove=True
                    moveInfected=moveInfected+8
                    spaces[moveInfected]= 1
                    numberInfectedmove= numberInfectedmove + 1
                if key == "DOWN":
                    infectedY=infectedY+100
                    infectedMove=True
                    moveInfected=moveInfected+1
                    spaces[moveInfected]= 1
                    numberInfectedmove= numberInfectedmove + 1


        else:
            infectedMove=False
            if key_is_pressed:
                if key == "LEFT":
                    infectedX=infectedX
                if key == "UP":
                    infectedY=infectedY
                if key == "RIGHT":
                    infectedX=infectedX
                if key == "DOWN":
                    infectedY=infectedY


        if(infectedMove==True):
            infectedTurn = False
            policeMove=False

        if(policeTurn==True):
            if key_is_pressed:
                if key == "a":
                    policeX=policeX-100   
                    policeMove=True
                    movePolice=movePolice-8
                    spaces[movePolice]= 2 
                    numberPolicemove = numberPolicemove +1

                if key == "w":
                    policeY=policeY-100
                    policeMove=True
                    movePolice=movePolice-1
                    spaces[movePolice]= 2  
                    numberPolicemove = numberPolicemove +1
          
                if key == "d":
                    policeX=policeX+100
                    policeMove=True 
                    movePolice=movePolice+8
                    spaces[movePolice]= 2                                         
                    numberPolicemove = numberPolicemove +1
                                 
                if key == "s":
                    policeY=policeY+100
                    policeMove=True
                    movePolice=movePolice+1
                    spaces[movePolice]= 2 
                    numberPolicemove = numberPolicemove +1
                    

        else:
            if key_is_pressed:
                if key == "a":
                    policeX=policeX
                if key == "w":
                    policeY=policeY
                if key == "d":
                    policeX=policeX
                if key == "s":
                    policeY=policeY



        if(numberInfectedmove > 32):
            if key_is_pressed:
                if key == "LEFT":
                    infectedX=infectedX
                if key == "UP":
                    infectedY=infectedY
                if key == "RIGHT":
                    infectedX=infectedX
                if key == "DOWN":
                    infectedY=infectedY
            for d in range(0,64):
                if(spaces[d] == 1):
                    infectedPoints=infectedPoints+1
                if(spaces[d] == 2):
                    policePoints=policePoints+1
            infectedPoints=infectedPoints-1 
            screen=3


            



        if(numberPolicemove > 32):
            if key_is_pressed:
                if key == "a":
                    policeX=policeX
                if key == "w":
                    policeY=policeY
                if key == "d":
                    policeX=policeX
                if key == "s":
                    policeY=policeY     


 



        if(policeMove==True):
            policeTurn=False
            infectedTurn=True


        if(infectedTurn==True):
            policeTurn=False 
        else:
            policeTurn=True
    

        if(policeTurn==True):
            infectedTurn=False 
        else:
            infectedTurn=True

        if(infectedX>800):
            infectedX=infectedX-100
            infectedMove=False

        if(infectedX<0):
            infectedX=infectedX+100
            infectedMove=False

        if(infectedY>800):
            infectedY=infectedY-100
            infectedMove=False

        if(infectedY<0):
            infectedY=infectedY+100
            infectedMove=False

        if(policeX>800):
            policeX=policeX-100
            policeMove=False

        if(policeX<0):
            policeX=policeX+100
            policeMove=False

        if(policeY>800):
            policeY=policeY-100
            policeMove=False

        if(policeY<0):
            policeY=policeY+100
            policeMove=False


        background(14)
        stroke_weight(1)
        stroke(255)
        no_fill()
        rect((1,1),height-1,(width/8)-1)
        rect((1,width/8),height-1,width/8)
        rect((1,(width/8)*2),height-1,width/8)
        rect((1,(width/8)*3),height-1,width/8)
        rect((1,(width/8)*4),height-1,width/8)
        rect((1,(width/8)*5),height-1,width/8)
        rect((1,((width/8)*6)),height-1,(width/8)-1)
        rect((1,((width/8)*7)-1),height-1,width/8)


        rect((1,1),(height/8)-1,width)
        rect((height/8,1),(height/8)-1,width)
        rect(((height/8)*2,1),(height/8)-1,width)
        rect(((height/8)*3,1),(height/8)-1,width)
        rect(((height/8)*4,1),(height/8)-1,width)
        rect(((height/8)*5,1),(height/8)-1,width)
        rect(((height/8)*6,1),(height/8)-1,width) 
        rect(((height/8)*7,1),(height/8)-1,width)

    
    if(screen==3):
        background(255)
        if(infectedPoints<policePoints):
            f = create_font("Arial.ttf", 30)
            text_font(f)
            text_align("CENTER")
            fill(0)
            text("Orange Wins!",(400,350))
        elif(infectedPoints>policePoints):
            f = create_font("Arial.ttf", 30)
            text_font(f)
            text_align("CENTER")
            fill(0)
            text("Blue Wins!",(400,350))
        elif(infectedPoints==policePoints):
            f = create_font("Arial.ttf", 30)
            text_font(f)
            text_align("CENTER")
            fill(0)
            text("Tie!",(400,350)) 

        f = create_font("Arial.ttf", 30)
        text_font(f)
        text_align("CENTER")
        fill(0)
        text("Blue: " + str(infectedPoints),(400,400))
        text("Orange: " + str(policePoints), (400,450))           


if __name__ == '__main__':
    run()

