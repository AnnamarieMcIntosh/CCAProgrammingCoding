from tkinter import *
import random
import time

STEP = 1 # this is the amount of pixels we move at a time

class Ball:

    def __init__(self, tk, canvas, color):
        '''
        Creates an instance of a ball in the center of the canvas and sets
        it's move values.
        '''
        self.tk = tk  # our root window
        self.canvas = canvas
        # create a ball to draw on our canvas
        # keep track of the id so that we can refer to it later
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        # position the ball where we want it to start
        # position (0,0) is the upper left corner of our canvas
        self.canvas.move(self.id, 235, 100)
        # our ball will move by x_move and y_move pixels at a time.
        # note that x does not change (it moves 0 pixels)
        self.x_move = 0
        self.y_move = -STEP

    def draw(self):
        '''
        Moves the ball according to the x_move and y_move values
        '''
        # redraws our ball
        # x_move is how many pixels to shift the current x position
        # y_move is how many pixels to shipt the current y position
        # a negative value for y will shift up, a positive value down
        # a negative value for x will shift left, a positive value right
        self.canvas.move(self.id, self.x_move, self.y_move)

    def advance(self):
        '''
        Moves the ball once, then schedules to move it again
        '''
        # draw the ball once
        self.draw()
        # after 1 millisecond, call advance() to move the ball again
        self.tk.after(1, self.advance)


def main():
    tk = Tk()
    tk.title("Bounce")
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()

    ball = Ball(tk, canvas, 'red')  # create our ball instance
    ball.advance() # start our ball moving

    tk.mainloop() # wait for user input
            

if __name__ == '__main__':
    main()
