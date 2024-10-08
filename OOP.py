import random
from datetime import datetime


class Player:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.age = 0

    def set_player_name(self):
        """ Asks user to enter full name, validates the input. """
        while True:
            name = input("Enter your full name (example: John Doe): ")
            name_split = name.split()

            if len(name_split) == 2 and all(part.isalpha() for part in name_split):
                self.name = f"{name_split[0].capitalize()} {name_split[1].capitalize()}"
                break
            else:
                print("Please enter a valid name with a first and last name using only alphabetic characters.")

    def set_player_birthdate(self):
        """ Asks user to enter birthdate, validates input and returns it. """
        while True:
            birthdate = input("Enter your birthdate (yyyymmdd): ")

            if len(birthdate) == 8 and birthdate.isdigit():
                year = int(birthdate[:4])
                month = int(birthdate[4:6])
                day = int(birthdate[6:8])

                if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                    self.birthdate = f"{year:04d}-{month:02d}-{day:02d}"
                    break
                else:
                    print("Invalid input. Please ensure the year is at least 1900, month is 01-12, and day is 01-31.")
            else:
                print("Please enter the birthdate in the correct format (yyyymmdd).")

    def calculate_age(self):
        """ Calculates the age of the player. """
        birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d")
        today = datetime.today()
        self.age = today.year - birthdate.year

        if (today.month, today.day) < (birthdate.month, birthdate.day):
            self.age -= 1


class Game:
    def __init__(self):
        self.lucky_list = []
        self.lucky_number = 0
        self.tries_count = 0

    def create_lucky_list(self):
        """ Creates a list of 9 unique lucky numbers. """
        self.lucky_list = random.sample(range(101), 9)

    def add_lucky_number_to_list(self):
        """ Generates and adds a lucky number to the list. """
        self.lucky_number = random.randint(0, 100)
        self.lucky_list.append(self.lucky_number)

    def print_lucky_list(self):
        """ Prints the lucky numbers. """
        print("Your lucky numbers are:", self.lucky_list)

    def modify_lucky_list(self):
        """ Generates a new lucky list based on the lucky number. """
        return [num for num in self.lucky_list if self.lucky_number - 10 <= num <= self.lucky_number + 10]

    def play(self):
        """ Core game logic. """
        self.create_lucky_list()
        self.add_lucky_number_to_list()
        self.print_lucky_list()

        while True:
            player_input = int(input("Pick your lucky number from the lucky list: "))
            self.tries_count += 1

            if player_input == self.lucky_number:
                print(f"Congrats, game is over! You got lucky number from try #{self.tries_count} :)")
                return True

            shorter_lucky_list = self.modify_lucky_list()

            if self.tries_count > 1 and player_input in shorter_lucky_list:
                shorter_lucky_list.remove(player_input)

            if len(shorter_lucky_list) <= 2:
                print("Game over! The lucky number was:", self.lucky_number)
                return False

            print(f"This is try #{self.tries_count} and new list is: {shorter_lucky_list}, choose the lucky number?")

    def restart_game(self):
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


def main():
    player = Player()
    player.set_player_name()
    player.set_player_birthdate()
    player.calculate_age()

    while player.age < 18:
        print(f"You need to be at least 18 years old to play. You entered that you are {player.age} years old.")
        player.set_player_birthdate()
        player.calculate_age()

    while True:
        game = Game()
        game.play()

        choice = game.restart_game()

        if choice == 'n':
            break
        elif choice == 'y':
            continue


main()
