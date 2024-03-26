

Okay so it seems actually pretty simple right now but I’m sure
I’m gonna run into some difficulties because I have a circle inside a square
and it may not be as easy as it seems.
But for now I’m gonna go to the graph and find the coordinates for x and y.
I need to review what it means to have (40, 10,  60, 10) again, I forgot.
Never mind, it's explained right after. Lol.
Okay so I have: 2 squares, 2 circles, and 1 rectangle. Let me look up the syntaxes for each. 
So square is: (a, b, extent), circle is: (a, b, extent), and rectangle is (a, b, c ,d)
On my graph paper, I have coordinates that are really small, like (2,2) so I'll probably just add a 0 to all of them for the pixel size. 
Since I have a circle inside the square, I'll have to change the color of the circle to delineate them.
OOH let me look up RGB numbers for different colors. 
So I plugged my numbers in and it's really not working lol. It looks at like one dot on it. The code I have is:
def setup():
    size(200, 300)
    noStroke()

def draw():
    fill(0)
    square(20, 20, 30) 
    square(80, 20,  30) 
    rect(40, 60,  50, 20) 
    
def draw(): 
    fill(140)
    circle(30, 30, 10)

OOOOH I just didn't have to create a new def draw():, and it worked with this:
def setup():
    size(200, 300)
    noStroke()

def draw():
    fill(0)
    square(20, 20, 30) 
    square(80, 20,  30) 
    rect(40, 60,  50, 20) 
    fill(140)
    circle(30, 30, 10)
    circle(90, 30, 10)

    Aww my robot is lowkey kinda cute, but the eyes aren't exactly in the middle like my shape. But it's so cute I kinda just wanna leave it like that. I understand it's an assignment so I'll get over the urge to be cute. 
    Okay so I think the reason the circles aren't in the center is because of how the coordinate starts it makes sense. Because I have graph paper I plotted the start of the circle at to the left corner of the grid box, so that means I have to make the coordinate in the center. So that's easy I think!. Yea it worked. 
    But now I wanna add a tiny little dot in the middle of the eye, so it looks more like an eye. I want the small circle to be on the top left, so it has to be between 30-35 and 90-95, and I'd rather stay in the integer world it doesn't have to be centered. Let me try (92, 32, 2) (32, 32, 2). OOO I have to make the circle white! And make the dot black! Also I should make the circle a bit bigger, like 15. 

    Lowkey just feel inclined to use resources to know the coordinates of colors. From this random website I found by searching, https://stackoverflow.com/questions/71276881/how-to-fill-shape-white, it says white is (255, 255, 255), so let me try that!


