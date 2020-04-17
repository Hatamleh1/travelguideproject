from tkinter import *
import tkinter as ttk
from firebase import firebase, pyerbase
from getpass import getpass

firebaseConfig = {
    "apiKey": "AIzaSyCgsTaRzssS9JsgC88uTDGoFS2TchT_kr4",
    "authDomain": "travelguideproject-3d198.firebaseapp.com",
    "databaseURL": "https://travelguideproject-3d198.firebaseio.com",
    "projectId": "travelguideproject-3d198",
    "storageBucket": "travelguideproject-3d198.appspot.com",
    "messagingSenderId": "1038280136856",
    "appId": "1:1038280136856:web:d0be96210c16ed0f6998ed",
    "measurementId": "G-SGY74C7BSY"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Email:\n")
password = getpass("Password:\n")

user = auth.create_user_with_email_and_password(email, password)




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


root.mainloop()
