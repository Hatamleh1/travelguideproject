from tkinter import *
import tkinter as ttk


root = Tk()
root.title("Tk dropdown example")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

country_choice = StringVar(root)

choices = {'Holland', 'Spain', 'Germany', 'UK', 'France'}
country_choice.set('Select country')

popupMenu = OptionMenu(mainframe, country_choice, *choices)
Label(mainframe, text="Choose a country").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


def change_dropdown(*args):
    print(country_choice.get())


country_choice.trace('w', change_dropdown)

change_dropdown() == ''


root.mainloop()
