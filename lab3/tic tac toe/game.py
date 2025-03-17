from menu import Menu
from player import Player
from board import Board
from utils import clear_screen


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            # First player chooses symbol freely
            if number == 1:
                player.choose_symbol()
            else:
                # Second player must choose a different symbol
                player.choose_symbol(self.players[0].symbol)
            print("---"*20)
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                self.board.display_board()
                print(f"{self.players[self.current_player_index].name} wins!")
                print("*"*25)
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                self.board.display_board()
                print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.switch_player()
        self.play_game()

    def check_win(self):
        win_combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in win_combination:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit()for cell in self.board.board)

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        if not self.check_win() and not self.check_draw():
            self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for Playing!")
