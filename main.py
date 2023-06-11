from movie_app import MovieApp
from storage_csv import StorageCSV
from storage_json import StorageJson
from movie_app import MovieApp
from menu import *


def main():
    """ This function stores the data from the movies and executes the menu """
    # storage = StorageCSV('movies.csv')
    storage = StorageCSV('movies_2.json')
    movie_app = MovieApp(storage)
    while True:
        choice = display_menu()
        movie_app.run(choice)
        input(Fore.YELLOW + 'Press enter to continue ' + Fore.RESET)


if __name__ == "__main__":
    main()
