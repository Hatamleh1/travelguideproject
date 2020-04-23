from hotel import *
import pickle

file = open('hotel_dict', 'wb')

d = {"Amsterdam": [Hotel("HOTEL V NESPLEIN"), Hotel("MOTEL ONE AMSTERDAM WATERLOOPLEIN"), Hotel("HYATT REGENCY"), Hotel("ESTHEREA")],
     "Haag": [Hotel("Hague1 Hotel"), Hotel("Hague2 Hotel"), Hotel("Hague3 Hotel"), Hotel("Hague4 Hotel")],
     "Rotterdam": [Hotel("Rotterdam Hotel"), Hotel("Rotterdam2 Hotel"), Hotel("Rotterdam3 Hotel"), Hotel("Rotterdam4 Hotel")],
     "Best": [Hotel("Best Hotel"), Hotel("Best2 Hotel"), Hotel("Best3 Hotel"), Hotel("Best4 Hotel")]}


pickle.dump(d, file)
file.close()

