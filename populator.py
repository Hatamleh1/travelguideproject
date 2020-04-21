from hotel import *
import pickle

file = open('hotel_list', 'wb')
<<<<<<< HEAD
l = [Hotel('Wellington_ams'), Hotel('W Hotel_ams')]
=======
l =[
    Hotel('Wellington'),
    Hotel('W Hotel')
]
>>>>>>> master

pickle.dump(l, file)
