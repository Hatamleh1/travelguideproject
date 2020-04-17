import tkinter as tk
from tkinter import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
       tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

##### Here Laith code

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, bg='white')
       label.pack(side="top", fill="both", expand=True)

       country_choice = StringVar(root)
       choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
       country_choice.set('Select country')
       popupMenu = OptionMenu(label, country_choice, *choices)
       Label(label, text="Choose a country").place(relx=0.5, rely=0.4, anchor=CENTER)
       popupMenu.place(relx=0.5, rely=0.5, anchor=CENTER)
       B1 = Button(label, text="Continue", command=Page2)
       B1.place(relx=0.5, rely=0.6, anchor=CENTER)


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Our TripAdvisor')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

