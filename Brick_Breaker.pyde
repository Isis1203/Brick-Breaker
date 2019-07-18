canvas_x = 600 
canvas_y = 600
rectangle_count = 6 
rectangle_height = 30
rectangle_width = canvas_x / rectangle_count 
print(rectangle_width)
paddle_width = 120
showbrick1 = True
showbrick2 = True 
showbrick3 = True 
showbrick4 = True 
showbrick5 = True 
showbrick6 = True 

ball_y = 100
y_speed = 2 #switching the speed of the ball 
ball_x = 100 #added new variables to make the ball go left and right
x_speed = 2

def setup():
    size(600, 600)
    background(255, 255, 255) 

def draw():
    background(255, 255, 255) #added the background in order for one ball to show at a time
    global ball_x
    global ball_y
    global showbrick1
    global showbrick2 
    global showbrick3 
    global showbrick4 
    global showbrick5 
    global showbrick6 
    
    if showbrick1 == True:
        rect(0, 0, rectangle_width, rectangle_height)
    if showbrick2 == True:
        rect(rectangle_width, 0, rectangle_width, rectangle_height)
    if showbrick3 == True:
        rect(2 * rectangle_width, 0, rectangle_width, rectangle_height)
    if showbrick4 == True:
        rect(3 * rectangle_width, 0, rectangle_width, rectangle_height)
    if showbrick5 == True:
        rect(4 * rectangle_width, 0, rectangle_width, rectangle_height)
    if showbrick6 == True:
        rect(5 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255)
    ellipse (ball_x, ball_y, 20, 20)  
    
    if  ball_x < 30 and ball_x > 0 and ball_x < 100:
        showbrick1 = False
        print("brick1")
    if  ball_y < 30 and ball_x > 100 and ball_x < 200:
        showbrick2 = False 
        print("brick2")
    if  ball_y < 30 and ball_x > 200 and ball_x < 300:
        showbrick3 = False 
        print("brick3")
    if ball_y < 30 and ball_x > 300 and ball_x < 400:
        showbrick4 = False 
        print("brick4")
    if ball_y < 30 and ball_x > 400 and ball_x < 500:
        showbrick5 = False 
        print("brick5")
    if ball_y < 30 and ball_x > 500 and ball_x < 600:
        showbrick6 = False 
        print("brick6")
    
#code for paddle#
    if mouseX > 0 and mouseX < 590:
        fill(255, 255, 255) 
        rect(mouseX-paddle_width/2, 500, paddle_width, 15) 
   
#code for ball#        
    ball_y = ball_y + y_speed #made the ball faster, "if statement still needed to make the ball bounce" 
    ball_x = ball_x + x_speed 
     
    line(0, 0, 0, 0)
    line(600, 0, 600, 600) 
    line(0, 600, 600, 600) 
    line(600, 600, 600, 600) 
    
    if ball_y > 490 and ball_x < mouseX + paddle_width/2 and ball_x > mouseX - paddle_width/2:
        global y_speed #as before, I had to use global to call the variable down to this line of code
        y_speed = -2 #made the ball reverse 
    if ball_y < 40:
        global y_speed 
        y_speed = 2 
    if ball_x > 590:
        global x_speed
        x_speed = -2
    if ball_x < 10:
        global x_speed 
        x_speed = 2
    print(ball_x, ball_y)
    if ball_y > 590: 
        noLoop()
        print("Game Over")
