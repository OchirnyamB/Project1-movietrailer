import webbrowser


class Karaoke():
    """This class provides a way to store song related information"""

# Preexisting class variable __doc__
# The function __init__ gets called first

    def __init__(
        self, song_title, singer_description,
            poster_image, trailer_youtube):

            # instant variables
            self.title = song_title
            self.storyline = singer_description
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

# The code has been successfully passed and checked through PEP8 :).
# Thank you for introducing me to PEP8!
# Now all the code structures are good to go.
