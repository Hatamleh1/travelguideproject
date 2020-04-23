import tkinter as tk
from tkinter import *
import pickle
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
        for F in (Main_page, Spain, UK, France, Germany, Holland, LoginPage, SignupPage, About_holland, Best_visit, Currency, Electricity, Transport, City,
                  Amsterdam_nav, Guide_info_ams, Hotels_ams, Restaurants_ams, Sightseeing_ams, Activities_ams,
                  Haag_nav, Guide_info_haag, Hotels_haag, Restaurants_haag, Sightseeing_haag, Activities_haag,
                  Rotterdam_nav, Guide_info_rot, Hotels_rot, Restaurants_rot, Sightseeing_rot, Activities_rot):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))


        self.show_frame(Holland)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# This code runs the pages, places root and shows different frames.


# This is our login function.
# The page of login

class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)

        userLbl = Label(self, text="Username:", bg='light grey')
        userLbl.place(relx=0.5, rely=0.3, anchor=CENTER)
        userEnt = Entry(self, text='', highlightbackground='light grey')
        userEnt.place(relx=0.5, rely=0.4, anchor=CENTER)

        passLbl = Label(self, text="Password:", bg='light grey')
        passLbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        passEnt = Entry(self, text='', show='*', highlightbackground='light grey')
        passEnt.place(relx=0.5, rely=0.6, anchor=CENTER)

        loginBtn = Button(self, text="Login", command=lambda:CheckLogin(), highlightbackground='light grey')
        loginBtn.place(relx=0.7, rely=0.72, anchor=CENTER, width=80)

        signupBtn = Button(self, text='Sign Up', highlightbackground='light grey', command=lambda: controller.show_frame(SignupPage))
        signupBtn.place(relx=0.3, rely=0.72, anchor=CENTER, width=80)


        # Checks if login is correct.
        def CheckLogin():
            upload = open('accounts.pickle', 'rb')
            accounts = pickle.load(upload)

            if userEnt.get() in accounts and accounts[userEnt.get()] == passEnt.get() and accounts[userEnt.get()] != '':
                controller.show_frame(Main_page)

            else:
                incorrect = Label(self, text='Username or password is incorrect. ', bg='light grey')
                incorrect.place(relx=0.5, rely=0.85, anchor=CENTER)


# Creates signup page.

class SignupPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        global new_passEnt
        global new_userEnt

        new_userLbl = Label(self, text="Create Username:", bg='light grey')
        new_userLbl.place(relx=0.5, rely=0.3, anchor=CENTER)
        new_userEnt = Entry(self, text='', highlightbackground='light grey')
        new_userEnt.place(relx=0.5, rely=0.4, anchor=CENTER)

        new_passLbl = Label(self, text="Create Password:", bg='light grey')
        new_passLbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        new_passEnt = Entry(self, text='', show='*', highlightbackground='light grey')
        new_passEnt.place(relx=0.5, rely=0.6, anchor=CENTER)

        submitBtn = Button(self, text='Submit', command=lambda: FSSignup(), highlightbackground='light grey')
        submitBtn.place(relx=0.7, rely=0.72, anchor=CENTER, width=80)

        cancelBtn = Button(self, text='Cancel', command=lambda: controller.show_frame(LoginPage), highlightbackground='light grey')
        cancelBtn.place(relx=0.3, rely=0.72, anchor=CENTER, width=80)


        def FSSignup():
            accounts[new_userEnt.get()] = new_passEnt.get()
            download = open('accounts.pickle', 'wb')
            pickle.dump(accounts, download)
            download.close()
            controller.show_frame(LoginPage)



# This is the first page, choosing a country.

class Main_page(Frame):
   def __init__(self, parent, controller):
       Frame.__init__(self, parent, bg='light grey', width=500, height=500)
       label = Label(self, text="Welcome to Trippy \n\n We will give you all the advice you \n need before and during your trip. \n\n Select you country below.", bg="light grey")
       label.place(relx=0.5, rely=0.4, anchor=CENTER)


       def option_changed(*args):
           c = variable.get()
           if c == 'Holland':
               controller.show_frame(Holland)
           elif c == 'Spain':
               controller.show_frame(Spain)
           elif c == 'Germany':
               controller.show_frame(Germany)
           elif c == 'UK':
               controller.show_frame(UK)
           elif c == 'France':
               controller.show_frame(France)

       variable = StringVar(self)
       variable.set("Select country") # default value
       variable.trace("w", option_changed)
       w = OptionMenu(self, variable, 'Holland', 'Spain', 'Germany', 'UK', 'France')
       w.config(bg="light grey")
       w.place(relx=0.5, rely=0.7, anchor=CENTER)


# Holland code.
# Buttons for Holland.

class Holland(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n Here we provide general \n information regarding the \n country you are travelling to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        B1 = Button(self, text='About the country', command=lambda: controller.show_frame(About_holland), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Best time to visit', command=lambda: controller.show_frame(Best_visit), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Public transportation', command=lambda: controller.show_frame(Transport), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Currency', command=lambda: controller.show_frame(Currency), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Type of electricity', command=lambda: controller.show_frame(Electricity), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        B6 = Button(self, text='Cities', command=lambda: controller.show_frame(City), width = 20, highlightbackground='light grey')
        B6.place(relx=0.5, rely=0.8, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.23, rely=0.9, anchor=CENTER)


class About_holland(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get all information \n about Holland needed before \n your trip to Holland:", bg='light grey')
        label.pack(side='top', expand=True)

        about = Label(self, text="The Netherlands, a country in northwestern Europe, is known for a flat landscape of"
                                 "canals, tulip fields, windmills and cycling routes. Amsterdam, the capital, is home to"
                                 "the Rijksmuseum, Van Gogh Museum and the house where Jewish diarist Anne Frank hid during WWII.", bg='light grey', anchor='e', width=24, wraplength=200, justify=LEFT)
        about.pack(side="top", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.pack(side="top", expand=True)

# Best time to visit.
class Best_visit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can read about the best \n time of the year to visit Holland:", bg='light grey', anchor='w')
        label.place(relx=0.1, rely=0.2)

        visit = Label(self, text="The best time weather wise is from mid April to mid October. July and August are the peak months for visitors.", bg="light gray", anchor='w', width=23, wraplength=200, justify=LEFT )
        visit.place(relx=0.1, rely=0.4)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Transportation information about Holland.
class Transport(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get information about \n Hollands pubic transportation", bg='light grey')
        label.place(relx=0.1, rely=0.1)

        trans = Label(self, text="The Netherlands have an extensive public transport network, which makes in easy to travel around the country. "
                                 "Staying in Amsterdam, you might use GVB trams, buses, metro and ferries, while when you travel to other cities "
                                 "and destinations, you will definitely need to take a train.", bg='light grey', width=24, wraplength=200, justify=LEFT)
        trans.place(relx=0.1, rely=0.25)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Currency information about Holland.
class Currency(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="What currency does Holland have? \n Here you can find out. ", bg='light grey')
        label.place(relx=0.1, rely=0.1)

        cur = Label(self, text='The oficial currency of the Netherlands is Euro', bg='light grey', width=24, wraplength=200, justify=LEFT)
        cur.place(relx=0.1, rely=0.4)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Electricity information about Holland.
class Electricity(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Holland has this typ of electricity.", bg='light grey')
        label.place(relx=0.05, rely=0.1)

        elec = Label(self, text="For the Netherlands there are two associated plug types, types C and F. "
                                "Plug type C is the plug which has two round pins and plug type F is the plug which has "
                                "two round pins with two earth clips on the side.", bg="light gray", width=24, wraplength=200, justify=LEFT)
        elec.place(relx=0.1, rely=0.3)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# This is the page where you can pick any city in Holland.
class City(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Select the city you are visiting \n and we will show you our advice.", bg='light grey')
        label.place(relx=0.5, rely=0.35, anchor=CENTER)

        def option_changed(*args):
            c = variable.get()
            if c == 'Amsterdam':
                controller.show_frame(Amsterdam_nav)
            elif c == 'Haag':
                controller.show_frame(Haag_nav)
            elif c == 'Rotterdam':
                controller.show_frame(Rotterdam_nav)


        variable = StringVar(self)
        variable.set("Select city") # default value
        variable.trace("w", option_changed)
        w = OptionMenu(self, variable, 'Amsterdam', 'Haag', 'Rotterdam')
        w.config(bg="light grey")
        w.place(relx=0.5, rely=0.55, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

# -------------------------------- Amsterdam --------------------------------
# Navigational page of Amsterdam.
class Amsterdam_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(Guide_info_ams), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Hotels', command=lambda: controller.show_frame(Hotels_ams), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Restaurants', command=lambda: controller.show_frame(Restaurants_ams), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Sightseeing', command=lambda: controller.show_frame(Sightseeing_ams), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Activities', command=lambda: controller.show_frame(Activities_ams), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(City), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Guide_info_ams(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information about Amsterdam:", bg="light grey", font=("Ariel", 13))
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="Amsterdam is one of the greatest small cities in the world. From Amsterdam canals to world-famous Amsterdam museums and historical Amsterdam sights,"
                                 "it is one of the most romantic and beautiful cities in Europe. Canal cruises are a popular way to see the city "
                                 "from the perspective of its canals.", bg="light grey", font=("Ariel", 13), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Hotels_ams(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.hotel_dict = {}
        try:
            file = open('hotel_dict', 'rb')
            self.hotel_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Amsterdam"
        headline = Label(self, text='Rate hotels from 1 to 5.\n\n', font=("Ariel", 15), bg='light grey')
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.hotel_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, anchor='e', width=15, font=("Ariel", 12), bg='light grey').grid(row=i, column=0, pady=(padding, 5), padx=3)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(), font=("Ariel", 12), bg='light grey'))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.hotel_dict[self.city]), column=1)
        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)
        back_Btn = Button(self, text="Back", highlightbackground='light grey', command=lambda: controller.show_frame(Amsterdam_nav))
        back_Btn.grid(row=len(self.hotel_dict[self.city]), column=0)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.hotel_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.hotel_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('hotel_dict', 'wb')
            pickle.dump(self.hotel_dict, file)
        except:
            print('error')


class Restaurants_ams(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.restaurant_dict = {}
        try:
            file = open('restaurant_dict', 'rb')
            self.restaurant_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Amsterdam"
        headline = Label(self, text='Rate restaurant from 1 to 5.\n\n', bg='light grey', font=("Ariel", 15))
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.restaurant_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, bg='light grey', anchor='e', width=15, font=("Ariel", 12)).grid(row=i, column=0, pady=(padding, 5), padx=5)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(),font=("Ariel", 12), bg='light grey'))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.restaurant_dict[self.city]), column=1)

        back_Btn = Button(self, text="Back", command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey')
        back_Btn.grid(row=len(self.restaurant_dict[self.city]), column=0)

        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.restaurant_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.restaurant_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('restaurant_dict', 'wb')
            pickle.dump(self.restaurant_dict, file)
        except:
            print('error')

class Sightseeing_ams(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on some sightseeing?", bg="light grey",  font=("Ariel", 12))
        label.place(relx=0.5, rely=0.08, anchor=CENTER)
        label = Label(self, text="One of Amsterdam's most popular attractions - and certainly its most important art repository - the Rijksmuseum (National Museum) was founded in 1798 to house the country's huge collection of rare art and antiquities. The museum's impressive collection includes a million cultural artifacts dating from the 13th century to the modern day, among them more than 8,000 important paintings spread across 250 rooms of this sprawling building.", bg="light grey",  font=("Ariel", 12), anchor='e', width=24, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.13)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_ams(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Activities to do in Amsterdam. ", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)
        label = Label(self, text="Often cited as Amsterdam’s most charming neighbourhood, wandering into the Jordaan feels like stepping back in time. Originally a working-class area, the Jordaan’s narrow streets and quaint buildings now make up one of Amsterdam’s most desirable quarters, dotted with independent art galleries, antique shops, courtyard gardens and atmospheric bars and restaurants.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)


        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

# ______________________________ Rotterdam ____________________________

class Rotterdam_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(Guide_info_rot), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Hotels', command=lambda: controller.show_frame(Hotels_rot), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Restaurants', command=lambda: controller.show_frame(Restaurants_rot), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Sightseeing', command=lambda: controller.show_frame(Sightseeing_rot), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Activities', command=lambda: controller.show_frame(Activities_rot), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(City), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

class Guide_info_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information Rotterdam.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="At Rotterdam Tourist Information you will find all the information you need to plan your visit to Rotterdam including brochures about Rotterdam, the Rotterdam Tourist Information app and practical information.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Hotels_rot(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.hotel_dict = {}
        try:
            file = open('hotel_dict', 'rb')
            self.hotel_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Rotterdam"
        headline = Label(self, text='Rate hotels from 1 to 5.\n\n', bg='light grey', font=("Ariel", 15))
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.hotel_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, bg='light grey', anchor='e', width=15, font=("Ariel", 12)).grid(row=i, column=0, pady=(padding, 5),  padx=5)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(), bg='light grey', font=("Ariel", 12)))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.hotel_dict[self.city]), column=1)

        back_Btn = Button(self, text="Back", command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey')
        back_Btn.grid(row=len(self.hotel_dict[self.city]), column=0)

        #self.img = PhotoImage(file = 'oval.gif')
        #image_button = Button(self, image=self.img, height=300, width=400)
        #image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.hotel_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.hotel_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('hotel_dict', 'wb')
            pickle.dump(self.hotel_dict, file)
        except:
            print('error')

class Restaurants_rot(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.restaurant_dict = {}
        try:
            file = open('restaurant_dict', 'rb')
            self.restaurant_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Rotterdam"
        headline = Label(self, text='Rate restaurant from 1 to 5.\n\n', bg='light grey', font=('Ariel', 15))
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.restaurant_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, bg='light grey', anchor='e', width=15, font=("Ariel", 12)).grid(row=i, column=0, pady=(padding, 5), padx=5)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(), bg='light grey', font=('Ariel', 12)))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.restaurant_dict[self.city]), column=1)

        back_Btn = Button(self, text="Back", command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey')
        back_Btn.grid(row=len(self.restaurant_dict[self.city]), column=0)


        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.restaurant_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.restaurant_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('restaurant_dict', 'wb')
            pickle.dump(self.restaurant_dict, file)
        except:
            print('error')


        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)


class Sightseeing_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on sightseeing?", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="The second largest city in the Netherlands, Rotterdam lies on both banks of the Nieuwe Maas, the tidal southern arm of the Rhine, where it's joined by the little River Rotte. It's also the world's largest port, home to the massive Europoort facility through which so much freight passes on its way to and from the continent.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)

        label = Label(self, text="Activities to do in Rotterdam. ", bg="light grey", font=("Ariel", 12))
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="A short walk from here is Maritime Museum Rotterdam. Established in 1873, the museum provides a fascinating look into the city's connection to the sea and its many waterways. Its large collections cover the history of shipping and seafaring, including ship models, a reconstruction of a 2,000-year-old vessel, and numerous seafaring paintings. ", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# -------------------------------- The Hague --------------------------------

class Haag_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(Guide_info_haag), width=20, highlightbackground='light grey')
        B1.place(relx=0.5, rely=0.3, anchor=CENTER)

        B2 = Button(self, text='Hotels', command=lambda: controller.show_frame(Hotels_haag), width=20, highlightbackground='light grey')
        B2.place(relx=0.5, rely=0.4, anchor=CENTER)

        B3 = Button(self, text='Restaurants', command=lambda: controller.show_frame(Restaurants_haag), width=20, highlightbackground='light grey')
        B3.place(relx=0.5, rely=0.5, anchor=CENTER)

        B4 = Button(self, text='Sightseeing', command=lambda: controller.show_frame(Sightseeing_haag), width=20, highlightbackground='light grey')
        B4.place(relx=0.5, rely=0.6, anchor=CENTER)

        B5 = Button(self, text='Activities', command=lambda: controller.show_frame(Activities_haag), width=20, highlightbackground='light grey')
        B5.place(relx=0.5, rely=0.7, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(City), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Guide_info_haag(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information about Haag.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="The Hague is the only big city with a beach directly on the North Sea coast. The city boasts many monuments, chic hotels, and a political heart. The government of Holland is run from the historic Binnenhof and the King’s office palace can be found on the Noordeinde. You can visit beautiful art museums and a day of high-end shopping.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Haag_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Hotels_haag(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.hotel_dict = {}
        try:
            file = open('hotel_dict', 'rb')
            self.hotel_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Haag"
        headline = Label(self, text='Rate hotels from 1 to 5.\n\n', bg='light grey', font=("Ariel", 15))
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.hotel_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, bg='light grey', anchor='e', width=12, font=("Ariel", 12)).grid(row=i, column=0, pady=(padding, 5), padx=15)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(), bg='light grey', font=("Ariel", 12)))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.hotel_dict[self.city]), column=1)

        back_Btn = Button(self, text="Back", command=lambda: controller.show_frame(Haag_nav), highlightbackground='light grey')
        back_Btn.grid(row=len(self.hotel_dict[self.city]), column=0)

        #self.img = PhotoImage(file = 'oval.gif')
        #image_button = Button(self, image=self.img, height=300, width=400)
        #image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.hotel_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.hotel_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('hotel_dict', 'wb')
            pickle.dump(self.hotel_dict, file)
        except:
            print('error')

class Restaurants_haag(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='light grey')
        self.restaurant_dict = {}
        try:
            file = open('restaurant_dict', 'rb')
            self.restaurant_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Haag"
        headline = Label(self, text='Rate restaurant from 1 to 5.\n\n', bg='light grey', font=("Ariel", 15))
        headline.grid(row=0, column=0, columnspan=3)
        for i, h in enumerate(self.restaurant_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name, bg='light grey', anchor='e', width=12, font=("Ariel", 12)).grid(row=i, column=0, pady=(padding, 5), padx=15)
            self.rating_fields.append(Entry(self, highlightbackground='light grey', width=8))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating(), bg='light grey', font=("Ariel", 12)))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit, highlightbackground='light grey')
        submit_button.grid(row=len(self.restaurant_dict[self.city]), column=1)

        back_Btn = Button(self, text="Back", command=lambda: controller.show_frame(Haag_nav), highlightbackground='light grey')
        back_Btn.grid(row=len(self.restaurant_dict[self.city]), column=0)


    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.restaurant_dict[self.city]):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.restaurant_dict[self.city]):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file = open('restaurant_dict', 'wb')
            pickle.dump(self.restaurant_dict, file)
        except:
            print('error')

        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

class Sightseeing_haag(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on sightseeing?", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="In the center of the oldest section of The Hague is the Binnenhof - the Inner Court - an irregular group of buildings constructed around a large central courtyard. With its origins dating back to 1250 and tied to the building of a castle, it soon became the residence of the ruling aristocracy, and today houses both chambers of Parliament.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Haag_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_haag(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Activities to do in Haag. ", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="Housed in a specially made rotunda, Panorama Mesdag is a gigantic painting measuring 120 meters in length and 14 meters in height that was painted by HW Mesdag and his wife, Sientje Mesdag-Van Houten, along with other artists of the Hague School.", bg="light grey", font=("Ariel", 12), anchor='e', width=25, wraplength=200, justify=LEFT)
        label.place(relx=0.1, rely=0.2)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Haag_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

# _____________________________ Coming Soon countries ________________________________


class Spain(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Coming soon", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Germany(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Coming soon", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class UK(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Coming soon", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class France(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Coming soon", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# call and run code
app = TravelguideApp()
app.mainloop()
