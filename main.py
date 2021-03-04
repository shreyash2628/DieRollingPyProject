
#importing Python libraries
import random
import tkinter

#setting up GUI instance
root = tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')

#space used to display die
label = tkinter.Label(root, text='', font=('Helvetica', 260))

#function used to generate random nos
def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()

button = tkinter.Button(root, text='roll dice', foreground='blue', command=roll_dice)
button.pack()
root.mainloop()