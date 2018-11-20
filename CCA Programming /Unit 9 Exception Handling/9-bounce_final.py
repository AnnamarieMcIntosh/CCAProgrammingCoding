from tkinter import *
import random
import time

BALL_STEP = 3
PADDLE_STEP = 4


class Ball:
       
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 230, 100)
        self.possible_moves = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -BALL_STEP
        # we need to separate the concept of ball moving and hitting bottom
        # into separate state variables
        self.moving = False  # new instance variable     
        self.hit_bottom = False 

    def start(self): # new
        """
        Start the ball moving
        """
        self.moving = True

    def reset(self):  # new
        """
        Resets the ball by moving it back to its start position,
        reseting the x and y move values and resetting the
        state variable.
        """
        self.canvas.coords(self.id, 10, 10, 25, 25)
        self.canvas.move(self.id, 230, 100)
        self.x_move = random.choice(self.possible_moves)
        self.y_move = -BALL_STEP
        self.moving = False # new
        self.hit_bottom = False
    
    def draw(self):
        if self.moving: # use moving variable instead
            self.canvas.move(self.id, self.x_move, self.y_move)
            pos = self.canvas.coords(self.id)
            height = self.canvas.winfo_height()
            width = self.canvas.winfo_width()
            if pos[1] <= 0: # upper y
                self.y_move = BALL_STEP
            # height is 1 on first iteration, until canvas gets rendered.
            if pos[3] >= height and height != 1: # lower y
                self.moving = False  # add this
                self.hit_bottom = True
            if pos[0] <= 0: # left x
                self.x_move = BALL_STEP
            if pos[2] >= width: # right x
                self.x_move = -BALL_STEP
            if self.hit_paddle(pos): # bounce up off paddle
                self.y_move = -self.y_move

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

    def reset(self): #new
        """
        Resets the paddle by moving it back to its start position,
        """
        self.canvas.coords(self.id, 0, 0, 100, 10)
        self.canvas.move(self.id, 200, 300)
        self.x_move = 0

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
        self.paddle = Paddle(canvas, "hot pink")                    
        self.ball = Ball(canvas, self.paddle, "MediumPurple1")
        self.game_over = False

    def start(self):
        """
        This method starts the game moving by calling the ball's start method
        """
        self.ball.start()

    def reset(self):
        self.ball.reset()
        self.paddle.reset()
        self.game_over = False

    def advance(self):
        self.ball.draw()
        self.game_over = self.ball.hit_bottom
        self.paddle.draw()
        self.tk.after(1, self.advance)
        

    
def main():
    tk = Tk()
    tk.title("Bounce")
    
    canvas = Canvas(tk, width=500, height=400, bd=0)
    canvas.pack()
    game = Game(tk, canvas)

    # create a new frame for our buttons
    frame = Frame(tk)
    frame.pack()
    # add button to Start the game
    start_button = Button(frame, text="START", bg='grey', command=game.start)
    start_button.pack(side=LEFT)
    # add a button to Restart the game
    reset_button = Button(frame, text="RESET", command=game.reset)
    reset_button.pack(side=LEFT)
    # add a button to Quit the game
    quit_button = Button(frame, text="QUIT", command=tk.destroy)
    quit_button.pack(side=RIGHT)

    game.advance()

    tk.mainloop()

        

if __name__ == '__main__':
    main()
