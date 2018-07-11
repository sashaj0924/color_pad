def setup():
    size(500, 500)
    background(252, 51, 255) 
    rect( 60, 20, 55,400, 10) 
    fill (66, 51, 255) 
    rect (20, 10, 85, 15)
      
    
def draw():
    if mousePressed and (mouseButton == RIGHT):
        fill(50, 0, 0)
        ellipse(mouseX, mouseY, 20, 20)
    if mousePressed and (mouseButton == CENTER):
        fill(88, 24, 69)
        ellipse(mouseX, mouseY, 20, 20)
    if mousePressed and (mouseButton == LEFT):
        fill(66, 51, 255)
        ellipse(mouseX, mouseY, 20, 20)
