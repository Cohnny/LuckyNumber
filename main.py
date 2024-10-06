from datetime import datetime


def get_player_name():
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


def get_player_birthdate():
    player_birthdate = 0
    run = True

    while run:
        birthdate = input("Enter your birthdate (yyyymmdd): ")

        if len(birthdate) == 8 and birthdate.isdigit():
            year = int(birthdate[:4])
            month = int(birthdate[4:6])
            day = int(birthdate[6:8])

            # Validate year, month, and day
            if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                player_birthdate = f"{year:04d}-{month:02d}-{day:02d}"
                run = False
            else:
                print("Invalid input. Please ensure the year is at least 1900, month is 01-12, and day is 01-31.")
        else:
            print("Please enter the birthdate in the correct format (yyyymmdd).")

    return player_birthdate


def calculate_player_age(player_birthdate):
    birthdate = datetime.strptime(player_birthdate, "%Y-%m-%d")
    today = datetime.today()
    player_age = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        player_age -= 1

    return player_age


def main():
    player_name = get_player_name()
    player_birthdate = get_player_birthdate()
    player_age = calculate_player_age(player_birthdate)
    while player_age < 18:
        print(f"You need to be at least 18 years old to play. You entered that you are {player_age} years old.")
        player_birthdate = get_player_birthdate()
        player_age = calculate_player_age(player_birthdate)


main()
