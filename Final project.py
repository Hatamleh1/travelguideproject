import tkinter as tk
from tkinter import *

class TravelguideApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        container.pack(side='top')

        self.frames = {}
        for F in (Page1, Page2, Page3, LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='N S E W')

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn1 = tk.Button(self, text='Visit Page 2', command=lambda: controller.show_frame(Page2))
        Btn1.pack()

        # country_choice = StringVar(tk.Frame) #<--- This code is not working and ruining the rest
        # choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
        # country_choice.set('Select country')
        # popupMenu = OptionMenu(label, country_choice, *choices)
        # Label(label, text="Choose a country").place(relx=0.5, rely=0.4, anchor=CENTER)
        # popupMenu.place(relx=0.5, rely=0.5, anchor=CENTER)
        # B1 = Button(label, text="Continue", command=lambda: controller.show_frame(Page2))
        # B1.place(relx=0.5, rely=0.6, anchor=CENTER)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", bg='white')
        label.pack(side="top", fill="both", expand=True)

        Btn = tk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(Page1))
        Btn.pack()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userLbl = Label(self, text="Username:")
        userLbl.place(relx=0.5, rely=0.4, anchor=CENTER)
        userEnt = Entry(self, text='')
        userEnt.place(relx=0.5, rely=0.5, anchor=CENTER)

        passLbl = Label(self, text="Password:")
        passLbl.place(relx=0.5, rely=0.6, anchor=CENTER)
        passEnt = Entry(self, text='', show='*')
        passEnt.place(relx=0.5, rely=0.7, anchor=CENTER)

        loginBtn = Button(self, text="Login", command=None)
        loginBtn.place(relx=0.6, rely=0.8, anchor=CENTER)

        signupBtn = Button(self, text='Sign Up', command= controller.show_frame(Page1))
        signupBtn.place(relx=0.4, rely=0.8, anchor=CENTER)



app = TravelguideApp()
app.mainloop()


# class welcome_page:
#     root = Tk()
#     root.title("Tk dropdown example")
#

#
#
# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)
#
#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)
#
#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#
#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
#
#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")
#
#         p1.show()
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title('Our TripAdvisor')
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()
#
#     mainframe = Frame(root)
#     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#     mainframe.columnconfigure(0, weight=1)
#     mainframe.rowconfigure(0, weight=1)
#     mainframe.pack(pady=100, padx=100)
#
#     country_choice = StringVar(root)
#
#     choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
#     country_choice.set('Select country')
#
#     popupMenu = OptionMenu(mainframe, country_choice, *choices)
#     Label(mainframe, text="Choose a country:").grid(row=1, column=1)
#     popupMenu.grid(row=2, column=1)
#
#
#     root.mainloop()
