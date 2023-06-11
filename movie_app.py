from movies_display_data import *
from get_api_data import *
from website_generator import *
from menu import *


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        """Prints all the movies, along with their rating 
        and prints how many movies there are in total in the database."""

        print(f'{len(movies)} movies in total:')
        [print(f"{movie}: Rating: {movies[movie]['rating']} Year: {movies[movie]['release_year']}") for movie in
         movies.keys()]

    def _command_add_movie(self):
        """ Asks the user for input and searches the API for the requested movie,
        if the movie is found, it then extracts the movie information
        and calls the add_movie method to store the information in a file"""

        movie = input(
            Fore.YELLOW + 'Please enter a new movie: ' + Fore.RESET)
        try:
            movie_info = data_extractor(movie)
            movie_link = get_imdb_link(movie)
            if movie_info is not None:
                title = movie_info["Title"]
                if len(movie_info['Ratings']) > 0:
                    rating = float(movie_info['Ratings'][0]['Value'].split("/")[0])
                else:
                    rating = None
                year = int(movie_info['Year'])
                poster = movie_info['Poster']

                self._storage.add_movie(title, rating, year, poster, movie_link)
                print(Fore.GREEN + f'Movie "{title}" successfully added to the collection!' + Fore.RESET)
            else:
                raise ValueError(
                    f'Sorry, the movie "{movie}" could not be found. Please check your spelling and try again.')

        except (KeyError, ValueError) as e:
            print(Fore.RED + 'Please try again with a different movie.' + Fore.RESET)
        except Exception as e:
            print(
                Fore.RED + 'An unexpected error occurred while adding the movie. Please try again later.' + Fore.RESET)
            print(Fore.RED + f'Error message: {str(e)}' + Fore.RESET)

    def _command_delete_movie(self):
        """Asks the user for the name of the movie to delete
        It then cals the delete_movie method """

        try:
            title = input(Fore.YELLOW + 'Enter movie name to delete: ' + Fore.RESET)
            self._storage.delete_movie(title)

        except Exception as e:
            print(
                Fore.RED + 'An unexpected error occurred while deleting the movie. Please try again later.' + Fore.RESET)
            print(Fore.RED + f'Error message: {str(e)}' + Fore.RESET)

    def _command_update_movie(self):
        """Asks the user for the name of the movie to update
            It then cals the update_movie method """
        try:
            title = input(Fore.YELLOW + "Enter the movie name: " + Fore.RESET)
            notes = (input(Fore.YELLOW + "Enter movie notes: " + Fore.RESET))
            self._storage.update_movie(title, notes)
        except Exception as e:
            print(
                Fore.RED + 'An unexpected error occurred while updating the movie. Please try again later.' + Fore.RESET)
            print(Fore.RED + f'Error message: {str(e)}' + Fore.RESET)

    def _command_movie_stats(self):
        """Prints statistics about the movies, such as total count,
        average rating, and release year range."""
        movies = self._storage.list_movies()
        movie_stats(movies)

    def _command_ratings_histogram(self):
        """Generates a histogram of the movie ratings."""
        movies = self._storage.list_movies()
        ratings_histogram(movies)

    def _command_random_movie(self):
        """Selects and displays a random movie from the collection."""
        movies = self._storage.list_movies()
        random_movie(movies)

    def _command_search_movie(self):
        """Allows the user to search for a movie by title or keyword."""
        movies = self._storage.list_movies()
        movie_search(movies)

    def _command_sorted_movies(self):
        """Displays the movies in sorted order based on rating."""
        movies = self._storage.list_movies()
        top_movies(movies)

    def _command_generate_website(self):
        """Generates a website with information about the movies and saves it to a file."""
        movies_dict = self._storage.list_movies()
        movies_dict = self._storage.list_movies()
        serialize_info(movies_dict)
        html_generator(movies_dict)

    def run(self, choice):
        """Runs the specified command based on the user's choice."""
        if choice == 1:
            self._command_list_movies()
        elif choice == 2:
            self._command_add_movie()
        elif choice == 3:
            self._command_delete_movie()
        elif choice == 4:
            self._command_update_movie()
        elif choice == 5:
            self._command_movie_stats()
        elif choice == 6:
            self._command_random_movie()
        elif choice == 7:
            self._command_search_movie()
        elif choice == 8:
            self._command_sorted_movies()
        elif choice == 9:
            self._command_ratings_histogram()
        elif choice == 10:
            self._command_generate_website()
        elif choice == 0:
            print(Fore.GREEN + "Bye!" + Fore.RESET)
            quit()
        else:
            print(f'Error: Choice {choice} not supported! Try again.')

