from tkinter import *
import random
import time

BALL_STEP = 3
PADDLE_STEP = 2


class Ball:

    def __init__(self, canvas, paddle, color): # pass the paddle to Ball constructor
        self.canvas = canvas
        self.paddle = paddle # remember the paddle
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -BALL_STEP

    def draw(self):
        self.canvas.move(self.id, self.x_move, self.y_move)
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        if pos[1] <= 0: # upper y
            self.y_move = BALL_STEP
        if pos[3] >= height: # lower y
            self.y_move = -BALL_STEP
        if pos[0] <= 0: # left x
            self.x_move = BALL_STEP
        if pos[2] >= width: # right x
            self.x_move = -BALL_STEP
        # add a new test to see if the ball has hit the paddle
        if self.hit_paddle(pos): # bounce off paddle
            self.y_move = -self.y_move # change direction

    def hit_paddle(self, pos):
        '''
        Check whether the ball has hit the paddle
        pos is the position of the ball
        '''
        paddle_pos = self.canvas.coords(self.paddle.id)
        # pos[2] is the x pos of the lower bounding box of ball (right edge)
        # pos[0] is the x pos of the upper bounding box of ball (left edge)
        # check if thes x positions are with in the x range of the paddle
        # is the right edge of the ball to the rigth of the left edge of the paddle AND
        # is the left edge of the ball to the left of the right edge of the paddle
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # x range
            # pos[3] is the y pos of the lower bounding box of ball (bottom edge)
            # pos[1] is the y pos of the upper bounding box of ball (top edge)
            # is the bottom edge of the ball lower than the top edge of the paddle AND
            # is the top edge of the ball higher than the bottom edge of the paddle
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]: # y range
                return True
        return False


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x_move = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def move_left(self, evt):
        self.x_move = -PADDLE_STEP

    def move_right(self, evt):
        self.x_move = PADDLE_STEP
        
    def draw(self):
        self.canvas.move(self.id, self.x_move, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0: # left x
            self.x_move = 0
        if pos[2] >= self.canvas.winfo_width(): # right x
            self.x_move = 0


class Game():
    
    def __init__(self, tk, canvas):
        self.canvas = canvas
        self.tk = tk
        self.paddle = Paddle(canvas, "blue")                    
        self.ball = Ball(canvas, self.paddle, "red") # pass in the paddle

    def advance(self):
        self.ball.draw()
        self.paddle.draw()
        self.tk.after(1, self.advance)
   

def main():
    tk = Tk()
    tk.title("Bounce")
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()
                    
    game = Game(tk, canvas)
    game.advance()

    tk.mainloop()
            

if __name__ == '__main__':
    main()
