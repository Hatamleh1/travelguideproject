from hotel import *

<<<<<<< Updated upstream
class Hotel:
=======
class Hotel_Amsterdam:
>>>>>>> Stashed changes
    def __init__(self, name):
        self.ratings = []
        self.name = name
    
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 'N/A'
        return str(sum(self.ratings) / len(self.ratings))
    
    def rate(self, value):
        try:
            if 0 <= float(value) <= 5:
                self.ratings.append(float(value))
        except:
            pass
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
