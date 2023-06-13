"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
this part is in code and the origin screen and the setting are all in this .py
including the paddle, ball, and brick.
in order to prevent user change the velocity easily so put the velocity in code and set into the private variable

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball



class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,x=(window_width-paddle_width)/2,y=(window_height-paddle_offset))
        self.paddle.filled= True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,x = (window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.bricknum = 100

        # create the brick
        
        for j in range(brick_rows):
            for i in range(brick_cols):
                brick = GRect(width=brick_width, height=brick_height, x=(brick_spacing+brick_width)*i, y=brick_offset+(brick_height+brick_spacing)*j)
                brick.filled = 'True'
                if j ==0 or j ==1:
                    brick.color = 'red'
                    brick.fill_color = 'red'
                elif j == 2 or j ==3:
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                elif j == 4 or j == 5:
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                elif j == 6 or j == 7:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                elif j ==8 or j ==9:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'

                self.window.add(brick)
        onmousemoved(self.brick_pos)
        # velocity
        self.__dx = 0
        self.__dy = 0

        # check
        self.check = False
        onmouseclicked(self.stargame)
        # self.collisioncheck()

    def reset(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.check = False


    def collisioncheck(self):
        ballpoint1 = self.window.get_object_at(self.ball.x,self.ball.y)
        ballpoint2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ballpoint3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ballpoint4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if ballpoint1 is not None:
            if ballpoint1 is not self.paddle:
                self.window.remove(ballpoint1)
                self.bricknum -= 1
                self.setvy(-self.__dy)
            else:
                if self.__dy > 0:
                    self.setvy(-self.__dy)

        elif ballpoint2 is not None:
            if ballpoint2 is not self.paddle:
                self.window.remove(ballpoint2)
                self.bricknum -= 1
                self.setvy(-self.__dy)
            else:
                if self.__dy > 0:
                    self.setvy(-self.__dy)

        elif ballpoint3 is not None:
            if ballpoint3 is not self.paddle:
                self.window.remove(ballpoint3)
                self.bricknum -= 1
                self.setvy(-self.__dy)
            else:
                if self.__dy > 0:
                    self.setvy(-self.__dy)

        elif ballpoint4 is not None:
            if ballpoint4 is not self.paddle:
                self.window.remove(ballpoint4)
                self.bricknum -= 1
                self.setvy(-self.__dy)
            else:
                if self.__dy > 0:
                    self.setvy(-self.__dy)

    def stargame(self,event):
        if not self.check:
            self.check = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = random.randint(1, INITIAL_Y_SPEED)

    # setter (by setter to get new volecity)
    def setvx(self, vx):
        self.__dx = vx

    def setvy(self,vy):
        self.__dy = vy

    # getter vx,vy
    def getball_vx(self):
        # self.__dx = random.randint(1, MAX_X_SPEED)
        # if random.random() > 0.5:
        #     self.__dx = -self.__dx
        return self.__dx

    def getball_vy(self):
        # self.__dy = random.randint(0, INITIAL_Y_SPEED)
        # if random.random() > 0.5:
        #     self.__dy = -self.__dy
        return self.__dy

    def brick_pos(self, event):
        self.paddle.x = event.x - self.paddle.width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x > self.window.width-self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width


        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks
