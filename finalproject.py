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
        for F in (main_page, Holland, germany, UK, france, LoginPage, SignupPage, About_holland, Best_visit, Currency, Electricity, Transport, City, Amsterdam_nav, Gudie_info_ams, Hotels_ams, Restaurants_ams, Sightseeing_ams, Activities_ams,
                  Rotterdam_nav, Gudie_info_rot, Hotels_rot, Restaurants_rot, Sightseeing_rot, Activities_rot):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))


        self.show_frame(LoginPage)

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
                controller.show_frame(main_page)

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
        new_userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
        new_userEnt = Entry(self, text='', highlightbackground='light grey')
        new_userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)
        new_userEnt.lower()

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
            controller.show_frame(LoginPage)



# This is the first page, choosing a country.
class main_page(Frame):
   def __init__(self, parent, controller):
       Frame.__init__(self, parent, bg='light grey', width=500, height=500)
       label = Label(self, text="Welcome to Trippy \n\n We will give you all the advice you \n need before and during your trip. \n\n Select you country below.", bg="light grey")
       label.place(relx=0.5, rely=0.4, anchor=CENTER)


       def option_changed(*args):
           c = variable.get()
           if c == 'Holland':
               controller.show_frame(Holland)
           # elif c == 'Spain':
           #     controller.show_frame(spain)
           # elif c == 'Germany':
           #     controller.show_frame(germany)
           # elif c == 'UK':
           #     controller.show_frame(UK)
           # elif c == 'France':
           #     controller.show_frame(france)

       variable = StringVar(self)
       variable.set("Select country") # default value
       variable.trace("w", option_changed)
       w = OptionMenu(self, variable, 'Holland')
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

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.23, rely=0.9, anchor=CENTER)


# Page about Holland
class About_holland(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get all information \n about Holland needed before \n your trip to Holland.", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Best time to visit.
class Best_visit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can read about the best \n time of the year to visit Holland", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Transportation information about Holland.
class Transport(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get information about \n Hollands pubic transportation", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Currency information about Holland.
class Currency(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="What currency does Holland have? \n Here you can find out. ", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Electricity information about Holland.
class Electricity(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Holland has this typ of electricity.", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

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
                controller.show_frame(spain)
            elif c == 'Rotterdam':
                controller.show_frame(Rotterdam_nav)
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

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Navigational page of Amsterdam.
class Amsterdam_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(Gudie_info_ams), width=20, highlightbackground='light grey')
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



class Gudie_info_ams(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information about Amsterdam.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class Hotels_ams(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.hotel_dict = {}
        try:
            file = open('hotel_dict', 'rb')
            self.hotel_dict = pickle.load(file)
        except:
            print('error')

        self.rating_fields = []
        self.rating_labels = []
        self.city = "Amsterdam"
        for i, h in enumerate(self.hotel_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name).grid(row=i, column=0, pady=(padding, 5))
            self.rating_fields.append(Entry(self))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating()))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=len(self.hotel_dict[self.city]), column=1)
        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

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


        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Restaurants_ams(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.restaurant_dict = {}
        try:
            file = open('restaurant_dict', 'rb')
            self.restaurant_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Amsterdam"
        for i, h in enumerate(self.restaurant_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name).grid(row=i, column=0, pady=(padding, 5))
            self.rating_fields.append(Entry(self))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating()))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        submit_button = Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=len(self.restaurant_dict[self.city]), column=1)
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
        label = Label(self, text="Excited to go on some sightseeing. \n Anne franks museum is rated highly \n so don't miss it.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_ams(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find the most interesting activities \n to do in Amsterdam. ", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)




# Navigational page of Amsterdam.
class Rotterdam_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)


        B1 = Button(self, text='Guide information', command=lambda: controller.show_frame(Gudie_info_rot), width=20, highlightbackground='light grey')
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



class Gudie_info_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information about Amsterdam.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class Hotels_rot(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.hotel_dict = {}
        try:
            file = open('hotel_dict', 'rb')
            self.hotel_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Rotterdam"
        for i, h in enumerate(self.hotel_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name).grid(row=i, column=0, pady=(padding, 5))
            self.rating_fields.append(Entry(self))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating()))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

        back_button = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav))
        back_button.grid(row=len(self.hotel_dict[self.city]), column=1)

        submit_button = Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=len(self.hotel_dict[self.city]), column=1)
        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

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
        super().__init__(parent, controller)
        self.restaurant_dict = {}
        try:
            file = open('restaurant_dict', 'rb')
            self.restaurant_dict = pickle.load(file)

        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        self.city = "Amsterdam"
        for i, h in enumerate(self.restaurant_dict[self.city]):
            padding = 5
            if i == 0:
                padding = 50
            Label(self, text=h.name).grid(row=i, column=0, pady=(padding, 5))
            self.rating_fields.append(Entry(self))
            self.rating_fields[-1].grid(row=i, column=1, pady=(padding, 5))
            self.rating_labels.append(Label(self, text=h.get_average_rating()))
            self.rating_labels[-1].grid(row=i, column=2, pady=(padding, 5))

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

        submit_button = Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=len(self.restaurant_dict[self.city]), column=1)

        back_button = Button(self, text='Submit', command=lambda: controller.show_frame(Rotterdam_nav))
        back_button.grid(row=len(self.restaurant_dict[self.city]), column=1)
        # self.img = PhotoImage(file = 'oval.gif')
        # image_button = Button(self, image=self.img, height=300, width=400)
        # image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

class Sightseeing_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on some sightseeing. \n Laith Mathilda is rated highly \n so don't miss it.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find the most interesting activities \n to do in Rotterdam. ", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class germany(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page 4", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class UK(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page 5", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)




class france(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page 6", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



# call and run code
app = TravelguideApp()
app.mainloop()
