from processing_py import *


app = App(600,400) # create window: width, height
app.background(0,0,0) # set background:  red, green, blue

# draw rectangle
app.fill(255,255,0) # set color for objects: red, green, blue
app.rect(100,100,200,100) # draw a rectangle: x0, y0, size_x, size_y

# draw line
app.fill(0,0,255) # set color for objects: red, green, blue
app.ellipse(300,200,50,50) # draw a circle: center_x, center_y, size_x, size_y


img = app.loadImage('Pictures/ghpicture.png')
app.background(0, 0, 0) # set background red, green, blue
app.image(img, 100, 100, 400, 200)



def setup():
    size(640, 360)
    stroke(255)
    noFill()


def draw():
    background(0)
    for i in range(0, 200, 20):
        bezier(mouseX - (i / 2.0), 40 + i, 410, 20, 440,
               300, 240 - (i / 16.0), 300 + (i / 8.0))


# Implementing mouse functionality
setup()
while True:
    draw()

app.redraw() # refresh the window
