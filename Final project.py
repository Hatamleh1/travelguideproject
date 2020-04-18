import tkinter as tk
from tkinter import *

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        container.pack(side='top')

        self.frames = {}
        for F in (Page1, Page2, Page3, LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='N S E W')

        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", bg='white')
        label.pack(side="top", fill="both", expand=True)

        country_choice = StringVar()
        choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
        country_choice.set('Select country')
        popupMenu = OptionMenu(label, country_choice, *choices)
        Label(label, text="Choose a country").place(relx=0.5, rely=0.4, anchor=CENTER)
        popupMenu.place(relx=0.5, rely=0.5, anchor=CENTER)
        B1 = Button(label, text="Continue", command=lambda: controller.show_frame(Page2))
        B1.place(relx=0.5, rely=0.6, anchor=CENTER)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userLbl = Label(self, text="Username:")
        userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
        userEnt = Entry(self, text='')
        userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

        passLbl = Label(self, text="Password:")
        passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
        passEnt = Entry(self, text='', show='*')
        passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)

        loginBtn = Button(self, text="Login", command=None)
        loginBtn.place(relx=0.6, rely=0.8, anchor=CENTER)

        signupBtn = Button(self, text='Sign Up', command=controller.show_frame(Page1))
        signupBtn.place(relx=0.4, rely=0.8, anchor=CENTER)


#running code
app = TravelguideApp()
app.mainloop()


