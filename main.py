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
    for i in range(9):
        random_number = get_random_integer()
        lucky_list.append(random_number)

    return lucky_list


def print_lucky_list(lucky_list):
    """ Prints the lucky numbers """
    random.shuffle(lucky_list)
    lucky_numbers = "Your lucky numbers are: "

    for num in lucky_list:
        lucky_numbers += str(num) + ", "

    lucky_numbers = lucky_numbers.rstrip(", ")

    print(lucky_numbers)


def main():
    player_name = set_player_name()
    player_birthdate = set_player_birthdate()
    player_age = calculate_player_age(player_birthdate)
    while player_age < 18:
        print(f"You need to be at least 18 years old to play. You entered that you are {player_age} years old.")
        player_birthdate = set_player_birthdate()
        player_age = calculate_player_age(player_birthdate)
    lucky_list = create_lucky_list()
    lucky_number = get_random_integer()
    lucky_list.append(lucky_number)
    print_lucky_list(lucky_list)



main()
