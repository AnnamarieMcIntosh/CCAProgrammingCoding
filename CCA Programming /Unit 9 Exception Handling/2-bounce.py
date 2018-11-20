from tkinter import *
import random
import time

STEP = 8


class Ball:

    def __init__(self, tk, canvas, color):
        self.tk = tk
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 235, 100)
        self.x_move = 0
        self.y_move = -STEP

    def draw(self):
        self.canvas.move(self.id, self.x_move, self.y_move)
        # get the current coordinates of our ball
        # pos return the list [x1, y1, x2, y2]
        # where (x1, y1) is the upper left corner of our objects bounding box
        # and (x2, y2) is the lower right corner of our object's bounding box
        pos = self.canvas.coords(self.id)
        # get the height of our canvas
        height = self.canvas.winfo_height()
        if pos[1] <= 0: # upper y
            self.y_move = STEP # start moving down
        if pos[3] >= height: # lower y
            self.y_move = -STEP # start moving up

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
