import turtle
from datetime import datetime
import os
import tkinter as tk
from Player import Player
from File import File
# from ScoreWindow import ScoreWindow
from ChallengeDisplay import ChallengeDisplay
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
        self.master = master
        self.master.resizable(False, False)
        self.pack(side="left")
        self.date_var = tk.StringVar()
        tk.Label(self,text="Ladder Date:").pack(side="top")
        self.chng_date_btn = tk.Button(self, text="Update Ladder Date", command=self.update_main_date)
        self.main_date_entry = tk.Entry(self, textvariable = self.date_var)
        self.main_date_entry.pack(side="top")
        self.chng_date_btn.pack(side="top")
        tk.Label(self,text="Number of challenges displaying:").pack(side="top")
        self.n_var = tk.StringVar()
        self.n_var.set(3)
        self.challenge_n_entry = tk.Entry(self, textvariable = self.n_var)
        self.challenge_n_btn = tk.Button(self, text="Update challenge count", command= lambda : self.update_challenge_canvas(int(self.n_var.get())))
        self.challenge_n_entry.pack(side="top")
        self.challenge_n_btn.pack(side="top")
        self.date_var.set(File().latest_date_in_the_data_file())
        self.create_ladder(master)
        self.update_main_date()
        self.update_ladder()
        self.update_challenge_canvas(int(self.n_var.get()))

    def create_ladder(self, master):
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=WIDTH, height=HEIGHT)
        self.canvas.pack(side="right")
        self.canvas2 = tk.Canvas(master)
        self.canvas2.config(width=WIDTH, height=HEIGHT)
        self.canvas2.pack(side="right")
        self.add_player = tk.Button(self, text="Add player to ladder",
                                    command=self.add_player)
        self.add_player.pack(side="top")
        self.remove_player_btn = tk.Button(self, text="Remove Player",
                                           command=self.remove_player)
        self.remove_player_btn.pack(side="top")
        self.add_challenge = tk.Button(self, text="Add Challenge",
                                       command=self.add_challenge)
        self.add_challenge.pack(side="top")
        self.display_challenge_btn = tk.Button(self, text="Display Challenge",
                                    command=self.display_challenge)
        self.display_challenge_btn.pack(side="top")
        # self.score_btn = tk.Button(self, text="Record score",
        #                            command=self.add_score)
        # self.score_btn.pack(side="right")
        self.screen = turtle.TurtleScreen(self.canvas)
        self.challenge_screen = turtle.TurtleScreen(self.canvas2)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.least_player = tk.Button(self,text="Least Active Player",
                                    command=self.show_least_active_player)
        self.least_player.pack()
        self.most_player = tk.Button(self,text="Most Active Player",
                                    command=self.show_most_active_player)
        self.most_player.pack()
        self.quit.pack(side="bottom")

    def update_main_date(self):
        self.main_date = self.date_var.get()
        try:
            Ladder.name_stack =  File().order_of_ladder_in_date(self.main_date)
            self.update_ladder()
        except ValueError:   
            tk.messagebox.showerror("Error", "Invalid Ladder Date!")
    def add_player(self):
        self.new_player_window = Player(self.master, self)

    def add_challenge(self):
        self.new_challenge_window = Challenge(self.master)

    # def add_score(self):
    #     self.new_score_window = ScoreWindow(self.master)

    def remove_player(self):
        self.remove_window = Player(self.master, self, "remove")

    def display_challenge(self):
        self.new_challenge_window = ChallengeDisplay(self.master, self)
    
    def show_least_active_player(self):
        ans = File().get_least_active_player()
        tk.messagebox.showinfo(message = f"Least active player is: {ans}")
    def show_most_active_player(self):
        ans = File().get_most_active_player()
        tk.messagebox.showinfo(message = f"Most active player is: {ans}")
    def update_ladder(self):
        self.screen.clear()
        self.screen.bgcolor("#0073FF")
        title_card = turtle.RawTurtle(self.screen)
        title_card._tracer(0)
        title_card.color('white')
        title_card.fillcolor("#d36e64")
        title_card.penup()
        title_card.goto(-WIDTH//2 + MARGIN, HEIGHT//2 -
                    CARDSPACING - (CARDSPACING * 0))
        title_card.pendown()
        title_card.begin_fill()
        for side in range(2):
            title_card.forward(CARDWIDTH)
            title_card.left(90)
            title_card.forward(CARDH)
            title_card.left(90)
        title_card.end_fill()
        title_card.penup()
        title_card.goto(-5, HEIGHT//2 -
                    CARDSPACING - (CARDSPACING * 0) + 5)
        title_card.pendown()
        title_card.color("white")
        title_card.write("BADMINTON LADDER", align="center")
        for pos, name in enumerate(Ladder.name_stack):
            card = turtle.RawTurtle(self.screen)
            card._tracer(0)
            card.color("blue")
            card.fillcolor("#d39364")
            card.penup()
            card.goto(-WIDTH//2 + MARGIN, HEIGHT//2 -
                      CARDSPACING - (CARDSPACING * (pos + 1)))
            card.pendown()
            card.begin_fill()
            for side in range(2):
                card.forward(CARDWIDTH)
                card.left(90)
                card.forward(CARDH)
                card.left(90)
            card.end_fill()
            card.penup()
            card.goto(-WIDTH//2 + 10 + MARGIN, HEIGHT//2 -
                      CARDSPACING - (CARDSPACING * (pos + 1)) + 5)
            card.pendown()
            card.color("white")
            card.write(name)
            # card.clear()
            Ladder.cards.append(card)
    def update_challenge_canvas(self, N):
        self.challenge_screen.clear()
        self.challenge_screen.bgcolor("#2b956d")
        title_card = turtle.RawTurtle(self.challenge_screen)
        title_card._tracer(0)
        title_card.color('white')
        title_card.fillcolor("#d36e64")
        title_card.penup()
        title_card.goto(-WIDTH//2 + MARGIN, HEIGHT//2 -
                    CARDSPACING - (CARDSPACING * 0))
        title_card.pendown()
        title_card.begin_fill()
        for side in range(2):
            title_card.forward(CARDWIDTH)
            title_card.left(90)
            title_card.forward(CARDH)
            title_card.left(90)
        title_card.end_fill()
        title_card.penup()
        title_card.goto(-5, HEIGHT//2 -
                    CARDSPACING - (CARDSPACING * 0) + 5)
        title_card.pendown()
        title_card.color("white")
        title_card.write(f"Latest {N} challenges", align="center")
        for pos, challenge in enumerate(File().get_latest_n_challenges(N)):
            card = turtle.RawTurtle(self.challenge_screen)
            card._tracer(0)
            card.color("blue")
            card.fillcolor("#d39364")
            card.penup()
            card.goto(-WIDTH//2 + MARGIN, HEIGHT//2 -
                      CARDSPACING - (CARDSPACING * (pos + 1)))
            card.pendown()
            card.begin_fill()
            for side in range(2):
                card.forward(CARDWIDTH)
                card.left(90)
                card.forward(CARDH)
                card.left(90)
            card.end_fill()
            card.penup()
            card.goto(-WIDTH//2 + 10 + MARGIN, HEIGHT//2 -
                      CARDSPACING - (CARDSPACING * (pos + 1)) + 5)
            card.pendown()
            card.color("white")
            res = challenge.split('/')
            card.write(f"{res[0]} --> {res[1]} on {res[2]}")
            # card.clear()
            Ladder.cards.append(card)

class Challenge(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Add Challege")
        # self.resizable(False,False)
        # self.minsize(300,200)
        # self.maxsize(300,200)
        self.challenger = tk.StringVar()
        self.challengee = tk.StringVar()
        self.date = tk.StringVar()
        self.name_entry1 = tk.Entry(self, textvariable=self.challenger)
        self.name_entry2 = tk.Entry(self, textvariable=self.challengee)
        self.date_entry = tk.Entry(self, textvariable=self.date)
        tk.Label(self, text="Enter Challenger name").pack(side='top')
        self.name_entry1.pack(side="top")
        tk.Label(self, text="Enter Challengee name").pack(side='top')
        self.name_entry2.pack(side="top")
        tk.Label(self, text="Enter Date(dd-mm-yyyy)").pack(side='top')
        self.date_entry.pack(side="top")
        self.score = tk.StringVar()
        self.score_entry = tk.Entry(self,textvariable = self.score,
                                 font=('calibre',10,'normal'))
        tk.Label(self, text = "Enter Score entries (Eg:12-21 20-21)").pack(side='top')
        self.score_entry.pack(side="top")
        self.add_btn = tk.Button(
            self, text="ADD", width=10, height=2, command=self.add_challenge)
        self.add_btn.pack()
        self.bind('<Return>', lambda event: self.add_challenge())

    def add_challenge(self):
        name1 = self.name_entry1.get()
        name2 = self.name_entry2.get()
        date = self.date_entry.get()
        scores = self.score_entry.get()
        if scores == '':
            scores = None
        if name1 in Ladder.name_stack and name2 in Ladder.name_stack:
            if name1 == name2:
                tk.Label(self, text="Player cannot challenge himself",
                         fg='red').pack(side='bottom')
            else:
                try:
                    dt = datetime.strptime (date, "%d-%m-%Y")
                    dt = dt.date().strftime("%d-%m-%Y")
                    latest_date = File().latest_date_in_the_data_file()
                    if dt < latest_date:
                        tk.messagebox.showerror("Date not acceptable", f"""You cannot add players to past.
                        \n Dates grater than latest date are only acceptable
                        \n Current latest date in ladder: {latest_date} """)
                    else:
                        pos1 = Ladder.name_stack.index(name1) + 1
                        pos2 = Ladder.name_stack.index(name2) + 1

                        if abs(pos1 - pos2) > 3:
                            tk.messgebox.showerror("challenge to players beyond three places or above is forbidden")
                        else:
                            File().write_challenge_data(name1, pos1, name2, pos2, dt, scores)
                            self.destroy()

                except ValueError:
                    tk.Label(self, text = "Invalid date!", fg='red').pack(side='bottom')
        else:
            tk.Label(self, text="Unknown Player Name",
                     fg='red').pack(side='bottom')


root = tk.Tk()
app = Ladder(root)
app.mainloop()
