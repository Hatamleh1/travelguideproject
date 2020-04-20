import tkinter as tk
from tkinter import *

hotels_r = dict()

root = Tk()
root.geometry('350x500')


label = Label(root, text="Find hotels and their ratings.", bg="light grey")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

o1 = tk.Entry(root, width=9, highlightbackground='light grey')
hotels_r['Wellington'] = list()

def display():
    r = hotels_r['Wellington']
    if o1.get() == '5' or o1.get() == '4' or o1.get() == '3' or o1.get() == '2' or o1.get() == '1':
        r.append(int(o1.get()))
        average = sum(r)/len(r)
        average = round(average, 1)
        tk.Label(root, text=average).place(relx=0.82, rely=0.35, anchor=W)



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