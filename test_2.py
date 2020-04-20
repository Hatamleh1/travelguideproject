import tkinter as tk
from tkinter import *
import pickle

<<<<<<< HEAD
root = Tk()
root.geometry('350x500')


label = Label(root, text="Find hotels and their ratings.", bg="light grey")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

o1 = tk.Entry(root, width=9, highlightbackground='light grey')


def write_data(ratings, data):
    f = open(ratings, 'w')
    for element in data:
        f.write(': '.join(element) + '\n')
    f.close()


def read_data(ratings):
    rate = []
    f = open(ratings)
    for line in f:
        rate.append(line.strip().split(': '))
    f.close()
    return rate


def display():
    countries_ = read_data('Ratings')
    for line in countries_:
        if line[0] == 'Holland' and o1.get() == '5':
            line[1] = str(int(line[1]) + 5)
            write_data('Ratings', countries_)
        elif line[0] == 'Holland' and o1.get() == "4":
            line[1] = str(int(line[1]) + 4)
            write_data('Ratings', countries_)
        elif line[0] == 'Holland' and o1.get() == "3":
            line[1] = str(int(line[1]) + 3)
            write_data('Ratings', countries_)
        elif line[0] == 'Holland' and o1.get() == "2":
            line[1] = str(int(line[1]) + 2)
            write_data('Ratings', countries_)
        elif line[0] == 'Holland' and o1.get() == "1":
            line[1] = str(int(line[1]) + 1)
            write_data('Ratings', countries_)
        else:
            pass


tk.Label(root, text="Hotels", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.03, rely=0.25, anchor=W)
tk.Label(root, text="Wellington", bg='light grey').place(relx=0.03, rely=0.35, anchor=W)


tk.Label(root, text="Your opinion", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.37, rely=0.25, anchor=W)
o1.place(relx=0.37, rely=0.35, anchor=W)


tk.Label(root, text="Rating", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.76, rely=0.25, anchor=W)

button1 = tk.Button(root, text="submit", command=lambda: display(), highlightbackground='light grey')
button1.place(relx=0.41, rely=0.70)

back_btn = Button(root, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

logout = Button(root, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
logout.place(relx=0.8, rely=0.9, anchor=CENTER)


root.mainloop()

=======
hotels_r = {}

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('TravelguideApp')
        self.geometry('250x300')
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        self.frames = {}
        for F in (hotels, holland):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(hotels)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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

class hotels(tk.Frame):
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

        tk.Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find hotels and their ratings.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        label = Label(self, text="Find hotels and their ratings.", bg="light grey")
        label.place(relx=0.5, rely=0.1, anchor=CENTER)

        tk.Label(self, text="Rating", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.76, rely=0.25, anchor=W)
        tk.Label(self, text="Your opinion", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.37, rely=0.25, anchor=W)



        tk.Label(self, text="Hotels", font=('Helvetica', 13, 'bold'), bg='light grey').place(relx=0.03, rely=0.25, anchor=W)
        tk.Label(self, text="Wellington", bg='light grey').place(relx=0.03, rely=0.35, anchor=W)
        tk.Label(self, text="W Hotel", bg='light grey').place(relx=0.03, rely=0.45, anchor=W)
        tk.Label(self, text="Ibis Hotel", bg='light grey').place(relx=0.03, rely=0.55, anchor=W)
        tk.Label(self, text="Yellow Hotel", bg='light grey').place(relx=0.03, rely=0.65, anchor=W)

        o1 = tk.Entry(self, width=9, highlightbackground='light grey')
        o1.place(relx=0.37, rely=0.35, anchor=W)

        o2 = tk.Entry(self, width=9, highlightbackground='light grey')
        o2.place(relx=0.37, rely=0.45, anchor=W)

        o3 = tk.Entry(self, width=9, highlightbackground='light grey')
        o3.place(relx=0.37, rely=0.55, anchor=W)

        o4 = tk.Entry(self, width=9, highlightbackground='light grey')
        o4.place(relx=0.37, rely=0.65, anchor=W)


        l1 = tk.Label(self, text='')
        if len(hotels_r['Wellington']) > 0:
            l1['text'] = sum(hotels_r['Wellington'])/len(hotels_r['Wellington'])
        l1.place(relx=0.82, rely=0.35, anchor=W)

        l2 = tk.Label(self, text='')
        if len(hotels_r['W_hotel']) > 0:
            l2['text'] = sum(hotels_r['W_hotel'])/len(hotels_r['W_hotel'])
        l2.place(relx=0.82, rely=0.35, anchor=W)

        l3 = tk.Label(self, text='')
        if len(hotels_r['Ibis_hotel']) > 0:
            l3['text'] = sum(hotels_r['Ibis_hotel'])/len(hotels_r['Ibis_hotel'])
        l3.place(relx=0.82, rely=0.35, anchor=W)

        l4 = tk.Label(self, text='')
        if len(hotels_r['Yellow_hotel']) > 0:
            l4['text'] = sum(hotels_r['Yellow_hotel'])/len(hotels_r['Yellow_hotel'])
        l4.place(relx=0.82, rely=0.35, anchor=W)

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
                tk.Label(self, text=average).place(relx=0.82, rely=0.35, anchor=W)
                l1['text'] = average
            r = hotels_r['W_hotel']
            if o2.get() == '5' or o2.get() == '4' or o2.get() == '3' or o2.get() == '2' or o2.get() == '1':
                r.append(int(o2.get()))
                average1 = round(sum(r)/len(r), 1)
                tk.Label(self, text=average1).place(relx=0.82, rely=0.45, anchor=W)
                l2['text'] = average1
            i = hotels_r['Ibis_hotel']
            if o3.get() == '5' or o3.get() == '4' or o3.get() == '3' or o3.get() == '2' or o3.get() == '1':
                i.append(int(o3.get()))
                average2 = round(sum(i)/len(i), 1)
                tk.Label(self, text=average2).place(relx=0.82, rely=0.55, anchor=W)
                l3['text'] = average2
            y = hotels_r['Yellow_hotel']
            if o4.get() == '5' or o4.get() == '4' or o4.get() == '3' or o4.get() == '2' or o4.get() == '1':
                y.append(int(o4.get()))
                average3 = round(sum(y)/len(y), 1)
                tk.Label(self, text=average3).place(relx=0.82, rely=0.65, anchor=W)
                l4['text'] = average3
            save()




        button1 = tk.Button(self, text="submit", command=submit, highlightbackground='light grey')
        button1.place(relx=0.41, rely=0.70)

        # back_btn = Button(root, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        # back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)

        logout = Button(self, text="Logout", bg='light grey', highlightbackground='light grey', command=lambda: controller.show_frame(LoginPage), width=5)
        logout.place(relx=0.8, rely=0.9, anchor=CENTER)


app = TravelguideApp()
app.mainloop()
>>>>>>> master