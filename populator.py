from hotel import *
import pickle

file = open('hotel_dict', 'wb')

d = {"Amsterdam": [Hotel("Amsterdam1 Hotel"), Hotel("Amsterdam2 Hotel"), Hotel("Amsterdam3 Hotel"), Hotel("Amsterdam4 Hotel")],
     "Haag": [Hotel("Hague1 Hotel"), Hotel("Hague2 Hotel"), Hotel("Hague3 Hotel"), Hotel("Hague4 Hotel")],
     "Rotterdam": [Hotel("Rotterdam Hotel"), Hotel("Rotterdam2 Hotel"), Hotel("Roterdam3 Hotel"), Hotel("Rotterdam4 Hotel")],
     "Best": [Hotel("Best Hotel"), Hotel("Best2 Hotel"), Hotel("Best3 Hotel"), Hotel("Best4 Hotel")]}


pickle.dump(d, file)
file.close()

