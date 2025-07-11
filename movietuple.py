class TupledMovie:
    def __init__(self,id,name,year,movie_rated,rating,num_raters,num_reviews):
        self.id = id
        self.name = name
        self.year = year
        self.movie_rated = movie_rated
        self.rating = rating
        self.num_raters=num_raters
        self.num_reviews=num_reviews

    def tupled(self):
        return (self.name, self.year, self.movie_rated, self.rating, self.num_raters, self.num_reviews)