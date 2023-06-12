from colorama import Fore

import file_handler
from istorage import IStorage


class StorageCSV(IStorage):
    def __init__(self, file_path):
        self.file = file_handler.load_csv(file_path)
        self.movies = {}
        for movie in self.file:
            if len(movie) >= 6:
                movie_data = {'release_year': movie[2], 'rating': movie[1], 'poster': movie[3], 'movie_link': movie[4],
                              'notes': movie[5]}
                self.movies[movie[0]] = movie_data

    def list_movies(self):
        return self.movies

    def return_to_csv(self):
        data = []
        for movie in self.movies:
            movie_row = [movie, self.movies[movie]['rating'], self.movies[movie]['release_year'],
                         self.movies[movie]['poster'],
                         self.movies[movie]['movie_link'], self.movies[movie]['notes']]
            data.append(movie_row)
        return data

    def add_movie(self, title, rating, year, poster, movie_link):
        if rating is not None and rating != '':
            self.movies[title] = {'rating': float(rating), 'release_year': int(year), 'poster': poster,
                                  'movie_link': movie_link, 'notes': None}
        else:
            self.movies[title] = {'rating': None, 'release_year': int(year), 'poster': poster,
                                  'movie_link': movie_link, 'notes': None}

        data = self.return_to_csv()
        file_handler.save_csv('movies.csv', data)

    def delete_movie(self, title):
        movie_to_delete = None

        for movie in self.movies:
            if title.lower() == movie.lower():
                movie_to_delete = movie
                break

        if movie_to_delete is not None:
            del self.movies[movie_to_delete]
            print(Fore.GREEN + f'Movie "{movie_to_delete}" successfully deleted' + Fore.RESET)
            data = self.return_to_csv()
            file_handler.save_csv('movies.csv', data)

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

            data = self.return_to_csv()
            file_handler.save_csv('movies.csv', data)

        else:
            print(Fore.RED + f'Movie "{title}" not found.' + Fore.RESET)
