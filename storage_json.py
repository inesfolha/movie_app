from colorama import Fore

import file_handler
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.movies = file_handler.load_data(file_path)
        self.file_path = file_path

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster, movie_link):
        if rating is not None:
            self.movies[title] = {'rating': float(rating), 'release_year': int(year), 'poster_url': poster,
                                  'movie_link': movie_link}
        else:
            self.movies[title] = {'rating': None, 'release_year': int(year), 'poster_url': poster,
                                  'movie_link': movie_link}
            print(Fore.GREEN + f'Movie "{title}" successfully added to the collection!' + Fore.RESET)

            file_handler.save_file(self.file_path, self.movies)

    def delete_movie(self, title):
        movie_to_delete = None

        for movie in self.movies:
            if title.lower() == movie.lower():
                movie_to_delete = movie
                break

        if movie_to_delete is not None:
            del self.movies[movie_to_delete]
            print(Fore.GREEN + f'Movie "{movie_to_delete}" successfully deleted' + Fore.RESET)
            file_handler.save_file(self.file_path, self.movies)
        else:
            print(Fore.RED + f'Movie "{title}" not found!' + Fore.RESET)

    def update_movie(self, title, notes):

        movie_to_update = None

        for movie in self.movies:
            if title.lower() == movie.lower():
                movie_to_update = movie
                break

        if movie_to_update is not None:
            self.movies[movie_to_update]['notes'] = notes
            print(Fore.GREEN + f"Movie {title} note updated successfully." + Fore.RESET)

            file_handler.save_file(self.file_path, self.movies)

        else:
            print(Fore.RED + f'Movie "{title}" not found.' + Fore.RESET)
