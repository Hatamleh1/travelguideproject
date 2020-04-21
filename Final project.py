import tkinter as tk
from tkinter import *
import pickle


hotels_r = {}
accounts = {}

# This code runs the pages, places root and shows different frames.
class TravelguideApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('TravelguideApp')
        self.geometry('500x350')

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
        for F in (main_page, holland, spain, germany, UK, france, LoginPage, SignupPage, about_holland, best_visit, currency, electricity, transport, neth_city, amsterdam_nav, gudie_info, hotels, restaurants, sightseeing, activities):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# This is our login function.
# The page of login



class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)

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


        # Checks if login is correct.
        def CheckLogin():
            upload = open('accounts.pickle', 'rb')
            accounts = pickle.load(upload)

            if userEnt.get() in accounts and accounts[userEnt.get()] == passEnt.get():
                controller.show_frame(main_page)

            else:
                r = Tk()
                r.title('D:')
                r.geometry('150x50')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()

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


# Holland code.
# Buttons for Holland.

class holland(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n Here we provide general \n information regarding the \n country you are travelling to.", bg='light grey')
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

        B6 = Button(self, text='Cities', command=lambda: controller.show_frame(neth_city), width = 20, highlightbackground='light grey')
        B6.place(relx=0.5, rely=0.8, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.23, rely=0.9, anchor=CENTER)


# Page about Holland
class about_holland(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get all information \n about Holland needed before \n your trip to Holland.", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Best time to visit.
class best_visit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can read about the best \n time of the year to visit Holland", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Transportation information about Holland.
class transport(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Here you can get information about \n Hollands pubic transportation", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Currency information about Holland.
class currency(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="What currency does Holland have? \n Here you can find out. ", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# Electricity information about Holland.
class electricity(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="Holland has this typ of electricity.", bg='light grey')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(holland), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


# This is the page where you can pick any city in Holland.
<<<<<<< Updated upstream
class city(Frame):
=======
class neth_city(tk.Frame):
>>>>>>> Stashed changes
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


# Navigational page of Amsterdam.
class amsterdam_nav(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey')
        label = Label(self, text="\n What are you looking for? \n Here we provide all kinds of \n actitives, resturants to go to.", bg='light grey')
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



class gudie_info(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Guide information about Amsterdam.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class hotels(Frame):
    def __init__(self, parent, controller):
        def load():
            global hotels_r
            try:
                global hotels_r
                rate_upload = open('hotels_rating.pickle', 'rb')
                hotels_r = pickle.load(rate_upload)
            except:
                hotels_r['Wellington'] = list()
                hotels_r['W_hotel'] = list()
                hotels_r['Ibis_hotel'] = list()
                hotels_r['Yellow_hotel'] = list()
        load()

        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find hotels and their ratings.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="Find hotels and their ratings.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self, text="Rating", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.76, rely=0.25, anchor=W)
        Label(self, text="Your opinion", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.37, rely=0.25, anchor=W)

        Label(self, text="Hotels", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.03, rely=0.25, anchor=W)
        Label(self, text="Wellington", bg='light grey').place(relx=0.03, rely=0.35, anchor=W)
        Label(self, text="W Hotel", bg='light grey').place(relx=0.03, rely=0.45, anchor=W)
        Label(self, text="Ibis Hotel", bg='light grey').place(relx=0.03, rely=0.55, anchor=W)
        Label(self, text="Yellow Hotel", bg='light grey').place(relx=0.03, rely=0.65, anchor=W)

        o1 = Entry(self, width=9, highlightbackground='light grey')
        o1.place(relx=0.37, rely=0.35, anchor=W)

        o2 = Entry(self, width=9, highlightbackground='light grey')
        o2.place(relx=0.37, rely=0.45, anchor=W)

        o3 = Entry(self, width=9, highlightbackground='light grey')
        o3.place(relx=0.37, rely=0.55, anchor=W)

        o4 = Entry(self, width=9, highlightbackground='light grey')
        o4.place(relx=0.37, rely=0.65, anchor=W)


        l1 = Label(self, text='')
        if len(hotels_r['Wellington']) > 0:
            l1['text'] = round(sum(hotels_r['Wellington'])/len(hotels_r['Wellington']), 1)
        l1.place(relx=0.82, rely=0.35, anchor=W)

        l2 = Label(self, text='')
        if len(hotels_r['W_hotel']) > 0:
            l2['text'] = round(sum(hotels_r['W_hotel'])/len(hotels_r['W_hotel']), 1)
        l2.place(relx=0.82, rely=0.45, anchor=W)

        l3 = Label(self, text='')
        if len(hotels_r['Ibis_hotel']) > 0:
            l3['text'] = round(sum(hotels_r['Ibis_hotel'])/len(hotels_r['Ibis_hotel']), 1)
        l3.place(relx=0.82, rely=0.55, anchor=W)

        l4 = Label(self, text='')
        if len(hotels_r['Yellow_hotel']) > 0:
            l4['text'] = round(sum(hotels_r['Yellow_hotel'])/len(hotels_r['Yellow_hotel']), 1)
        l4.place(relx=0.82, rely=0.65, anchor=W)

        def save():
            rate_download = open('hotels_rating.pickle', 'wb')
            pickle.dump(hotels_r, rate_download)
            rate_download.close()

        def submit():
            global hotels_r
            w = hotels_r['Wellington']
            if o1.get() == '5' or o1.get() == '4' or o1.get() == '3' or o1.get() == '2' or o1.get() == '1':
                w.append(int(o1.get()))
                average = round(sum(w)/len(w), 1)
                l1['text'] = average
            r = hotels_r['W_hotel']
            if o2.get() == '5' or o2.get() == '4' or o2.get() == '3' or o2.get() == '2' or o2.get() == '1':
                r.append(int(o2.get()))
                average1 = round(sum(r)/len(r), 1)
                l2['text'] = average1
            i = hotels_r['Ibis_hotel']
            if o3.get() == '5' or o3.get() == '4' or o3.get() == '3' or o3.get() == '2' or o3.get() == '1':
                i.append(int(o3.get()))
                average2 = round(sum(i)/len(i), 1)
                l3['text'] = average2
            y = hotels_r['Yellow_hotel']
            if o4.get() == '5' or o4.get() == '4' or o4.get() == '3' or o4.get() == '2' or o4.get() == '1':
                y.append(int(o4.get()))
                average3 = round(sum(y)/len(y), 1)
                l4['text'] = average3
            save()


        button1 = Button(self, text="submit", command=submit, highlightbackground='light grey')
        button1.place(relx=0.41, rely=0.70)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class restaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Here you can find the best \n restaurants.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class sightseeing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on some sightseeing. \n Anne franks museum is rated highly \n so don't miss it.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class activities(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find the most interesting activities \n to do in Amsterdam. ", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)




<<<<<<< Updated upstream
class spain(Frame):
=======
class spain(tk.Frame):
>>>>>>> Stashed changes
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page 3", bg='white')
        label.pack(side="top", fill="both", expand=True)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(main_page), highlightbackground='light grey', width=5)
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
