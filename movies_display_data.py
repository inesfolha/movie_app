import random

import matplotlib.pyplot as plt
from colorama import init, Fore
from fuzzywuzzy import fuzz

init()


def ratings_list(movies):
    rated_movies = [movie for movie in movies if movies[movie]['rating'] is not None and movies[movie]['rating'] != '']

    if len(rated_movies) == 0:
        print("There are no rated movies in the database.")

    ratings = []
    for movie in rated_movies:
        rating = float(movies[movie]['rating'])
        ratings.append(rating)
    return ratings, rated_movies


def avg_rating(movies):
    """calculates the average rating"""
    ratings = ratings_list(movies)[0]
    rated_movies = ratings_list(movies)[1]
    average = sum(movie for movie in ratings) / len(rated_movies)
    print(f"Average rating: {average:.1f}")


def median_rating(movies):
    """calculates the median rating"""
    ratings = ratings_list(movies)[0]
    sorted_ratings = sorted(ratings)

    mid = len(sorted_ratings) // 2
    if len(sorted_ratings) % 2 == 0:
        median = (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2
    else:
        median = sorted_ratings[mid]
    print(f"Median rating: {median:.1f}")


def get_best_and_worst(movies):
    """finds the best and worst rated movies"""

    rated_movies = [(movie, float(data['rating'])) for movie, data in movies.items()
                    if data['rating'] is not None and data['rating'] != '']

    max_rating = max(rated_movies, key=lambda x: x[1])[1]
    min_rating = min(rated_movies, key=lambda x: x[1])[1]

    best_movies = []
    worst_movies = []
    for movie, rating in rated_movies:
        if rating == max_rating:
            best_movies.append((movie, rating))
        elif rating == min_rating:
            worst_movies.append((movie, rating))

    print('Best Movies:')
    for movie, rating in best_movies:
        print(f"{movie}, {rating}")
    print('Worst Movies:')
    for movie, rating in worst_movies:
        print(f"{movie}, {rating}")


def movie_stats(movies):
    """Calculates and prints statistics about the movies in the database:
        Average rating, Median rating, The best movie and The worst movie"""
    avg_rating(movies)
    median_rating(movies)
    get_best_and_worst(movies)


def random_movie(movies):
    """ This function prints a random movie, and it’s rating. """
    suggestion_movie = random.choice(list(movies.keys()))
    rating = movies[suggestion_movie]
    print(f"Your movie suggestion: {suggestion_movie}, it's rated {movies[suggestion_movie]['rating']}")


def movie_search(movies):
    """ This function asks the user to enter a part of a movie name, and then search all the movies in the database,
    it then prints all the movies that matched the user’s query, along with the rating.
    If the movie searched is not in the database, it looks for similar names using the fuzz module from the fuzzywuzzy
    library and prints them by similarity order """

    search = input(Fore.YELLOW + "Enter part of a movie name: " + Fore.RESET)
    matching_movies = []
    for movie, rating in movies.items():
        # Using the fuzz.token_set_ratio function to compare the user's search string with each movie name
        ratio = fuzz.token_set_ratio(search.lower(), movie.lower())
        # Define a threshold is 70% similarity to consider a match.
        if ratio >= 70:
            matching_movies.append((movie, rating, ratio))
    # Sorting the matching movies by similarity score in descending order
    matching_movies = sorted(matching_movies, key=lambda x: x[2], reverse=True)
    print(f'We found these results matching "{search}":')
    for movie, rating, ratio in matching_movies:
        print(f" {movie}, Rating: {rating} ({ratio}% match)")


def top_movies(movies):
    """This function prints all the movies and their ratings, in descending order by the rating.
    All None ratings are displayed in the end """
    sorted_movies = sorted(movies.items(),
                           key=lambda x: float(x[1]['rating']) if x[1]['rating'] and x[1]['rating'] != ''
                           else float('-inf'), reverse=True)
    print('Movies sorted by rating:')
    for movie, movie_data in sorted_movies:
        rating = movie_data['rating']
        if rating is not None and rating != '':
            print(f" - {movie}: {rating}")
        else:
            print(f" - {movie}: N/A")


def ratings_histogram(movies):
    """ This function creates a histogram of the ratings of the movies.
    then, it asks the user in which file to save the histogram, and save the plot to a file. """
    ratings = [movie_data['rating'] for movie_data in movies.values() if movie_data['rating'] is not None]
    plt.hist(ratings)
    plt.title("Movie Rating Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    file_name = input(
        Fore.YELLOW + "Choose a file name to save the histogram (including file extension): " + Fore.RESET)
    plt.savefig(file_name)
    print(Fore.GREEN + f'Your file {file_name} was successfully saved' + Fore.RESET)
