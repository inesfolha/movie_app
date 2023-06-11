from movie_app import MovieApp
from storage_csv import StorageCSV
from storage_json import StorageJson
from movie_app import MovieApp
from menu import *


def main():
    """
       Executes the main functionality of the movie app.

       - Initializes the storage object (either StorageCSV or StorageJson).
       - Creates an instance of the MovieApp class using the storage object.
       - Displays the menu and prompts the user for a choice.
       - Executes the corresponding command based on the user's choice using the movie_app object.
       - Prompts the user to press enter to continue after executing a command.
       """

    # storage = StorageCSV('movies.csv')
    storage = StorageJson('movies_2.json')
    movie_app = MovieApp(storage)
    while True:
        choice = display_menu()
        movie_app.run(choice)
        input(Fore.YELLOW + 'Press enter to continue ' + Fore.RESET)


if __name__ == "__main__":
    main()
