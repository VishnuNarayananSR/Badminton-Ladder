import tkinter as tk
from File import File
from datetime import datetime
class ChallengeDisplay(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Challenge Display")
        self.by_player_btn = tk.Button(self, text="By player name", command=self.by_player_name)
        self.yet_play_btn = tk.Button(self, text="Yet to play challenges", command=self.yet_to_play)
        self.date_btn = tk.Button(self, text="By date", command=self.by_date)
        self.yet_play_btn.pack()
        self.by_player_btn.pack()
        self.date_btn.pack()
        self.display = tk.Text(self,state='disabled')
        self.display.pack()
        self.name = tk.StringVar()
        self.date = tk.StringVar() 
        self.name_entry = tk.Entry(self, textvariable=self.name)
        self.date_entry =tk.Entry(self, textvariable=self.date)
        self.player_name_label = tk.Label(self, text="Enter Player Name")
        self.date_label = tk.Label(self, text="Enter Date (dd-mm-yyyy)")
        self.search_btn = tk.Button(self, text='Search')
    def by_player_name(self):
        self.player_name_label.pack()
        self.name_entry.pack(side ='top')
        self.search_btn.configure(command=self.player_btn_action)
        self.search_btn.pack()
        self.date_entry.pack_forget()
        self.date_label.pack_forget()
        self.bind('<Return>', lambda event :self.player_btn_action())

    def by_date(self):
        self.date_label.pack()
        self.date_entry.pack(side ='top')
        self.search_btn.configure(command=self.date_btn_action)
        self.search_btn.pack()
        self.name_entry.pack_forget()
        self.player_name_label.pack_forget()
        self.bind('<Return>', lambda event :self.date_btn_action())

    def yet_to_play(self):
        self.display.configure(state='normal')
        self.clear(self.display)
        self.display.insert(tk.END,"yet to play")
        self.display.configure(state='disabled')
    def player_btn_action(self):
        self.display.configure(state='normal')
        self.clear(self.display)
        name_str = self.name.get()
        res = File().get_challenges_by_player_name(name_str)
        self.display.insert(tk.END, f"By player name {name_str}:\n\n")
        for i, ch in enumerate(res):
            self.display.insert(tk.END, f"{i + 1}. {ch} \n")
        self.display.configure(state='disabled')
        self.name_entry.pack_forget()
        self.player_name_label.pack_forget()
        self.search_btn.pack_forget()
    def date_btn_action(self):
        self.display.configure(state='normal')
        self.clear(self.display)
        date_str = self.date.get()
        try:
            dt = datetime.strptime (date_str, "%d-%m-%Y")
            dt = dt.date().strftime("%d-%m-%Y")
            res = File().get_challenges_by_date(date_str)
            self.display.insert(tk.END, f"Challenges on {date_str}:\n\n")
            for i, ch in enumerate(res):
                self.display.insert(tk.END, f"{i + 1}. {ch} \n")
            self.display.configure(state='disabled')
            self.date_entry.pack_forget()
            self.date_label.pack_forget()
            self.search_btn.pack_forget()
        except ValueError:   
            tk.messagebox.showerror("Error", "Invalid Date!")
    def clear(self,display):
        display.delete('1.0', tk.END)