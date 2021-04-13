from file_operations import add_player
import tkinter as tk
class Player(tk.Toplevel):
    def __init__(self, master=None, parent=None):
        super().__init__(master = master)
        self.title("Add player")
        self.minsize(300,100)
        self.maxsize(300,100)
        self.resizable(False,False)
        self.name = tk.StringVar()
        self.name_entry = tk.Entry(self,textvariable = self.name,
                                 font=('calibre',10,'normal'))
        tk.Label(self, text = "Enter Name").pack(side='top')
        self.name_entry.pack(side="top")
        self.bind('<Return>', lambda event: self.add_player(parent))
        self.add_btn = tk.Button(self, text="ADD", command=lambda: self.add_player(parent))
        self.add_btn.pack(side="bottom")

    def add_player(self,parent):
        name = self.name.get()
        add_player(player_name=name)
        parent.name_stack.append(name)
        parent.update_ladder()
        self.destroy()


if __name__ == "__main__":
    pass