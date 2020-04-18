import tkinter as tk
from tkinter import *


class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('250x300')
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        self.frames = {}
        for F in (Page1, Page2, Page3, Page4, Page5, Page6, LoginPage, about_holland, best_visit, currency, electricity, transport, city, amsterdam_nav):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
       label = Label(self, text="Welcome to Trippy \n\n We will give you all the advice you \n need before and during your trip. \n\n Select you country below.", bg="light grey")
       label.place(relx=0.5, rely=0.4, anchor=CENTER)

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
       w.config(bg="light grey")
       w.place(relx=0.5, rely=0.7, anchor=CENTER)

       logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage))
       logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey')
        label = tk.Label(self, text="\n Here we provide general \n information regarding the \n country you are travelling to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='About the country', command=lambda: controller.show_frame(about_holland), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Best time to visit', command=lambda: controller.show_frame(best_visit), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Public transportation', command=lambda: controller.show_frame(transport), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Currency', command=lambda: controller.show_frame(currency), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Type of electricity', command=lambda: controller.show_frame(electricity), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        B6 = Button(self, text='Cities', command=lambda: controller.show_frame(city), width = 20, highlightbackground='light grey')
        B6.place(relx=0.5, rely=0.8, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page1), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.23, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.76, rely=0.9, anchor=CENTER)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 3", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page1), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 4", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page1), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 5", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page1), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 6", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page1), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class about_holland(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="About Holland", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class best_visit(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Best time to visit", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class transport(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Public transportation", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class currency(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Currency", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class electricity(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Electricity", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class city(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Select the city you are visiting \n and we will show you our advice.", bg='light grey')
        label.place(relx=0.5, rely=0.35, anchor=CENTER)

        def option_changed(*args):
            c = variable.get()
            if c == 'Amsterdam':
                controller.show_frame(amsterdam_nav)
            elif c == 'Haag':
                controller.show_frame(Page3)
            elif c == 'Rotterdam':
                controller.show_frame(Page4)
            elif c == 'Utrecht':
                controller.show_frame(Page5)
            elif c == 'Best':
                controller.show_frame(Page6)

        variable = StringVar(self)
        variable.set("Select city") # default value
        variable.trace("w", option_changed)
        w = OptionMenu(self, variable, 'Amsterdam', 'Haag', 'Rotterdam', 'Utrecht', 'Best')
        w.config(bg="light grey")
        w.place(relx=0.5, rely=0.55, anchor=CENTER)


        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Page2), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)

class amsterdam_nav(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey')
        label = tk.Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(about_holland), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Hotels', command=lambda: controller.show_frame(best_visit), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Restaurants', command=lambda: controller.show_frame(transport), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Sightseeing', command=lambda: controller.show_frame(currency), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Activites', command=lambda: controller.show_frame(electricity), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)



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
