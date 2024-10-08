import random
from datetime import datetime


def set_player_name():
    """ Asks user to enter full name, validates the input and makes sure that there is a whitespace between them. """
    formatted_name = ""
    run = True

    while run:
        name = input("Enter your full name (example: John Doe): ")
        name_split = name.split()

        if len(name_split) == 2 and all(part.isalpha() for part in name_split):
            formatted_name = f"{name_split[0].capitalize()} {name_split[1].capitalize()}"
            run = False
        else:
            print("Please enter a valid name with a first and last name using only alphabetic characters.")

    return formatted_name


def set_player_birthdate():
    """ Asks user to enter brith date, validates input and then returns it """
    player_birthdate = 0
    run = True

    while run:
        birthdate = input("Enter your birthdate (yyyymmdd): ")

        if len(birthdate) == 8 and birthdate.isdigit():
            year = int(birthdate[:4])
            month = int(birthdate[4:6])
            day = int(birthdate[6:8])

            if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                player_birthdate = f"{year:04d}-{month:02d}-{day:02d}"
                run = False
            else:
                print("Invalid input. Please ensure the year is at least 1900, month is 01-12, and day is 01-31.")
        else:
            print("Please enter the birthdate in the correct format (yyyymmdd).")

    return player_birthdate


def calculate_player_age(player_birthdate):
    """" Takes the player_birthdate and calculates the age of the player """
    birthdate = datetime.strptime(player_birthdate, "%Y-%m-%d")
    today = datetime.today()
    player_age = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        player_age -= 1

    return player_age


def get_random_integer():
    """ Randomly generates a random integer from 0-100 """
    random_int = random.randint(0, 100)

    return random_int


def create_lucky_list():
    """ Creates a list of lucky numbers """
    lucky_list = []

    while len(lucky_list) < 9:
        number = random.randint(0, 100)

        if number not in lucky_list:
            lucky_list.append(number)

    return lucky_list


def add_lucky_number_to_list(lucky_list, lucky_number):
    """ Adds a lucky number to the list """
    while lucky_number in lucky_list:
        lucky_number = random.randint(0, 100)
    lucky_list.append(lucky_number)

    return lucky_list


def print_lucky_list(lucky_list):
    """ Prints the lucky numbers """
    random.shuffle(lucky_list)
    lucky_numbers = "Your lucky numbers are: "

    for num in lucky_list:
        lucky_numbers += str(num) + ", "

    lucky_numbers = lucky_numbers.rstrip(", ")

    print(lucky_numbers)


def player_choice(lucky_list):
    """ Asks user to input a number from the lucky list and returns the player choice """
    guess = 0
    run = True

    while run:
        guess = input(f"Pick a number from the list: ")

        if guess.isdigit():
            guess = int(guess)
            if guess in lucky_list:
                run = False
            else:
                print("Please choose a number from the list.")
        else:
            print("Please enter a valid number.")

    return guess


def modify_lucky_list(lucky_list, lucky_number):
    lower_bound = lucky_number - 10
    upper_bound = lucky_number + 10
    modified_lucky_list = [num for num in lucky_list if lower_bound <= num <= upper_bound]

    return modified_lucky_list


def restart_game():
    """ Asks user to restart the game and returns the choice """
    run = True
    choice = ""

    while run:
        play_again = input("Do you like to play again? (Input y: Yes, n: No): ").lower()

        if play_again == 'n':
            print("Thank you for playing!")
            run = False
            choice = "n"
        elif play_again == 'y':
            print("Starting a new game!")
            run = False
            choice = "y"
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")

    return choice


def play_game():
    """ Core game logic. """
    lucky_list = create_lucky_list()
    lucky_number = get_random_integer()
    add_lucky_number_to_list(lucky_list, lucky_number)
    print_lucky_list(lucky_list)

    tries_count = 0

    while True:
        player_input = int(input("Pick your lucky number from the lucky list: "))
        tries_count += 1

        if player_input == lucky_number:
            print(f"Congrats, game is over! And you got lucky number from try#{tries_count} :) ")
            break
        else:
            shorter_lucky_list = modify_lucky_list(lucky_list, lucky_number)

            if tries_count > 1 and player_input in shorter_lucky_list:
                shorter_lucky_list.remove(player_input)

            if len(shorter_lucky_list) <= 2:
                print("Game over! The lucky number was:", lucky_number)
                break

            print(f"This is try#{tries_count} and new list is: {shorter_lucky_list}, choose the lucky number?")
            lucky_list = shorter_lucky_list


def main():
    player_name = set_player_name()
    player_birthdate = set_player_birthdate()
    player_age = calculate_player_age(player_birthdate)

    while player_age < 18:
        print(f"You need to be at least 18 years old to play. You entered that you are {player_age} years old.")
        player_birthdate = set_player_birthdate()
        player_age = calculate_player_age(player_birthdate)

    while True:
        play_game()

        choice = restart_game()

        if choice == 'n':
            break
        elif choice == 'y':
            continue


main()
