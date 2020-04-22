from restaurant import *
import pickle

file = open('restaurant_dict', 'wb')

d = {"Amsterdam": [Restaurant("Amsterdam1 Rest"), Restaurant("Amsterdam2 Rest"), Restaurant("Amsterdam3 Rest"), Restaurant("Amsterdam4 Rest")],
     "Haag": [Restaurant("Hague1 Rest"), Restaurant("Hague2 Rest"), Restaurant("Hague3 Rest"), Restaurant("Hague4 Rest")],
     "Rotterdam": [Restaurant("Rotterdam Rest"), Restaurant("Rotterdam2 Rest"), Restaurant("Rotterdam3 Rest"), Restaurant("Rotterdam4 Rest")],
     }

pickle.dump(d, file)
file.close()

