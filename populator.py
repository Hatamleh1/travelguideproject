from hotel import *
import pickle

file = open('hotel_list', 'wb')

d = {Hotel("Amsterdam"): ["a", "b", "c"], Hotel("The Hague"): ["d", "e, f"], Hotel("Rotterdam"):["g", "h", "i"]}


print(d)

pickle.dump(d, file)
file.close()

