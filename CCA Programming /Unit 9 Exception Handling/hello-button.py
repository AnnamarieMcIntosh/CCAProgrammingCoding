from tkinter import *

class App:

    def __init__(self, root):
        """ App class constructor """
        # create a frame widget for our buttons
        # a frame is a simple container that can hold and position
        # other widgets,
        frame = Frame(root)
        # call pack to make our frame visible
        frame.pack()

        # create two button widgets inside of our frame
        # text: the text on our button
        # command: a call back function to be invoked when the button is clicked.
        self.quit_button = Button(frame, text='QUIT', command=root.destroy)
        self.quit_button.pack(side=LEFT) # pack also manages layout

        self.hi_button = Button(frame, text="Hello", command=self.say_hi)
        self.hi_button.pack(side=LEFT)

    def say_hi(self):
        print("Hello World!")


def main():
    root = Tk() 
    app = App(root)
    root.mainloop() # calls the tk event loop
       

if __name__ == '__main__':
    main()
