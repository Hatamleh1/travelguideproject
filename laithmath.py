from tkinter import *
import pickle
from hotel import *


hotels_r = {}
hotels_dict = {}

class TravelguideApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('TravelguideApp')
        self.geometry('250x300')
        container = Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        self.frames = {}
        for F in (hotels,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(hotels)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class hotels(Frame):
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
        self.img = PhotoImage(file = 'oval.gif')
        image_button = Button(self, image=self.img, height=300, width=400)
        image_button.grid(row=len(self.hotel_dict[self.city]), column=2)

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



app = TravelguideApp()
app.mainloop()
