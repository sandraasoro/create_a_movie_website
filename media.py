# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:31:53 2016

@author: OTeniola-LPTP
"""

import webbrowser
class Movie():
# Movie creates the structure for the multiple arrays in entertainment_center.py
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
                  
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)