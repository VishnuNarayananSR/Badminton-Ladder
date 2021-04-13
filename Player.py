from File import File
import tkinter as tk
from datetime import datetime
class Player(tk.Toplevel):
    def __init__(self, master=None, parent=None):
        super().__init__(master = master)
        self.title("Add player")
        # self.minsize(300,100)
        # self.maxsize(300,100)
        # self.resizable(False,False)
        self.name = tk.StringVar()
        self.date = tk.StringVar()
        self.name_entry = tk.Entry(self,textvariable = self.name,
                                 font=('calibre',10,'normal'))
        tk.Label(self, text = "Enter Name").pack(side='top')
        self.name_entry.pack(side="top")
        self.date_entry = tk.Entry(self,textvariable = self.date,
                                 font=('calibre',10,'normal'))
        tk.Label(self, text = "Enter date(dd-mm-yyyy)").pack(side='top')
        self.date_entry.pack(side="top")
        self.bind('<Return>', lambda event: self.add_player(parent))
        self.add_btn = tk.Button(self, text="ADD", command=lambda: self.add_player(parent))
        self.add_btn.pack(side="top")

    def add_player(self,parent):
        name = self.name.get()
        date = self.date.get()
        try:
            dt = datetime.strptime (date, "%d-%m-%Y")
            dt = dt.date()
            File().add_player_file(player_name=name, _date=date)
            parent.name_stack.append(name)
            parent.update_ladder()
            self.destroy()
        except ValueError:
            tk.Label(self, text = "Invalid date!", fg='red').pack(side='bottom')
        



if __name__ == "__main__":
    pass