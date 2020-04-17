import _tkinter as tk
from tkinter import *


class Main:

    root = Tk()
    root.title("Log In Page")
    root.geometry('500x350')


    userLbl = Label(root, text="Username:")
    userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    userEnt = Entry(root, text='')
    userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

    passLbl = Label(root, text="Password:")
    passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
    passEnt = Entry(root, text='', show='*')
    passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)

    loginBtn = Button(root, text="Login", command=None)
    loginBtn.place(relx=0.6, rely=0.8, anchor=CENTER)

    signupBtn = Button(root, text='Sign Up', command=None)
    signupBtn.place(relx=0.4, rely=0.8, anchor=CENTER)

    root.mainloop()

class signup:
    window = Tk()
    window.title("Sign Up")
    window.geometry('500x350')

    new_userLbl = Label(window, text="Username:")
    new_userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    new_userEnt = Entry(root, text='')
    new_userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

    new_passLbl = Label(window, text="Password:")
    new_passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
    new_passEnt = Entry(root, text='', show='*')
    new_passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)


    submitBtn = Button(window, text='Sign Up', command=signup)
    submitBtn.place(relx=0.4, rely=0.8, anchor=CENTER)

    window.mainloop()
