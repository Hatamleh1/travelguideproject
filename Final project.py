import tkinter as tk
from tkinter import *

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
<<<<<<< HEAD
<<<<<<< Updated upstream
        self.geometry('500x350')
        container = tk.Frame(self)

=======

        container = tk.Frame(self)
>>>>>>> Stashed changes

=======
        self.geometry('400x250')
        container = tk.Frame(self)

>>>>>>> master
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
<<<<<<< Updated upstream
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", bg='white')
<<<<<<< HEAD
        label.place(relx=0.2, rely=0.3, anchor=CENTER)
=======
        root = tk.Frame.__init__(self, parent)
        label = tk.Label(root, text="Main Page", bg='white')
        label.pack(side="top", fill="both", expand=True)
>>>>>>> Stashed changes
=======
        label.pack()
>>>>>>> master

        country_choice = StringVar(root)
        choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
        country_choice.set('Select country')
<<<<<<< Updated upstream
        popupMenu = OptionMenu(label, country_choice, *choices)
        Label(label, text="Choose a country").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)
        B1 = Button(label, text="Continue", command=lambda: controller.show_frame(Page2))
        B1.grid(row=3, column=1)

=======
        popupMenu = OptionMenu(root, country_choice, *choices)
        Label(root, text="Choose a country").place(x=50, rely=10, anchor=CENTER)
        popupMenu.place(x=50, y=50, anchor=CENTER)
        B1 = Button(root, text="Continue", command=lambda: controller.show_frame(Page2))
        B1.place(x=50, y=90, anchor=CENTER)
>>>>>>> Stashed changes

class Page2(tk.Frame):
    def __init__(self, parent, controller):
<<<<<<< HEAD
        root = tk.Frame.__init__(self, parent)
        label = tk.Label(root, text="Page 2", bg='white')
=======
        root2 = tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
>>>>>>> master
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

