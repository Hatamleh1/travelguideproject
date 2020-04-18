import tkinter as tk
from tkinter import *
import pickle

accounts = {}

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('500x350')
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.pack(side='top')

        self.frames = {}
        for F in (login, signup):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=(N, S, E, W))

        self.show_frame(login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class login(tk.Frame):
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

        signupBtn = Button(self, text='Sign Up', highlightbackground='light grey', command=lambda: controller.show_frame(signup))
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

class signup(tk.Frame):
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

        cancelBtn = Button(self, text='Cancel', command=lambda: controller.show_frame(login), highlightbackground='light grey')
        cancelBtn.place(relx=0.56, rely=0.8, anchor=CENTER)


        def FSSignup():
            accounts[new_userEnt.get()] = new_passEnt.get()
            download = open('accounts.pickle', 'wb')
            pickle.dump(accounts, download)
            download.close()



app = TravelguideApp()
app.mainloop()
