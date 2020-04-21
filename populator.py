from hotel import *
import pickle

file = open('hotel_list', 'wb')
l = [Hotel('Wellington_ams'), Hotel('W Hotel_ams')]

pickle.dump(l, file)
