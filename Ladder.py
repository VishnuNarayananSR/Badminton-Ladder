import tkinter as tk
from datetime import datetime
import turtle
import os
from Player import Player
from File import File
HEIGHT = 600
WIDTH = 300
MARGIN = 20
CARDSPACING = 40
CARDWIDTH = 250
CARDH = 30
class Ladder(tk.Frame):
    name_stack = []
    cards = []
    def __init__(self, master=None):
        super().__init__(master)
        if os.path.exists('ladder.txt'):
            with open('ladder.txt', 'r') as ladderfile:
                for line in ladderfile.readlines():
                    Ladder.name_stack.append(line.strip())
        self.master = master
        self.master.resizable(False,False)
        self.pack()
        self.create_ladder(master)
        self.update_ladder()
    def create_ladder(self, master):
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.pack(side="right")
        self.add_player = tk.Button(self, text="Add player to ladder",
                                    command=self.add_player)
        self.add_player.pack(side="right")
        self.add_challenge = tk.Button(self, text="Add Challenge",
                                    command=self.add_challenge)
        self.add_challenge.pack(side="top")

        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("#0073FF")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_player(self):
        self.new_player_window = Player(self.master, self)
        self.update_ladder()
    def add_challenge(self):
        self.new_challenge_window = Challenge(self.master)
    def update_ladder(self):
        for pos, name in enumerate(Ladder.name_stack):
            card = turtle.RawTurtle(self.screen)
            card._tracer(0)
            card.color("blue")
            card.fillcolor("#d39364")
            card.penup()
            card.goto(-WIDTH//2 + MARGIN, HEIGHT//2 - CARDSPACING - (CARDSPACING * pos))
            card.pendown()
            card.begin_fill()
            for side in range(2):
                card.forward(CARDWIDTH)
                card.left(90)
                card.forward(CARDH)
                card.left(90)
            card.end_fill()
            card.penup()
            card.goto(-WIDTH//2 + 10 + MARGIN, HEIGHT//2 - CARDSPACING - (CARDSPACING * pos) + 5)
            card.pendown()
            card.color("white")
            card.write(name)
            # card.clear()
            Ladder.cards.append(card)



class Challenge(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Add Challege")
        self.resizable(False,False)
        self.minsize(300,200)
        self.maxsize(300,200)
        self.challenger = tk.StringVar()
        self.challengee = tk.StringVar()
        self.date = tk.StringVar()
        self.name_entry1 = tk.Entry(self,textvariable = self.challenger)
        self.name_entry2 = tk.Entry(self,textvariable = self.challengee)
        self.date_entry = tk.Entry(self, textvariable = self.date)
        tk.Label(self, text = "Enter Challenger name").pack(side='top')
        self.name_entry1.pack(side="top")
        tk.Label(self, text = "Enter Challengee name").pack(side='top')
        self.name_entry2.pack(side="top")
        tk.Label(self, text = "Enter Date(dd-mm-yyyy)").pack(side='top')
        self.date_entry.pack(side="top")
        self.add_btn = tk.Button(self, text="ADD",width=10,height=2, command=self.add_challenge)
        self.add_btn.pack()
        self.bind('<Return>', lambda event: self.add_challenge())

    def add_challenge(self):
        name1 = self.name_entry1.get()
        name2 = self.name_entry2.get()
        date = self.date_entry.get()
        if name1 and name2 in Ladder.name_stack:
            if name1 == name2:
                tk.Label(self, text = "Player cannot challenge himself", fg='red').pack(side='bottom')
            else:
                try:
                    dt = datetime.strptime (date, "%d-%m-%Y")
                    dt = dt.date()
                    pos1 = Ladder.name_stack.index(name1) + 1
                    pos2 = Ladder.name_stack.index(name2) + 1

                    if abs(pos1 - pos2) > 3:
                        tk.Label(self, text = "challenge to players beyond three places above is forbidden", fg='red').pack(side='bottom')
                    else:
                        File().write_challege_data(name1, pos1, name2, pos2, _date)
                        # with open("data.txt", "a") as datafile:
                        #     datafile.write(f'{name1} {pos1} {name2} {pos2} {dt}\n')
                        self.destroy()

                except ValueError:
                    tk.Label(self, text = "Invalid date!", fg='red').pack(side='bottom')
        else:
            tk.Label(self, text = "Unknown Player Name", fg='red').pack(side='bottom')

root = tk.Tk()
app = Ladder(root)
app.mainloop()