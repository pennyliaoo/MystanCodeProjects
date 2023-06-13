"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
the game start condition and finish condition set in user
and the animation put the in the user
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
check = False


def main():
    # Add the animation loop here!
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    while True:
        pause(FRAME_RATE)
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            if lives >0:
                graphics.reset()
            else:
                break
        if graphics.bricknum == 0:
            break
        dx = graphics.getball_vx()
        dy = graphics.getball_vy()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.setvx(-dx)
        if graphics.ball.y <= 0:
            graphics.setvy(-dy)

        graphics.collisioncheck()





if __name__ == '__main__':
    main()
