from finalproject import *
import pickle

file = open('hotel_list_ams', 'wb')

<<<<<<< Updated upstream
d = [Hotel('Hotel W'), Hotel('Yellow Hotel')]

pickle.dump(d, file)
=======
a = [Hotel("Wellington Hotel"), Hotel("W Hotel"), Hotel("Ibis Hotel"), Hotel("Yesllow Hotel")]


pickle.dump(a, file)
>>>>>>> Stashed changes
file.close()

