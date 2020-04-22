import tkinter as tk
from tkinter import *


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
        self.hotel_list = []
        try:
            file2 = open('hotel_list_rot', 'rb')
            self.hotel_list = pickle.load(file2)
        except:
            print('error')
        self.rating_fields = []
        self.rating_labels = []
        for i, h in enumerate(self.hotel_list):
            Label(self, text=h.name).grid(row=i, column=0)
            self.rating_fields.append(Entry(self))
            self.rating_fields[-1].grid(row=i, column=1)
            self.rating_labels.append(Label(self, text=h.get_average_rating()))
            self.rating_labels[-1].grid(row=i, column=2)
        submit_button = Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=len(self.hotel_list), column=1)

    def update_ratings(self):
        for r, h in zip(self.rating_labels, self.hotel_list):
            r['text'] = h.get_average_rating()

    def submit(self):
        for f, h in zip(self.rating_fields, self.hotel_list):
            h.rate(f.get())
        self.update_ratings()
        self.save_to_file()

    def save_to_file(self):
        try:
            file2 = open('hotel_list_rot', 'wb')
            pickle.dump(self.hotel_list_rot, file2)
        except:
            print('error')


        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(Rotterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Restaurants_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Here you can find the best \n restaurants.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)



class Sightseeing_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Excited to go on some sightseeing. \n Laith Mathilda is rated highly \n so don't miss it.", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)


class Activities_rot(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='light grey', width=500, height=500)
        label = Label(self, text="Find the most interesting activities \n to do in Rotterdam. ", bg="light grey")
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        back_btn = Button(self, text='Back', command=lambda: controller.show_frame(amsterdam_nav), highlightbackground='light grey', width=5)
        back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)
