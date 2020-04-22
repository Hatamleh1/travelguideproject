from hotel import *

class Hotel:
    def __init__(self, name):
        self.ratings = []
        self.name = name
    
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 'N/A'
        return str(round(sum(self.ratings) / len(self.ratings), 1))
    
    def rate(self, value):
        try:
            if 0 <= float(value) <= 5:
                self.ratings.append(float(value))
        except:
            pass
