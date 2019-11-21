from fresh_tomatoes import *


class Movie():
    """class Movie saves the information of the movie."""
    def __init__(self, title, image_url, trailer_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url


# instance
butterfly_effect = Movie("The Butterfly Effect",
                         "https://upload.wikimedia.org/wikipedia/"
                         "en/4/43/Butterflyeffect_poster.jpg",
                         "https://www.youtube.com/watch?v=B8_dgqfPXFg")

# instance
artificial_intelligence = Movie("A.I.",
                                "https://upload.wikimedia.org/wikipedia/"
                                "en/e/e6/AI_Poster.jpg",
                                "https://www.youtube.com/watch?v=_19pRsZRiz4")

# instance
secret = Movie("Secret",
               "http://images.wikia.com/drama/es/images/3/3c/9947.jpg",
               "https://www.youtube.com/watch?v=DTDuOkNSJA4&t=19s")


# create movie list
movie_list = [butterfly_effect, artificial_intelligence, secret]

# generate website
open_movies_page(movie_list)
