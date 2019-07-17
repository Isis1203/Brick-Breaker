#variables for rectangles (top)#
canvas_x = 600 
canvas_y = 600
rectangle_count = 6 
rectangle_height = 30
rectangle_width = canvas_x / rectangle_count 
print(rectangle_width)
paddle_width = 120
#end of variables#

#variables for bouncing ball#
ball_y = 100
y_speed = 2 #switching the speed of the ball 
ball_x = 100 #added new variables to make the ball go left and right
x_speed = 2
#end of variables#

def setup():
    size(600, 600)
    background(255, 255, 255) 
    global ball_x
    global ball_y

def draw():
    background(255, 255, 255) #added the background in order for one ball to show at a time
    
#coding for bricks#
    rect(0, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255) 
    rect(rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255)  
    rect(2 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255)
    rect(3 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255)
    rect(4 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255)  
    rect(5 * rectangle_width, 0, rectangle_width, rectangle_height)
#end of code for bricks#
    
#code for paddle#
    if mouseX > 60 and mouseX < 540:
        fill(255, 255, 255) 
        rect(mouseX-60, 500, paddle_width, 15) 
    if mouseX < 60:
        rect(0, 500, paddle_width, 15) 
    if mouseX > 540:
        rect(390, 500, 120, 15)
#end of code for paddle#
   
#code for ball#        
    ball_y = ball_y + y_speed #made the ball faster, "if statement still needed to make the ball bounce" 
    ball_x = ball_x + x_speed 

    if ball_y > 385 and ball_y < 400 and ball_x > mouseX-60 and ball_x < mouseX+60:
        y_speed = 3 
    if ball_y < 10: 
        y_speed = 3 
    global ball_y
    global ball_x
    ellipse (ball_x, ball_y, 20, 20) 
    line(0, 0, 0, 0)
    line(600, 0, 600, 600) 
    line(0, 600, 600, 600) 
    line(600, 600, 600, 600) 
    if ball_y > 490 and ball_x < mouseX + paddle_width/2 and ball_x > mouseX - paddle_width/2:
        global y_speed #as before, I had to use global to call the variable down to this line of code
        print("BOUNCE") #bounce appeared at the bottom in the text box therefore, the barrier is on the right track 
        y_speed = -2 #made the ball reverse 
        #now add another "if" statement to get the ball bounce back and forth* 
    if ball_y < 50:
        global y_speed 
        print("BOUNCE2") 
        y_speed = 2 
    if ball_x > 590:
        global x_speed
        print("BOUNCEL") 
        x_speed = -2
    if ball_x < 50:
        global x_speed 
        print("BOUNCER")
        x_speed = 2
    print(ball_x, x_speed)
    if ball_y > 600: 
        noLoop()
#code for ball ends here#
