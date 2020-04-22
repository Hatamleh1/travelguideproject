from hotel import *
import pickle

file = open('hotel_list', 'wb')

d = [Hotel('Hotel W'), Hotel('Yellow Hotel'), Hotel('Wellington'), Hotel('Ibis Hotel'), Hotel('Marriot Hotel')]

pickle.dump(d, file)
file.close()

