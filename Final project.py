import tkinter as tk
from tkinter import *
import pickle

accounts = {}

# This code runs the pages, places root and shows different frames.
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('250x300')
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        self.frames = {}
<<<<<<< Updated upstream
        for F in (main_page, holland, spain, germany, UK, france, LoginPage, about_holland, best_visit, currency, electricity, transport, city, amsterdam_nav, gudie_info, hotels, restaurants, sightseeing, activities):
=======
        for F in (main_page, holland, spain, germany, UK, france, LoginPage, SignupPage, about_holland, best_visit, currency, electricity, transport, city, amsterdam_nav, gudie_info, hotels, restaurants, sightseeing, activities):
>>>>>>> Stashed changes
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

<<<<<<< Updated upstream
        self.show_frame(main_page)
=======
        self.show_frame(LoginPage)
>>>>>>> Stashed changes

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


<<<<<<< Updated upstream
# This is the first page, choosing a country.

=======
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)


        userLbl = Label(self, text="Username:", bg='light grey')
        userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
        userEnt = Entry(self, text='', highlightbackground='light grey')
        userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

        passLbl = Label(self, text="Password:", bg='light grey')
        passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
        passEnt = Entry(self, text='', show='*', highlightbackground='light grey')
        passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)

        loginBtn = Button(self, text="Login", command=lambda:CheckLogin(), highlightbackground='light grey')
        loginBtn.place(relx=0.56, rely=0.8, anchor=CENTER)

        signupBtn = Button(self, text='Sign Up', highlightbackground='light grey', command=lambda: controller.show_frame(SignupPage))
        signupBtn.place(relx=0.4, rely=0.8, anchor=CENTER)



        def CheckLogin():
            upload = open('accounts.pickle', 'rb')
            accounts = pickle.load(upload)

            if userEnt.get() in accounts and accounts[userEnt.get()] == passEnt.get():
                controller.show_frame(main_page)
                r = Tk() # Opens new window
                r.title(':D')
                r.geometry('150x50') # Makes the window a certain size
                rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
                rlbl.pack() # Pack is like .grid(), just different
                r.mainloop()
            else:
                r = Tk()
                r.title('D:')
                r.geometry('150x50')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        global new_passEnt
        global new_userEnt

        new_userLbl = Label(self, text="Create Username:", bg='light grey')
        new_userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
        new_userEnt = Entry(self, text='', highlightbackground='light grey')
        new_userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

        new_passLbl = Label(self, text="Create Password:", bg='light grey')
        new_passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
        new_passEnt = Entry(self, text='', show='*', highlightbackground='light grey')
        new_passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)


        submitBtn = Button(self, text='Submit', command=lambda: FSSignup(), highlightbackground='light grey')
        submitBtn.place(relx=0.4, rely=0.8, anchor=CENTER)

        cancelBtn = Button(self, text='Cancel', command=lambda: controller.show_frame(LoginPage), highlightbackground='light grey')
        cancelBtn.place(relx=0.56, rely=0.8, anchor=CENTER)


        def FSSignup():
            accounts[new_userEnt.get()] = new_passEnt.get()
            download = open('accounts.pickle', 'wb')
            pickle.dump(accounts, download)
            download.close()


# This is the first page, choosing a country.
>>>>>>> Stashed changes
class main_page(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
       label = Label(self, text="Welcome to Trippy \n\n We will give you all the advice you \n need before and during your trip. \n\n Select you country below.", bg="light grey")
       label.place(relx=0.5, rely=0.4, anchor=CENTER)

       def option_changed(*args):
           c = variable.get()
           if c == 'Holland':
               controller.show_frame(holland)
           elif c == 'Spain':
               controller.show_frame(spain)
           elif c == 'Germany':
               controller.show_frame(germany)
           elif c == 'UK':
               controller.show_frame(UK)
           elif c == 'France':
               controller.show_frame(france)

       variable = StringVar(self)
       variable.set("Select country") # default value
       variable.trace("w", option_changed)
       w = OptionMenu(self, variable, 'Holland', 'Spain', 'Germany', 'UK', 'France')
       w.config(bg="light grey")
       w.place(relx=0.5, rely=0.7, anchor=CENTER)

       logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage))
       logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Holland code.
# Buttons for Holland.

class holland(tk.Frame):
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

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.23, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.76, rely=0.9, anchor=CENTER)


# Page about Holland
class about_holland(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="About Holland", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Best time to visit.
class best_visit(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Best time to visit", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Transportation information about Holland.
class transport(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Public transportation", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Currency information about Holland.
class currency(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Currency", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Electricity information about Holland.
class electricity(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Electricity", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# This is the page where you can pick any city in Holland.
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
                controller.show_frame(spain)
            elif c == 'Rotterdam':
                controller.show_frame(germany)
            elif c == 'Utrecht':
                controller.show_frame(UK)
            elif c == 'Best':
                controller.show_frame(france)

        variable = StringVar(self)
        variable.set("Select city") # default value
        variable.trace("w", option_changed)
        w = OptionMenu(self, variable, 'Amsterdam', 'Haag', 'Rotterdam', 'Utrecht', 'Best')
        w.config(bg="light grey")
        w.place(relx=0.5, rely=0.55, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


# Navigational page of Amsterdam.
class amsterdam_nav(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey')
        label = tk.Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(gudie_info), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Hotels', command=lambda: controller.show_frame(hotels), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Restaurants', command=lambda: controller.show_frame(restaurants), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Sightseeing', command=lambda: controller.show_frame(sightseeing), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Activities', command=lambda: controller.show_frame(activities), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(city), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class gudie_info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

<<<<<<< Updated upstream
        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class hotels(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Hotels", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)
        rating1 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating1.place(relx=0.75, rely=0.3, anchor=CENTER)
        rating2 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating2.place(relx=0.75, rely=0.45, anchor=CENTER)
        rating3 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating3.place(relx=0.75, rely=0.6, anchor=CENTER)
        rating4 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating4.place(relx=0.75, rely=0.75, anchor=CENTER)


class restaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Restaurants", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class sightseeing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Sightseeing", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class activities(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Activities", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

=======
>>>>>>> Stashed changes
        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class hotels(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Hotels", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

<<<<<<< Updated upstream


####################################################




class spain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 3", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
=======
        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)
        rating1 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating1.place(relx=0.75, rely=0.3, anchor=CENTER)
        rating2 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating2.place(relx=0.75, rely=0.45, anchor=CENTER)
        rating3 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating3.place(relx=0.75, rely=0.6, anchor=CENTER)
        rating4 = Scale(self, from_=0, to=5, orient=HORIZONTAL)
        rating4.place(relx=0.75, rely=0.75, anchor=CENTER)


class restaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Restaurants", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
>>>>>>> Stashed changes
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


<<<<<<< Updated upstream
class germany(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 4", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
=======
class sightseeing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Sightseeing", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
>>>>>>> Stashed changes
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


<<<<<<< Updated upstream
class UK(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 5", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
=======
class activities(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Activities", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
>>>>>>> Stashed changes
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


<<<<<<< Updated upstream
class france(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 6", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class LoginPage(tk.Frame):
=======



####################################################




class spain(tk.Frame):
>>>>>>> Stashed changes
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 3", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


<<<<<<< Updated upstream
        signupBtn = Button(self, text='Sign Up', command=controller.show_frame(main_page))
        signupBtn.place(relx=0.4, rely=0.8, anchor=CENTER)
=======
class germany(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 4", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class UK(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 5", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


class france(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 6", bg='white')
        label.pack(side="top", fill="both", expand=True)
>>>>>>> Stashed changes

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

<<<<<<< Updated upstream
=======
        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


>>>>>>> Stashed changes
#call and run code
app = TravelguideApp()
app.mainloop()



