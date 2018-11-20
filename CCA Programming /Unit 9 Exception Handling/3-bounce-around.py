from tkinter import *
import random # needed to start ball moving at a random angle
import time

# let's make the ball move a little faster
STEP = 3


class Ball:

    def __init__(self, tk, canvas, color):
        self.tk = tk
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        # lets make an intital move value for our x coordinate
        # make it random so that the ball appears to move differently
        # at each play.
        # by moving both the x and y coordinate, the ball
        # will appear to move at an angle
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -STEP

    def draw(self):
        self.canvas.move(self.id, self.x_move, self.y_move)
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()
        # we need to know the canvas width so we can tell when the
        # ball hits the right side of the canvas
        width = self.canvas.winfo_width()
        # notice we don't use elif here.  that's because the ball could
        # theoretically hit two sides simultaneously if it hits a corner.
        # so we need to check all sides for each move
        if pos[1] <= 0: # upper y
            self.y_move = STEP
        if pos[3] >= height: # lower y
            self.y_move = -STEP
        # add this code to check when we hit the left or right canvas
        if pos[0] <= 0: # left x
            self.x_move = STEP
        if pos[2] >= width: # right x
            self.x_move = -STEP

    def advance(self):
        self.draw()
        self.tk.after(1, self.advance)


def main():
    tk = Tk()
    tk.title("Bounce")
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()
                    
    ball = Ball(tk, canvas, 'red')
    ball.advance()

    tk.mainloop()
            

if __name__ == '__main__':
    main()
