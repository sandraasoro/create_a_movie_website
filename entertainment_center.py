#Stage 3: Create a Movie Website


#Define instances of the class Movie defined in media.py and follow by opening the fresh_tomoatoes.html to see your webpage
import fresh_tomatoes
import media

# The structure from media was (self, movie_title,movie_storyline,poster_image, trailer_youtube)
# It is repeated below with other films in the website project
love_and_basketball = media.Movie ("Love and Basketball",
"All is fair in love and basketball",
"http://image.tmdb.org/t/p/original/zQoCjIInTAmt7LTLRNOiPMAeb8E.jpg",
"https://www.youtube.com/watch?v=tKXP-KrY2UY")

my_girl = media.Movie ("My Girl",
"An 11-year-old girl and a hypochondriac Harry Sultenfuss is an awkward widower who does not understand his daughter, so he constantly ignores her. ",
"http://ia.media-imdb.com/images/M/MV5BMTkwNjA5MzQ2OV5BMl5BanBnXkFtZTcwMjAxMDYyMQ@@._V1._SX336_SY475_.jpg",
"https://www.youtube.com/watch?v=GreDP22A-0k")

the_godfather = media.Movie ("The Godfather",
"The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. ",
"http://img.goldposter.com/2015/04/The-Godfather_poster_goldposter_com_2.jpg",
"https://www.youtube.com/watch?v=sY1S34973zA")

the_wizard_of_oz= media.Movie ("The Wizard of Oz",
"When a tornado rips through Kansas, Dorothy and her dog, Toto, are whisked away in their house to the magical land of Oz",
"http://www.blogcdn.com/news.moviefone.com/media/2013/07/wizard-of-oz-imax3d-poster-660.jpg",
"https://www.youtube.com/watch?v=FfpF8UUVTeM")

forrest_gump = media.Movie ("Forrest Gump",
"Forrest Gump as he discusses his relative level of intelligence with a stranger while waiting for a bus.",
"http://www.tribute.ca/tribute_objects/images/movies/Forrest_Gump/forrestgump.jpg",
"https://www.youtube.com/watch?v=bLvqoHBptjg")

#The create an array of the movies described above and initiate a way to create the fresh_tomatoes.html.
movies = [love_and_basketball, my_girl, the_godfather, the_wizard_of_oz, forrest_gump]
fresh_tomatoes.open_movies_page(movies)

""" entertainment_center is a student built portion of the Udacity Full Stack Nano Degree Project 1 "Movie Trailer Website"""