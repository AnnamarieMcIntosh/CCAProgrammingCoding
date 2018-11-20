from tkinter import *
import random
import time

# give the ball and paddle separate step variables
# this way they can move a different speeds
BALL_STEP = 3
PADDLE_STEP = 4


class Ball:

    def __init__(self, tk, canvas, color):
        self.tk = tk
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -BALL_STEP #change var
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x_move, self.y_move)
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        # change var to BALL_STEP
        if pos[1] <= 0: # upper y
            self.y_move = BALL_STEP 
        if pos[3] >= height: # lower y
            self.y_move = -BALL_STEP
        if pos[0] <= 0: # left x
            self.x_move = BALL_STEP
        if pos[2] >= width: # right x
            self.x_move = -BALL_STEP

    def advance(self):
        self.draw()
        self.tk.after(1, self.advance)



class Paddle:

    def __init__(self, tk, canvas, color):
        '''
        Creates an instance of a paddle in the center of the canvas and sets
        it's move values.
        Binds the left and right arrow keys to functions that change the paddle direction
        '''
        self.tk = tk
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        # no y value, only moves left to right
        self.x_move = 0 # paddle starts off as NOT moving
        # define handlers for left and right arrow key
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def move_left(self, evt):
        '''
        Force paddle to move left
        '''
        self.x_move = -PADDLE_STEP

    def move_right(self, evt):
        '''
        Force paddle to move right
        '''
        self.x_move = PADDLE_STEP
        
    def draw(self):
        '''
        Moves the paddle according to the x_move and y_move values
        '''  
        self.canvas.move(self.id, self.x_move, 0) # y is always 0, b/c we only move left/right
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0: # left x
            self.x_move = 0 # don't change position, just stop
        if pos[2] >= self.canvas.winfo_width(): # right x
            self.x_move = 0 # don't change position, just stop

    def advance(self):
        '''
        Moves the paddle once, then schedules to move it again
        '''
        self.draw()
        self.tk.after(1, self.advance)


def main():
    tk = Tk()
    tk.title("Bounce")
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()
                    
    ball = Ball(tk, canvas, 'red')
    ball.advance()
    paddle = Paddle(tk, canvas, 'blue')
    paddle.advance()  # add call to start paddle moving


    tk.mainloop()
            

if __name__ == '__main__':
    main()
