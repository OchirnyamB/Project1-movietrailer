import karaoke

import fresh_tomatoes

# Comments are now properly style where every comment has a space after '#'
# This is the same movie trailer project which
# i finished it in the intro to programming course.
# Except I have modified the movie trailers to Mongolian karaoke songs :).

# Creating the variables which later calls into the class Karaoke.
# Instance code lines are not longer than the maximum
# length of 72-99 characters anymore.
# The code has been successfully passed and checked through PEP8

javkhlan = karaoke.Karaoke(
   "Javkhlan Mongoljingoo",
   "Javkhlan is a Mongolian singer",
   "http://i.ytimg.com/vi/XpmQa9-OXpQ/maxresdefault.jpg",
   "https://www.youtube.com/watch?v=VHAWgAT-QRo")

javkhlan2 = karaoke.Karaoke(
   "Nasan bagiin dursamj",
   "Javkhlan is a Mongolian singer",
   "http://www.miniih.com/miniiblog/misia/files/s_javkhlan-middle.jpg",
   "https://www.youtube.com/watch?v=kBrt8yVay0E")

bx = karaoke.Karaoke(
   "Sorrow",
   "BX is a Mongolian pop singer",
   "http://www.infomongolia.com/images/stories/news/news/2012/02_february/02/bx_singer.gif",  # noqa
   "https://www.youtube.com/watch?v=BVj1SdxzdCo")  # noqa

bx2 = karaoke.Karaoke(
   "My love", "BX is a Mongolian pop singer",
   "http://stat.gogo.mn/blog/9/77689/mglinstrumental/url.jpg",
   "https://www.youtube.com/watch?v=4wGiBzv8B0U")

batbold = karaoke.Karaoke(
   "Bi Mongol Er Hun", "Batbold duuchin hun",
   "http://i.ytimg.com/vi/_n_N69oRb7k/maxresdefault.jpg",
   "https://www.youtube.com/watch?v=OIjfMLOEGGM")

purevsuren = karaoke.Karaoke(
   "Ekhiin Duu", "Eejiin tuhai goy duu",
   "http://i.ytimg.com/vi/s6ct_kZba74/maxresdefault.jpg",
   "https://www.youtube.com/watch?v=8QZH451A80o")

# Storing the variables in an array in order to call for
# the function open_movies_page in fresh_tomatoes.py.

songs = [javkhlan, javkhlan2, bx, bx2, batbold, purevsuren]

fresh_tomatoes.open_movies_page(songs)

# Here printing the documentation of what the karaoke.py has.
print(karaoke.Karaoke.__doc__)
