#!/usr/bin/env python3

# IMDB top 10 movies

# my_tuple argument's elements should be in "Title Year Rating" format
def list_movies(my_tuple):
    print("{0:50} {1:^50} {2:>50}".format("Title", "Year", "Rating"))
    print("-"*153)
    for element in my_tuple:
        print("{0:50} {1:^50} {2:>50}".format(element[0], element[1], element[2]))
    print("\n")


def main():
    imdb_top_ten_movies = [("The Shawshank Redemption", 1994, 9.2),
                           ("The Godfather", 1972, 9.2),
                           ("The Dark Knight", 2008, 9.0),
                           ("The Godfather Part II", 1974, 9.0),
                           ("12 Angry Men", 1957, 9.0),
                           ("Schindler's List", 1993, 8.9),
                           ("The Lord of the Rings: The Return of the King", 2003, 8.9),
                           ("Pulp Fiction", 1994, 8.8),
                           ("The Lord of the Rings: The Fellowship of the Ring", 2001, 8.8),
                           ("The Good, the Bad and the Ugly", 1966, 8.8)]
    list_movies(imdb_top_ten_movies)

    star_wars_movies_chronologically = [("Episode I.: The Phantom Menace", 1999, 6.5),
                                        ("Episode II.: Attack of the Clones", 2002, 6.6),
                                        ("Episode III.: Revenge of the Sith", 2005, 6.5),
                                        ("Episode IV.: A New Hope", 1977, 8.6),
                                        ("Episode V.: The Empire Strikes Back", 1980, 8.7),
                                        ("Episode VI.: Return of the Jedi", 1983, 8.3),
                                        ("Episode VII.: The Force Awakens", 2015, 7.8),
                                        ("Episode VII.: The Last Jedi", 2017, 6.9),
                                        ("Episode IX.: The Rise of Skywalker", 2019, 6.5)]
    
    list_movies(star_wars_movies_chronologically)




if __name__ == "__main__":
    main()