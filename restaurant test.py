from tkinter import *
import pickle
from restaurant import *
from hotel import *

accounts = {}

class TravelguideApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('TravelguideApp')
        self.geometry('250x300')
        container = Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        menubbar = Menu(container)
        account_menu = Menu(menubbar, tearoff=0)
        account_menu.add_command(label="Log Out", command=lambda: logout())
        account_menu.add_separator()
        account_menu.add_command(label="Quit", command=lambda: exit())
        menubbar.add_cascade(label="Account", menu=account_menu)
        Tk.config(self, menu=menubbar)

        def logout():
            self.show_frame(LoginPage)

        def exit():
            quit()

        self.frames = {}
        for F in (main_page,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))


        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
