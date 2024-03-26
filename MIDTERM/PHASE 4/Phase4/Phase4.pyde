def setup():
    size(400, 400)
    noStroke()

def drawObject(x, y, s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    square(20, 20, 30) 
    square(80, 20,  30) 
    rect(40, 60,  50, 20) 
    fill(255, 255, 255)
    circle(35, 35, 20)
    circle(95, 35, 20)
    fill(0)
    circle(32, 32, 3)
    circle (92, 32, 3)
    pop()
     
def draw():
    for x in range (0, 381, 20):
        drawObject(x, 0, .2)
    for y in range (0, 381, 20):
        drawObject(x, y, .2)
    
    
    

    
    
    
