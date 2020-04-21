from hotel import *
import pickle

file = open('hotel_list', 'wb')
<<<<<<< HEAD
<<<<<<< HEAD
l = [Hotel('Wellington_ams'), Hotel('W Hotel_ams')]
=======
l =[
    Hotel('Wellington'),
    Hotel('W Hotel')
]
>>>>>>> master

pickle.dump(l, file)
=======

d = {Hotel("Amsterdam"): ["a", "b", "c"], Hotel("The Hague"): ["d", "e, f"], Hotel("Rotterdam"):["g", "h", "i"]}


print(d)

pickle.dump(d, file)
file.close()

>>>>>>> master
