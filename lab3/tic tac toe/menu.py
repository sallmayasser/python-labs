from utils import clear_screen

class Menu:
    def validate_choice(self):
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                return choice
            print("Invalid choice. Please enter 1 or 2.")

    def display_main_menu(self):
        print("Welcome to My Tic Tac Toe Game.")
        print("*"*35)
        print("1. Start Game")
        print("2. Exit Game")
        choice = self.validate_choice()
        clear_screen()
        return choice

    def display_endgame_menu(self):
        print("Game Over!")
        print("1. Restart")
        print("2. Exit Game")
        choice = self.validate_choice()
        return choice
