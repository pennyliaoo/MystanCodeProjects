"""
File: 
Name:Penny
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
VY = 0
window = GWindow(800, 500, title='bouncing_ball.py')
# create the ball
ball = GOval(SIZE, SIZE, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)
ball.filled = True
window.add(ball)
check = False
cnt = 0
def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(star_ball)

def star_ball(mouse):
    # let ball drop
    global VY
    global GRAVITY
    global cnt
    global check
    if not check:
        check = True
        while True:
            if cnt == 3:
                break
            ball.move(VX, VY)
            VY += GRAVITY
            if VY == 0 or ball.y + ball.height >= window.height:
                VY = -VY * REDUCE
            if ball.x + ball.width >= window.width:
                ball.x = START_X - SIZE / 2
                ball.y = START_Y - SIZE / 2
                cnt += 1
                check = False
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
