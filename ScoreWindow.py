import tkinter as tk
from tkinter import ttk
from File import File
class ScoreWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Update Score")
        self.update_score()
    def update_score(self):
        self.challenge_chosen = tk.StringVar()
        tk.Label(self, text = "Select challenge").pack(side='top')
        challenge_list = ttk.Combobox(self, width = 60, textvariable = self.challenge_chosen)
        options = File().get_yet_to_finish_challenges()
        challenge_list['values'] = options
        challenge_list['state'] = 'readonly'
        challenge_list.current(0)
        challenge_list.pack()
        self.score = tk.StringVar()
        self.score_entry = tk.Entry(self,textvariable = self.score,
                                 font=('calibre',10,'normal'))
        tk.Label(self, text = "Enter Score entries (12-21 20-21)").pack(side='top')
        self.score_entry.pack(side="top")
        self.challenge_button = tk.Button(self, text="OK", command=lambda : self.write_score(self.challenge_chosen.get(),self.score.get()))
        self.challenge_button.pack()
    def write_score(self, data, score):
        if not score:
            tk.Label(self, text = "Invalid Score format").pack(side='bottom')
        File().update_score(data, score)
        self.destroy()

if __name__ == "__main__":
    pass