from colorama import init, Fore

import menu_text

init()


def display_menu():
    """ This function displays the menu and gets the user's choice """
    menu = menu_text.menu
    title = menu_text.title

    print(Fore.BLUE + title + Fore.RESET)
    print(Fore.BLUE + menu + Fore.RESET)

    while True:
        try:
            choice = int(input(Fore.YELLOW + 'Enter choice (0-10): ' + Fore.RESET))
            if choice not in range(0, 11):
                print(f'Error: Choice {choice} not supported! Try again.')
            else:
                return choice
        except ValueError:
            print('Error: Invalid input! Enter an integer between 1 and 10.')


