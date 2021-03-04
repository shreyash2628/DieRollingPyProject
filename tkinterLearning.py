import random
from tkinter import *

root = Tk()
root.geometry("700x450")
root.title("Roll Die")

label = Label(root,text="s")

def roll_dice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

    button = Button(root,text="Roll",command=roll_dice())
    button.pack()

root.mainloop()