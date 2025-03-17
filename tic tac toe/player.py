class Player:

    def _init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name. isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self, other_player_symbol=None):
        while True:
            symbol = input(
                f"{self.name}, choose your symbol (a single letter): ")

            if symbol.isalpha() and len(symbol) == 1:
                symbol = symbol.upper()

                if other_player_symbol and symbol == other_player_symbol:
                    print(
                        "Symbol already chosen by the other player. Choose a different one.")
                    continue

                self.symbol = symbol
                break

            print("Invalid symbol. Please choose a single letter.")
