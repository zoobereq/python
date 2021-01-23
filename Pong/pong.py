# Implementation of classic arcade game Pong
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
direction = RIGHT
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    elif direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score1, score2  
    spawn_ball(LEFT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]         
                  
    # draw ball
    ball = canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 40 and paddle1_pos + paddle1_vel <= 360: 
        paddle1_pos = paddle1_pos + paddle1_vel
        
    if paddle2_pos + paddle2_vel >= 40 and paddle2_pos + paddle2_vel <= 360:
        paddle2_pos = paddle2_pos + paddle2_vel   
    
    # draw paddles
    paddle1 = canvas.draw_line([4, (paddle1_pos - 40)], [4, (paddle1_pos + 40)], 8, "White")
    paddle2 = canvas.draw_line([596, (paddle2_pos - 40)], [596, (paddle2_pos + 40)], 8, "White")
    
    # determine whether paddle and ball collide
    # define the behavior of the ball at each vertical collision
    # increase ball velocity with each vertical collision   
    if ball_pos[0] <= 28 and ball_pos[1] >= paddle1_pos - 40 and ball_pos[1] <= paddle1_pos + 40:
        ball_vel[0] = - ((.1 * ball_vel[0]) + ball_vel[0])
        ball_vel[1] = ((.1 * ball_vel[1]) + ball_vel[1])
    if ball_pos[0] >= 572 and ball_pos[1] >= paddle2_pos - 40 and ball_pos[1] <= paddle2_pos + 40:
        ball_vel[0] = - ((.1 * ball_vel[0]) + ball_vel[0])
        ball_vel[1] = ((.1 * ball_vel[1]) + ball_vel[1])
    
    # define ball's behavior with each horizonal collision
    if ball_pos[1] <= 20:
        ball_vel[1] = - ball_vel[1]
          
    if ball_pos[1] >= 380:
        ball_vel[1] = - ball_vel[1] 
        
    # define and draw scoring
    if ball_pos[0] < 28:
        score2 = score2 + 1
        spawn_ball(RIGHT)
        
    if ball_pos[0] > 572:
        score1 = score1 + 1
        spawn_ball(LEFT)
    
    canvas.draw_text(str(score1), (150, 150), 40, "White", "sans-serif")
    canvas.draw_text(str(score2), (450, 150), 40, "White", "sans-serif")  
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 3
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 3

def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_up, paddle1_down, paddle2_up, paddle2_down
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel  = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel  = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel  = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)

# start frame
new_game()
frame.start()



