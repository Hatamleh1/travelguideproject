from hotel import *
import pickle

file = open('hotel_dict', 'wb')

d = {"Amsterdam": [Hotel("Hotel V Nesplein"), Hotel("Motel Waterlooplein"), Hotel("Hyatt Regency"), Hotel("Estherea")],
     "Haag": [Hotel("Hilton The Hague"), Hotel("Hotel Des Indes"), Hotel("Crown Plaza"), Hotel("Staybridge Suites")],
     "Rotterdam": [Hotel("Hotel Mainport"), Hotel("Hilton Rotterdam"), Hotel("Rotterdam Marriott"), Hotel("nhow Rotterdam")]}


pickle.dump(d, file)
file.close()

