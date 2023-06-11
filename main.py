from movie_app import MovieApp
from storage_csv import StorageCSV
from storage_json import StorageJson
from movie_app import MovieApp
from menu import *
import argparse


def main():
    """
       Executes the main functionality of the movie app.

       - Initializes the storage object based on the specified file.
       - Creates an instance of the MovieApp class using the storage object.
       - Displays the menu and prompts the user for a choice.
       - Executes the corresponding command based on the user's choice using the movie_app object.
       - Prompts the user to press enter to continue after executing a command.
       """
    parser = argparse.ArgumentParser(description='Movie App')
    parser.add_argument('file', help='Path to the storage file')
    args = parser.parse_args()

    file_extension = args.file.split('.')[-1].lower()

    if file_extension == 'csv':
        from storage_csv import StorageCSV
        storage = StorageCSV(args.file)
    elif file_extension == 'json':
        from storage_json import StorageJson
        storage = StorageJson(args.file)
    else:
        raise ValueError(f'Unsupported file extension: {file_extension}')

    movie_app = MovieApp(storage)
    while True:
        choice = display_menu()
        movie_app.run(choice)
        input(Fore.YELLOW + 'Press enter to continue ' + Fore.RESET)


if __name__ == "__main__":
    main()
