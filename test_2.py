import tkinter as tk
from tkinter import *
import pickle

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

