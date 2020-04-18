import tkinter as tk
from tkinter import *

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('400x250')
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        container.pack(side='top')

        self.frames = {}
        for F in (Page1, Page2, Page3, Page4, Page5, Page6, LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       label = tk.Label(self, text="Main Page", bg='grey', height=300, width=300, padx=300, pady=300)
       label.columnconfigure(0, weight=1)
       label.rowconfigure(0, weight=1)
       label.pack()

       def option_changed(*args):
           c = variable.get()
           if c == 'Holland':
               controller.show_frame(Page2)
           elif c == 'Spain':
               controller.show_frame(Page3)
           elif c == 'Germany':
               controller.show_frame(Page4)
           elif c == 'UK':
               controller.show_frame(Page5)
           elif c == 'France':
               controller.show_frame(Page6)

       variable = StringVar(self)
       variable.set("Select country") # default value
       variable.trace("w", option_changed)
       w = OptionMenu(self, variable, 'Holland', 'Spain', 'Germany', 'UK', 'France')
       w.pack()

       B1 = Button(label, text="Logout", command=lambda: controller.show_frame(LoginPage))
       B1.grid(row=1, column=1, sticky=(N, S, E, W))


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        root2 = tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 3", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 4", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 5", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 6", bg='white')
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

