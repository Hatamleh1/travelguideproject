from restaurant import *
import pickle

file = open('restaurant_dict', 'wb')

d = {"Amsterdam": [Restaurant("Amsterdam1 Restaurant"), Restaurant("Amsterdam2 Restaurant"), Restaurant("Amsterdam3 Restaurant"), Restaurant("Amsterdam4 Restaurant")],
     "Haag": [Restaurant("Hague1 Restaurant"), Restaurant("Hague2 Restaurant"), Restaurant("Hague3 Restaurant"), Restaurant("Hague4 Restaurant")],
     "Rotterdam": [Restaurant("Rotterdam Restaurant"), Restaurant("Rotterdam2 Restaurant"), Restaurant("Roterdam3 Restaurant"), Restaurant("Rotterdam4 Restaurant")],
     "Best": [Restaurant("Best Restaurant"), Restaurant("Best2 Restaurant"), Restaurant("Best3 Restaurant"), Restaurant("Best4 Restaurant")]}

pickle.dump(d, file)
file.close()

