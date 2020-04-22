from hotel import *
import pickle

file2 = open('hotel_dict', 'wb')

r = {"Amsterdam": [Hotel("Rotterdam1 Hotel"), Hotel("Rotterdam2 Hotel"), Hotel("Rotterdam3 Hotel"), Hotel("Rotterdam4 Hotel")],
     "Barcelona": [Hotel("W Hotel")]}



pickle.dump(r, file2)
file2.close()

