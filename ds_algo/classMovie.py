"""
-------------------------------------------------------
movie.py
Movie class definition.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-01-28"
-------------------------------------------------------
"""


class Movie:
    """
    Defines data for a single movie: title, year, director, rating, genres.
    """
    # Constants
    MIN_RATING = 0
    MAX_RATING = 10
    FIRST_YEAR = 1888
    GENRES = ("science fiction", "fantasy", "drama",
              "romance", "comedy", "zombie", "action",
              "historical", "horror", "war")
    # Defines a range of valid integer genre codes:
    GENRE_CODES = range(len(GENRES))

    def __init__(self, title, year, director, rating, genres):
        """
        -------------------------------------------------------
        Initialize a Movie object.
        Use: movie = Movie(title, year, director, rating, genres)
        -------------------------------------------------------
        Preconditions:
            title - movie title (str)
            year - year of release (int)
            director - name of director (str)
            rating - rating of 1 - 10 from IMDB (float)
            genres - numbers representing movie genres_list (list of int)
        Postconditions:
            Movie values are set.
        -------------------------------------------------------
        """
        assert year >= Movie.FIRST_YEAR, "Movie year must be >= {}".format(
            Movie.FIRST_YEAR)
        assert rating is None or Movie.MIN_RATING <= rating <= Movie.MAX_RATING, \
            "Movie ratings must be between {} and {}".format(
                Movie.MIN_RATING, Movie.MAX_RATING)
        assert genres == [] or min(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            min(genres))
        assert genres == [] or max(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            max(genres))

        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genres = genres
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie data.
        Use: print(m)
        Use: string = str(m)
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of movie (str)
        -------------------------------------------------------
        """
        # Generate the list of genres as a string.
        genres_list = self.genres_string()

        string = """Title:    {}
Year:     {}
Director: {}
Rating:   {}
Genres:   {}""".format(self.title, self.year, self.director, self.rating, genres_list)
        return string

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this movie against another movie for equality.
        Use: m1 == m2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] movie to compare to (movie)
        Postconditions:
            returns
            result - True if title and year match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) == \
            (rs.title.lower(), rs.year)
        return result

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this movie comes before another.
        Use: m1 < m2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] movie to compare to (movie)
        Postconditions:
            returns
            result - True if movie precedes rs, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) < \
            (rs.title.lower(), rs.year)
        return result

    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this movie precedes or is or equal to another.
        Use: m1 <= m2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] movie to compare to (movie)
        Postconditions:
            returns
            result - True if this movie precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < rs or self == rs
        return result

    def genres_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genres based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "science fiction, drama"
        Use: string = g.genres_string()
        -------------------------------------------------------
        Postconditions:
            returns
            string - string of genres (str)
        -------------------------------------------------------
        """
        string = ""
        n = len(self.genres)
        i = 0

        while i < n - 1:
            string += Movie.GENRES[self.genres[i]] + ", "
            i += 1

        string += Movie.GENRES[self.genres[i]]
        return string

    def write(self, fv):
        """
        -------------------------------------------------------
        Writes a single line of movie data to an open file fv.
        Use: m.write(fv)
        -------------------------------------------------------
        Preconditions:
            fv - an already open file of movie data (file)
        Postconditions:
            The contents of movie are written as a string in the format
              title|year|director|rating|code to file_variable.
        -------------------------------------------------------
        """
        print("{}|{}|{}|{}|{}"
              .format(self.title, self.year, self.director,
                      self.rating, self.genres_list),
              file=fv)
        return

    def key(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie key data.
        Use: key = m.key()
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of movie key (str)
        -------------------------------------------------------
        """
        string = "{}, {}".format(self.title, self.year)
        return string

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a movie name.
        Use: h = hash(movie)
        -------------------------------------------------------
        Postconditions:
            returns
            value - the total of the characters in the name string
                multiplied by the year (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.title:
            value = value + ord(c)
        value *= self.year
        return value