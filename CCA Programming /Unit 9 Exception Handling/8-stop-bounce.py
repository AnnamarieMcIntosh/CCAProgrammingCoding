from tkinter import *
import random
import time

BALL_STEP = 3
PADDLE_STEP = 4


class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -BALL_STEP
        self.hit_bottom = False

    def draw(self):
        if not self.hit_bottom:
            self.canvas.move(self.id, self.x_move, self.y_move)
            pos = self.canvas.coords(self.id)
            height = self.canvas.winfo_height()
            width = self.canvas.winfo_width()
            if pos[1] <= 0: # upper y
                self.y_move = BALL_STEP
            # height is 1 on first iteration, until canvas gets rendered.
            if pos[3] >= height and height != 1: # lower y
                self.hit_bottom = True
            if pos[0] <= 0: # left x
                self.x_move = BALL_STEP
            if pos[2] >= width: # right x
                self.x_move = -BALL_STEP
            if self.hit_paddle(pos): # bounce up off paddle
                self.y_move = -self.y_move #change directions

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # x range
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
        self.ball = Ball(canvas, self.paddle, "red")

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
