from restaurant import *
import pickle

file = open('restaurant_dict', 'wb')

d = {"Amsterdam": [Restaurant("Bonboon"), Restaurant("Restaurant Zaza's"), Restaurant("Spectrum "), Restaurant("Ciel Bleu")],
     "Haag": [Restaurant("Restaurant Spijs"), Restaurant("Capriole Cafe"), Restaurant("Ruisenor"), Restaurant("Giuliano's")],
     "Rotterdam": [Restaurant("Vader Kleinjan"), Restaurant("Restaurant Three"), Restaurant("Restaurant Fred"), Restaurant("Restaurant Meatcave")]}

pickle.dump(d, file)
file.close()

