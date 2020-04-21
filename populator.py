from hotel import *
import pickle

file = open('hotel_list', 'wb')

d = [Hotel('Hotel W'), Hotel('Yellow Hotel')]

pickle.dump(d, file)
file.close()

