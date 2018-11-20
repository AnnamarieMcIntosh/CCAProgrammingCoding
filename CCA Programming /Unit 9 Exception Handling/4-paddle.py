from tkinter import *
import random
import time

STEP = 3


class Ball:

    def __init__(self, tk, canvas, color):
        self.tk = tk
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -STEP
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x_move, self.y_move)
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        if pos[1] <= 0: # upper y
            self.y_move = STEP
        if pos[3] >= height: # lower y
            self.y_move = -STEP
        if pos[0] <= 0: # left x
            self.x_move = STEP
        if pos[2] >= width: # right x
            self.x_move = -STEP

    def advance(self):
        self.draw()
        self.tk.after(1, self.advance)


# Add a new class to draw a paddle.  It doesn't move yet!
class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

    def draw(self):
        pass

    

def main():
    tk = Tk()
    tk.title("Bounce")
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()
                    
    ball = Ball(tk, canvas, 'red')
    ball.advance()
    # create our new stationary paddle
    paddle = Paddle(canvas, 'blue')


    tk.mainloop()
            

if __name__ == '__main__':
    main()
